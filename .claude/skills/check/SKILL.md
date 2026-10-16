---
name: check
description: Check the user's LeetCode Top 150 solutions against the problem's examples, report any failing example, and if everything passes commit and push to GitHub. Use when the user says "检查", "check", "/check", "我写完了", or names a problem number they finished.
---

# Check & commit a Top 150 solution

The user writes solutions; you verify them. **Never add test files, harnesses or test cases to the repo.** All throwaway code goes in the scratchpad / a temp dir.

## 1. Find what to check
- If the user gave a number (e.g. `88`) or slug: look it up in `top150/problems.json` (`id` / `slug` → `dir`).
- Otherwise run `git status --porcelain top150/` and check every problem dir with modified `solution.*` files.
- In each dir, only check languages whose file differs from the template (`python tools/progress.py` logic: sha1 vs `templateSha1`). Skip untouched languages silently.

## 2. Verify each language
Read `problem.md` (statement, examples with expected output, constraints) and the solution file. `problems.json` has `metaData` (function name, param/return types, or class design info) and `exampleTestcases` (raw example inputs).

For every example in `problem.md`, actually run the code — don't just eyeball it:
- **Python**: `python -I` a temp script that `exec`s / imports the solution file and calls it.
- **C++**: temp `.cpp` that `#include`s the solution file and a `main`, `g++ -std=c++17 -O2`.
- **TypeScript**: temp `.ts` with the solution code (drop the `export {};` line) plus calls, run with `node --experimental-strip-types --no-warnings`.
- Convert `ListNode` / `TreeNode` / `Node` from LeetCode's array notation; for design problems replay the operations/argument lists and compare the output list.
- In-place problems (`void` return, e.g. 88, 189, 48): compare the mutated argument as described in the statement. For "any order" / "any valid answer" outputs, compare accordingly.

Then also review the code against the constraints: obvious edge cases the examples miss (empty input, single element, overflow, duplicates) and time complexity that would TLE. Mention these as warnings, separate from example results.

## 3. Report (in Chinese, concise)
Per language: ✅ all examples pass, or ❌ `Example k`: input, expected, actual (and compile/runtime error message if any). Do not rewrite the user's solution unless they ask; a hint about the bug is fine.

## 4. Commit & push (only when every checked language passes)
```
python tools/progress.py
git add <problem dir>/solution.* README.md
git commit -m "Solve <id>. <Title> (<langs>)"
git push
```
`<langs>` = the passing languages, e.g. `Python, C++`. If something failed, don't commit; tell the user what to fix. If the user explicitly asks to commit anyway, commit only the passing languages.
