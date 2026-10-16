# LeetCode practice repo

- `top150/<NN-group>/<NNNN-slug>/`: one folder per Top Interview 150 problem, with `problem.md` (statement, gitignored) and `solution.py` / `solution.cpp` / `solution.ts`.
- Each solution file has a local-only header (imports, `ListNode`/`TreeNode` definitions); the user submits only the part below `---- submit below this line ----`.
- `top150/problems.json`: index (id, slug, group, metaData, example inputs, template hashes).
- `tools/fetch_top150.py`: re-downloads statements/templates (never overwrites solutions). `tools/progress.py`: rebuilds the README progress table.
- Old solutions from before Top 150 sit in the repo root; leave them alone.
- The user writes solutions in Python, C++ and TypeScript. When they say they finished a problem or ask to check, follow the `check` skill (`.claude/skills/check/SKILL.md`): run the examples in a temp dir, report failures by example number, then commit and push on success. Don't add test files to the repo.
- Talk to the user in Chinese.
