"""Regenerate the root README.md progress table for Top Interview 150.

A solution counts as done once its file differs from the generated template
(compared via templateSha1 in top150/problems.json).

Usage:  python tools/progress.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = [("py", "Python"), ("cpp", "C++"), ("ts", "TypeScript")]


def is_done(path: Path, template_sha1: str) -> bool:
    if not path.exists():
        return False
    content = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(content).hexdigest() != template_sha1


def main() -> None:
    index = json.loads((ROOT / "top150" / "problems.json").read_text(encoding="utf-8"))
    problems = index["problems"]
    counts = {ext: 0 for ext, _ in LANGS}
    solved_any = 0
    rows: dict[str, list[str]] = {}
    for p in problems:
        cells = []
        any_done = False
        for ext, _ in LANGS:
            if is_done(ROOT / p["dir"] / f"solution.{ext}", p["templateSha1"][ext]):
                counts[ext] += 1
                any_done = True
                cells.append(f"[✅]({p['dir']}/solution.{ext})")
            else:
                cells.append("")
        solved_any += any_done
        link = f"[{p['title']}](https://leetcode.com/problems/{p['slug']}/)"
        rows.setdefault(p["group"], []).append(
            f"| {p['id']} | {link} | {p['difficulty']} | " + " | ".join(cells) + " |")

    total = len(problems)
    out = [
        "# LeetCode",
        "",
        f"## {index['plan']}",
        "",
        f"Solved **{solved_any} / {total}** · "
        + " · ".join(f"{name} {counts[ext]}" for ext, name in LANGS),
        "",
        "Solutions live in [`top150/`](top150/). Older solutions are in the repo root.",
        "",
    ]
    for group, group_rows in rows.items():
        out += [f"### {group}", "",
                "| # | Problem | Difficulty | " + " | ".join(n for _, n in LANGS) + " |",
                "|---:|---|---|:---:|:---:|:---:|", *group_rows, ""]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"README.md updated: {solved_any}/{total} solved")


if __name__ == "__main__":
    main()
