# DSA Mastery

Notes, patterns and solved problems for senior-level DSA interviews, taught from the very beginning as illustrated PDF lessons. Every lesson has a real-world scenario, diagrams, a complexity table, practice problems, and tested code in **Python, Java, Go, Rust, JavaScript and TypeScript**.

## Lessons

| # | Lesson | PDF | Code |
|---|---|---|---|
| 1 | The Array | [lesson01_arrays.pdf](lesson01/lesson01_arrays.pdf) | [code](lesson01/code) |

### Reference handbooks

| Handbook | PDF | Code |
|---|---|---|
| Complexity Handbook: every time and space complexity class, best/worst/amortized, with scenarios and diagrams | [complexity_handbook.pdf](complexity/complexity_handbook.pdf) | [code](complexity/code) |

Coming next: Two-Pointer technique, Linked Lists, then stacks, queues, hash tables, sorting, binary search, trees, graphs, heaps, recursion and dynamic programming.

## Build the PDFs

Every PDF is generated from LaTeX source (`.tex`) kept in the repo, so any page can be edited and rebuilt. Requires XeLaTeX plus the Inter and DejaVu Sans Mono fonts.

```bash
make          # build all lessons
make clean    # remove LaTeX build files
```

## Layout

```
style/dsa-style.sty        shared design (Inter font, navy/teal/gold)
lessonNN/*.tex, *.pdf      lesson source and compiled PDF
lessonNN/code/             runnable example in each of the six languages
complexity/                Complexity Handbook (tex, pdf, code/)
CLAUDE.md, AGENTS.md       AI context for Claude Code and Cursor (AGENTS.md is a symlink)
```

## Run the Lesson 1 examples

```bash
python3 lesson01/code/arrays.py
javac -d /tmp/out lesson01/code/ArraysDemo.java && java -cp /tmp/out ArraysDemo
go run lesson01/code/arrays.go
rustc -o /tmp/arrays lesson01/code/arrays.rs && /tmp/arrays
node lesson01/code/arrays.js
tsc --outDir /tmp/out lesson01/code/arrays.ts && node /tmp/out/arrays.js
```

The complexity examples run the same way (`complexity/code/`); compile its TypeScript with `tsc --target es2020 --outDir /tmp/out complexity/code/complexity.ts`.
