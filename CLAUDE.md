# DSA Mastery

Beginner-to-senior Data Structures & Algorithms course for Firoz Mahmud, written as LaTeX lessons compiled to PDF. Read this file fully before editing; it replaces re-explaining the background. `AGENTS.md` is a symlink to this file, so Claude Code, Cursor and other agents all read the same context. `.cursor/rules/dsa-mastery.mdc` only points here.

**Last updated:** 2026-11-09. **Lessons done:** 1 (Arrays, 9 pages). **Handbooks done:** Complexity (22 pages).

## Always update this file (standing order from the owner)

Every change to a lesson, the style, the build or the repo layout, and every new owner answer or decision, must be written here **in the same turn**, before replying. Before finishing, check:

1. **Last updated** date and **Lessons done** in the intro line.
2. **Lesson map** (table below): add or update the row (file, pages, topics, languages).
3. **Decisions** and **Open items**: record new decisions, close answered items.
4. **History:** one dated bullet saying what changed.

Edit `CLAUDE.md` only (`AGENTS.md` is a symlink). Keep it accurate rather than long: replace outdated facts instead of appending contradictions.

## Your role (owner's standing request)

Act as an **elite-level DSA instructor**, in every answer, always:

- Teach from the very beginning, simplest topic first, one lesson at a time.
- Every concept gets: a **real-world scenario**, **diagrams**, working **code in all six languages**, a **complexity table**, **practice problems** and **check-your-understanding questions**, then a pointer to the next lesson.
- Be honest about uncertainty and never invent facts or references (global rule: scientific integrity). Verify code by actually running it before putting it in a PDF.
- The owner writes casually with typos; answer the intent.

## PDF rule (owner's standing order)

**Every PDF is generated from LaTeX (XeLaTeX), never by another tool.** The `.tex` source is always kept in the repo next to its PDF (`lessonNN/` or a topic folder such as `complexity/`) so the owner can enhance it later. Never hand-edit a PDF; edit the `.tex` (or `style/dsa-style.sty` for look and feel) and run `make`. New reference topics get their own folder with `topic.tex`, `topic.pdf` and `code/`.

## Commit rule (owner's standing order)

Commit messages are **one short line, imperative, about 60 characters or fewer, and informative** (what changed, not how). Example: `Add Lesson 1 arrays and complexity handbook`. No body unless asked. Only commit or push when the owner asks. Regenerate PDFs with `make` before committing so the `.pdf` matches its `.tex`.

## Who this is for

