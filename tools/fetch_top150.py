"""Download the LeetCode "Top Interview 150" study plan into top150/.

For every problem it writes
    top150/<NN-group>/<NNNN-slug>/problem.md      (statement, local only / gitignored)
    top150/<NN-group>/<NNNN-slug>/solution.{py,cpp,ts}
and a top150/problems.json index used by tools/progress.py.

Existing solution files are never overwritten, so it is safe to re-run.
Raw API responses are cached in .cache/leetcode/ (use --refresh to refetch).

Usage:  python tools/fetch_top150.py [--refresh]
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "top150"
CACHE = ROOT / ".cache" / "leetcode"
PLAN = "top-interview-150"
API = "https://leetcode.com/graphql/"
LANGS = {"python3": "py", "cpp": "cpp", "typescript": "ts"}

PLAN_QUERY = """query($slug:String!){studyPlanV2Detail(planSlug:$slug){
  name planSubGroups{name questions{titleSlug questionFrontendId}}}}"""
QUESTION_QUERY = """query($s:String!){question(titleSlug:$s){
  questionFrontendId title titleSlug difficulty isPaidOnly content hints
  topicTags{name} metaData exampleTestcaseList codeSnippets{langSlug code}}}"""


def gql(query: str, variables: dict) -> dict:
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "Mozilla/5.0",
        },
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            if data.get("errors"):
                raise RuntimeError(data["errors"])
            return data["data"]
        except Exception as e:  # noqa: BLE001 - retry on any network/API hiccup
            if attempt == 4:
                raise
            print(f"  retry ({e})", file=sys.stderr)
            time.sleep(2 * (attempt + 1))
    raise AssertionError


def cached(name: str, fetch, refresh: bool) -> dict:
    path = CACHE / f"{name}.json"
    if path.exists() and not refresh:
        return json.loads(path.read_text(encoding="utf-8"))
    data = fetch()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    time.sleep(0.4)
    return data


# ---------------------------------------------------------------- HTML -> Markdown
class _MD(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.lists: list[list] = []  # stack of [kind, counter]
        self.pre = 0
        self.code = False

    def w(self, s: str) -> None:
        self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "pre":
            self.pre += 1
            self.w("\n\n```text\n")
        elif self.pre:
            return  # drop <strong> etc. inside code blocks
        elif tag == "p":
            self.w("\n\n")
        elif tag == "br":
            self.w("  \n")
        elif tag in ("strong", "b"):
            self.w("**")
        elif tag in ("em", "i"):
            self.w("*")
        elif tag == "code":
            self.code = True
            self.w("`")
        elif tag == "sup":
            self.w("^" if self.code else "<sup>")
        elif tag == "sub":
            self.w("_" if self.code else "<sub>")
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 0])
            self.w("\n")
        elif tag == "li":
            kind = self.lists[-1] if self.lists else ["ul", 0]
            kind[1] += 1
            bullet = f"{kind[1]}." if kind[0] == "ol" else "-"
            self.w("\n" + "  " * (len(self.lists) - 1) + bullet + " ")
        elif tag == "img":
            self.w(f"\n\n![{a.get('alt') or 'image'}]({a.get('src', '')})\n\n")

    def handle_endtag(self, tag):
        if tag == "pre":
            self.pre -= 1
            if self.out and not self.out[-1].endswith("\n"):
                self.w("\n")
            self.w("```\n\n")
        elif self.pre:
            return
        elif tag in ("strong", "b"):
            self.w("**")
        elif tag in ("em", "i"):
            self.w("*")
        elif tag == "code":
            self.code = False
            self.w("`")
        elif tag == "sup":
            self.w("" if self.code else "</sup>")
        elif tag == "sub":
            self.w("" if self.code else "</sub>")
        elif tag in ("ul", "ol"):
            self.lists.pop()
            self.w("\n\n")

    def handle_data(self, data):
        if self.pre:
            self.w(data.lstrip("\n") if self.out[-1].endswith("```text\n") else data)
        else:
            self.w(re.sub(r"\s+", " ", data.replace("\xa0", " ")))


def html_to_md(src: str) -> str:
    p = _MD()
    p.feed(src)
    md = "".join(p.out)
    md = re.sub(r"\*\*\s*\*\*", "", md)  # empty bold from <strong>&nbsp;</strong>
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


# ---------------------------------------------------------------- templates
def split_definitions(code: str, lang: str) -> tuple[str, str]:
    """Split LeetCode's leading commented-out type definitions (ListNode, TreeNode, Node...)
    from the template. Returns (uncommented definitions, rest of template)."""
    lines = code.replace("\r\n", "\n").split("\n")
    if lang == "py":
        if lines and lines[0].strip() == '"""':
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == '"""')
            body, rest = lines[1:end], lines[end + 1 :]
        else:
            n = 0
            while n < len(lines) and lines[n].startswith("#"):
                n += 1
            body = [re.sub(r"^# ?", "", l) for l in lines[:n]]
            rest = lines[n:]
        defs = [("# " + l if l.lstrip().startswith("Definition") else l) for l in body]
        defs = [l for l in defs if l.strip() and not l.startswith("# Definition")]
    else:
        if not lines or not lines[0].lstrip().startswith("/*"):
            return "", code
        end = next(i for i, l in enumerate(lines) if "*/" in l)
        body, rest = lines[1:end], lines[end + 1 :]
        body = [re.sub(r"^\s?\*( |$)", "", l) for l in body]
        defs = [l for l in body if l.strip() and not re.match(r"\s*(//\s*)?Definition", l)]
    if not any(re.match(r"\s*(class|struct)\s", l) for l in defs):
        return "", code  # leading comment wasn't a definition block
    return "\n".join(defs).strip("\n"), "\n".join(rest).strip("\n")


def fill_python_bodies(code: str) -> str:
    """LeetCode leaves method bodies empty; add `pass` so the file is valid Python."""
    lines = code.split("\n")
    out = []
    for i, line in enumerate(lines):
        out.append(line)
        if re.match(r"\s*def .*:\s*$", line):
            nxt = next((l for l in lines[i + 1 :] if l.strip()), None)
            indent = len(line) - len(line.lstrip())
            if nxt is None or len(nxt) - len(nxt.lstrip()) <= indent:
                out.append(" " * (indent + 4) + "pass")
    return "\n".join(l.rstrip() for l in out)


PY_HEADER = """\
# {fid}. {title}
# {url}
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
import math
"""
CPP_HEADER = """\
// {fid}. {title}
// {url}
#include <bits/stdc++.h>
using namespace std;
"""
TS_HEADER = """\
// {fid}. {title}
// {url}
export {{}}; // local only: gives this file its own module scope
"""
SUBMIT = {"py": "# ---- submit below this line ----", "cpp": "// ---- submit below this line ----",
          "ts": "// ---- submit below this line ----"}
LOCAL = {"py": "# ---- local definitions (do not submit) ----",
         "cpp": "// ---- local definitions (do not submit) ----",
         "ts": "// ---- local definitions (do not submit) ----"}


def build_solution(q: dict, lang: str, code: str) -> str:
    ctx = dict(fid=q["questionFrontendId"], title=q["title"],
               url=f"https://leetcode.com/problems/{q['titleSlug']}/")
    header = {"py": PY_HEADER, "cpp": CPP_HEADER, "ts": TS_HEADER}[lang].format(**ctx)
    defs, rest = split_definitions(code, lang)
    if lang == "py":
        rest = fill_python_bodies(rest)
        defs = fill_python_bodies(defs) if defs else defs
    parts = [header]
    if defs:
        parts.append(f"{LOCAL[lang]}\n{defs}\n")
    parts.append(f"{SUBMIT[lang]}\n{rest.rstrip()}\n")
    return "\n".join(parts)


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def problem_md(q: dict, group: str) -> str:
    tags = ", ".join(t["name"] for t in q["topicTags"])
    url = f"https://leetcode.com/problems/{q['titleSlug']}/"
    md = [f"# {q['questionFrontendId']}. {q['title']}\n",
          f"**Difficulty:** {q['difficulty']} · **Group:** {group} · **Tags:** {tags}  ",
          f"**Link:** <{url}>\n", html_to_md(q["content"])]
    if q.get("hints"):
        md.append("\n<details><summary>Hints</summary>\n")
        for i, h in enumerate(q["hints"], 1):
            md.append(f"{i}. {html_to_md(h).strip()}")
        md.append("\n</details>\n")
    return "\n".join(md)


def main() -> None:
    refresh = "--refresh" in sys.argv
    plan = cached("_plan", lambda: gql(PLAN_QUERY, {"slug": PLAN}), refresh)["studyPlanV2Detail"]
    index = []
    total = sum(len(g["questions"]) for g in plan["planSubGroups"])
    n = 0
    for gi, group in enumerate(plan["planSubGroups"], 1):
        gdir = f"{gi:02d}-{slugify(group['name'])}"
        for item in group["questions"]:
            n += 1
            slug = item["titleSlug"]
            q = cached(slug, lambda: gql(QUESTION_QUERY, {"s": slug}), refresh)["question"]
            print(f"[{n:3d}/{total}] {q['questionFrontendId']:>4}. {q['title']}")
            pdir = OUT / gdir / f"{int(q['questionFrontendId']):04d}-{slug}"
            pdir.mkdir(parents=True, exist_ok=True)
            (pdir / "problem.md").write_text(problem_md(q, group["name"]), encoding="utf-8")

            snippets = {s["langSlug"]: s["code"] for s in q["codeSnippets"]}
            templates = {}
            for lang_slug, ext in LANGS.items():
                content = build_solution(q, ext, snippets[lang_slug])
                templates[ext] = hashlib.sha1(content.encode()).hexdigest()
                f = pdir / f"solution.{ext}"
                if not f.exists():
                    f.write_text(content, encoding="utf-8", newline="\n")

            index.append({
                "order": n,
                "id": q["questionFrontendId"],
                "title": q["title"],
                "slug": slug,
                "difficulty": q["difficulty"],
                "group": group["name"],
                "dir": pdir.relative_to(ROOT).as_posix(),
                "metaData": json.loads(q["metaData"]),
                "exampleTestcases": q["exampleTestcaseList"],
                "templateSha1": templates,
            })
    (OUT / "problems.json").write_text(
        json.dumps({"plan": plan["name"], "problems": index}, ensure_ascii=False, indent=1),
        encoding="utf-8", newline="\n")
    print(f"done: {len(index)} problems -> {OUT}")


if __name__ == "__main__":
    main()