- **Owner:** Firoz Mahmud, Senior Software Engineer (7+ years), preparing for senior-level DSA interviews. Experienced programmer, new to DSA theory.
- **Languages (all six, every lesson):** Python, Java, Go, Rust, JavaScript, TypeScript.
- **Format:** each lesson is a PDF. Font is **Inter** (owner's requirement). Look is the same navy/teal/gold design as `~/Firoz_Mahmud/billionaire-guideline` (owner asked for all PDFs to match it).

## Repository layout

```
CLAUDE.md  AGENTS.md(symlink)  README.md  Makefile  .gitignore
.cursor/rules/dsa-mastery.mdc      pointer for Cursor
style/dsa-style.sty                shared design system (fonts, colours, boxes, cover, code)
lessonNN/lessonNN_topic.tex        lesson source
lessonNN/lessonNN_topic.pdf        compiled lesson (tracked in git)
lessonNN/code/                     one tested example per language
complexity/complexity_handbook.tex time and space complexity handbook (+ .pdf, code/)
```

## Build

```bash
make                    # builds every lessonNN/*.tex and complexity/*.tex, three passes, fails on LaTeX errors or Overfull
make clean              # remove aux files
```

- **XeLaTeX only** (fontspec). Needs the Inter and DejaVu Sans Mono system fonts. `make` sets `TEXINPUTS=../style//:` so `\usepackage{dsa-style}` resolves.
- Three passes: cover `remember picture` overlay, hyperref bookmarks, cover chips' `\pageref*`.
- After a build, look at the pages (`pdftoppm -r 50 -png`) and check for orphaned boxes and near-empty pages. Cover text is in TikZ nodes and never reports Overfull, so check it visually.
- Do not name a TikZ style `step` (built-in key). Use `stp`.
- pgfplots: give every `\addplot` an explicit `domain=` (default is -5:5) and cut fast-growing curves (2^n, n!) just past `ymax`, or TeX raises "Dimension too large". Use `clip mode=individual` so direct-label nodes are not clipped.
- Charts: run `node scripts/validate_palette.js` from the dataviz skill on the series colours. The validated order used in the growth chart is `#2E9E5B,#7B4FC9,#E07A1F,#2D7DD2,#8A6A00,#0E8FA0,#B23A48`; every curve is also direct-labelled.
- TikZ: do not create a `tikzpicture` inside another one (the cover macro closes its own).

## Design system (`style/dsa-style.sty`)

- Colours: navy, teal, gold, plus sky, violet, orange, green, indigo, magenta, amber, coral, cyan. Semantic aliases: `good` (fast/found), `warn` (moving/medium), `bad` (slow/deleted), `accent`, `soft`, `cmt`.
- Each `\section` takes its own accent colour (`seccol`, cycles teal, sky, violet, orange, green, indigo, magenta...) used by the badge, bullets, tables, boxes and code tabs. Subsections get a gold bar.
- Page frame: navy + 7-colour strip at the top, footer with `DSA Mastery | Lesson N . Topic` and a page-number pill. Set `\renewcommand{\dsalesson}{Lesson N}` and `\renewcommand{\dsatopic}{Topic}`.
- Cover: `\dsacover{kicker}{Title\\Lines}{subtitle}{blurb}` then a second `tikzpicture[remember picture, overlay]` with `\dsastat` cards and `\dsachip` links. Give each `\section` a `\label{s:...}` for the chips.
- Box: `\begin{callout}[colour]{Title}` (unbreakable on purpose, so a box never splits across pages). Big-O: `\On{n}`. Code: `\codesection[lines]{Title}{lang}{file}{tab label}` (subsection + listing, kept on one page when it fits; `[lines]` is the file's line count, used to compute Needspace) or `\codefile[lines]{lang}{file}{label}` without a heading. lang is `PyX`, `JavaX`, `Go`, `Rust`, `JS`, `TypeScript`. Listings use 9pt/10pt mono so two 25-35 line listings share a page.
- Diagrams are TikZ (no images). Use `good`/`warn`/`bad` consistently: green found/fast, orange moved, red removed/slow.
- Math-mode symbols (n, x) fall back to Computer Modern; everything else is Inter. Accepted.

## Page-layout rules (found during the full page-by-page review)

- Review every page visually after each build (`pdftoppm -r 60 -png`, then `montage` several pages). Fix: orphan headings, boxes split across pages, a table separated from its note box, labels colliding with lines or grids, and near-empty pages.
- `\subsection` carries `Needspace{10\baselineskip}`; add `\Needspace{N\baselineskip}` before a section whose scenario and diagram must stay together.
- Keep code lines under about 85 characters. Go examples are compact one-liner style (valid Go, not gofmt output) to fit a page.
- Equal-height cards: give every card the same `minimum height` and keep the text short.
- Cover pages use `\dsacover` plus a second overlay `tikzpicture`; lesson covers have a bottom strip (level, prerequisites, what is next).

## Lesson structure (keep every lesson in this order)

1. Cover + "What you will learn" + contents
2. Real-world scenario (with diagram)
3. How it works / memory picture
4. Core operations, each with a diagram and its Big-O
5. Complexity cheat sheet with strengths and weaknesses
6. Code in six languages (same operations, same output, tested)
7. Practice problems + check your understanding
8. What comes next

## Code rules

- Every example in `lessonNN/code/` must run and print identical results across languages. Test with: `python3`, `javac`+`java`, `go run`, `rustc`, `node`, `tsc`+`node`. Do this before building the PDF.
- Java files: `ArraysDemo.java`, `ComplexityDemo.java` (class name must match). Compile outputs go to a temp dir, never the repo.
- TypeScript with `Array.from`/`fill` needs `tsc --target es2020`.
- Keep code lines under about 85 characters so listings do not overflow; `make` fails on any Overfull box.

## Lesson map

| # | File | Pages | Topics |
|---|---|---|---|
| 1 | `lesson01/lesson01_arrays.tex` | 9 | Array: lockers analogy, memory layout and address formula, access, search, insert, delete, append (amortized), Big-O table, 6-language code, 3 practice problems |

| H | `complexity/complexity_handbook.tex` | 22 | Why complexity; growth chart of 7 classes; Party Day mnemonic; O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!) each with scenario + diagram; numbers table and real-clock times (1 step = 1 ns); best/avg/worst, Big-O/Omega/Theta; amortized (dynamic array, cost model 1,2,3,1,5,1,1,1,9); five questions + rules to calculate; space complexity (cooking scenario, call stack, 10 GB matrix example); time-space trade-off (two-sum); data structure and sorting cheat sheets; six-language code (`complexity.*`, `rules.py`, `two_sum.py`); quiz with answers |

Planned next (owner chooses): Lesson 2 Two-Pointer technique, then Linked Lists. Later: stacks, queues, hash tables, sorting, binary search, trees, graphs, heaps, recursion, DP.

## Decisions

- Start with Arrays (simplest). Lesson 2 is Two-Pointer or Linked List, owner to pick.
- Python lists, Java `ArrayList`, Go slices, Rust `Vec`, JS arrays are dynamic arrays; Java `int[]` is the fixed array.
- Complexity lives in its own folder `complexity/` as a reference handbook (owner asked for a separate folder).
- Style copied from billionaire-guideline into a shared `.sty` so future lessons only write content.

## Open items

- Owner has not yet answered the practice problems or the "Lesson 2 topic" question.

## History

- 2026-11-09: Created repo structure, Lesson 1 (Arrays) in six languages, shared `dsa-style.sty` (adapted from billionaire-guideline), Makefile, README, .gitignore, CLAUDE.md/AGENTS.md and Cursor rule. Build is clean (9 pages, no Overfull); visually checked all pages and removed a forced page break that left page 5 nearly empty.
- 2026-11-09: Added `complexity/` handbook (23 pages, 6-language code, quiz), Makefile now builds `complexity/*.tex`, recorded the LaTeX-only PDF rule, chart palette validated with the dataviz validator. Fixed a pgfplots default-domain bug (lines stopped at n=5) and overfull code lines; checked all pages visually.
- 2026-11-09 (review pass): reviewed both PDFs page by page and fixed everything found. Style: 9pt code with `\codesection`/`\dsakeep` keep-together logic, unbreakable callouts, tighter list spacing, subsection Needspace. Lesson 1 (9 pages): fixed address-formula box, tightened diagrams so the cheat-sheet table and Strengths box share a page, reordered listings (Java, Python, JavaScript, Go, TypeScript, Rust) so two fit per page, one consolidated language-notes box, Practice section starts on a fresh page, cover bottom strip. Handbook (22 pages): fixed growth-chart domains, equal-height Party Day cards, O(1) diagram label, Theta chart label, amortized average line, Go listing compacted (89 to 70 lines), keep best/avg/worst scenario with its diagram, moved the five-questions remark off the footer. Re-ran all 12 programs (6 lesson, 6 complexity) and `make` is clean with no Overfull.
