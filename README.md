# COMP359 — Assignment 3: Labeled Trees and Prüfer Sequences

## Overview

This assignment explores the theory and computation of labeled and unlabeled trees on n vertices. Using Prüfer sequences as the central tool, we count, encode, decode, generate, and visualize labeled trees — connecting the combinatorial theory behind Cayley's formula to working Python implementations.

The three core results this assignment builds on:

- The number of labeled trees on n vertices is **n^(n−2)** — Cayley's formula
- Every labeled tree corresponds to exactly one Prüfer sequence of length n−2, giving a bijection that proves Cayley's formula
- Unlabeled trees are counted up to isomorphism — there is no simple closed formula like the labeled case

---

## Group Members

| Member | Name | GitHub | Responsibility |
|--------|------|--------|----------------|
| Member 1 | Gavin Mcnaughton | alashir | Cayley's formula and labeled tree theory write-up |
| Member 2 | *(fill in)* | *(fill in)* | Unlabeled trees and formula comparison |
| Member 3 | *(fill in)* | *(fill in)* | Prüfer code decoding and tree reconstruction |
| Member 4 | *(fill in)* | *(fill in)* | Prüfer code encoding and one-to-one correspondence |
| Member 5 | *(fill in)* | *(fill in)* | Tree generation and filtering |
| Member 6 | *(fill in)* | *(fill in)* | Visualization, colours, and final integration |

---

## Repository Structure

```
.
├── README.md                   ← this file (includes debugging log)
├── PLAN.md                     ← Kanban task board
|__ Theory Write-up             - Member 1: Cayley’s Formula
|
├── comparison.py               ← Member 2: labeled vs unlabeled comparison
│
├── decode_prufer.py            ← Member 3: Prüfer decoding implementation
├── test_decode_prufer.py       ← Member 3: test cases for decoding
│
├── encode_prufer.py            ← Member 4: Prüfer encoding implementation
├── test_encode_prufer.py       ← Member 4: test cases for encoding
│
├── generate_trees.py           ← Member 5: tree generation and filtering
├── test_generate_trees.py      ← Member 5: test cases for generation
│
└── visualize_trees.py          ← Member 6: drawing and image output
```

---

## How to Run

### Requirements

```bash
pip install networkx matplotlib
```

No other external dependencies — `itertools` is part of the Python standard library.

### Member 2 — Labeled vs Unlabeled Comparison

```bash
python comparison.py
```

Prints a table comparing labeled tree counts (Cayley's formula) against unlabeled tree counts for n = 1 to 7.

### Member 3 — Decode a Prüfer Code

```bash
python decode_prufer.py       # step-by-step verbose examples
python test_decode_prufer.py  # 7 tests + 2 error-handling tests
```

```python
from decode_prufer import decode_prufer
decode_prufer([1, 1, 3])
# → [(1, 2), (1, 4), (1, 3), (3, 5)]
```

### Member 4 — Encode a Tree into a Prüfer Code

```bash
python encode_prufer.py       # runs examples
python test_encode_prufer.py  # runs all tests
```

Encoding then decoding gives back the original tree, verifying the bijection.

### Member 5 — Generate All Labeled Trees

```bash
python generate_trees.py       # generates n=7 trees with max degree 3
python test_generate_trees.py  # 18 tests
```

```python
from generate_trees import generate_trees
accepted, stopped_early, total_checked = generate_trees(7, max_degree=3, stop_at=100)
# → 100 trees, stopped_early=True, total_checked=191
```

### Member 6 — Visualize the Trees

```bash
python visualize_trees.py
```

Draws all accepted trees for n=7 with max degree 3, using colours instead of numeric labels, and saves the images.

---

## Key Results

### Labeled vs Unlabeled Tree Counts

| n | Labeled (n^(n−2)) | Unlabeled |
|---|-------------------|-----------|
| 1 | 1 | 1 |
| 2 | 1 | 1 |
| 3 | 3 | 1 |
| 4 | 16 | 2 |
| 5 | 125 | 3 |
| 6 | 1,296 | 6 |
| 7 | 823,543 | 11 |

The labeled count grows extremely fast because vertex labels matter — swapping two labels produces a different tree. The unlabeled count grows much slower since only the shape matters.

### n=7 Generation Results

For n=7 with max degree ≤ 3, the generator checked **191 Prüfer sequences** before reaching **100 accepted trees** and stopping early.

---

## How the Algorithms Work

### Prüfer Decoding Algorithm 

Given a Prüfer sequence of length n−2 with labels 1..n:

1. Build the set of all available labels {1, 2, ..., n}
2. Repeat n−2 times:
   - Find the smallest label **not** in the remaining code — this is a leaf
   - Connect the leaf to the first element of the code
   - Remove the leaf from available; remove the first element from the code
3. Connect the final two remaining labels as the last edge

**Example** — decoding `[1, 1, 3]` on 5 vertices:

| Step | Remaining code | Available | Leaf | Edge added |
|------|---------------|-----------|------|------------|
| 1 | [1, 1, 3] | [1,2,3,4,5] | 2 | (1, 2) |
| 2 | [1, 3] | [1,3,4,5] | 4 | (1, 4) |
| 3 | [3] | [1,3,5] | 1 | (1, 3) |
| Final | — | [3,5] | — | (3, 5) |

Result: `[(1, 2), (1, 4), (1, 3), (3, 5)]`

### Tree Generation and Filtering 

it uses `itertools.product` to generate every possible Prüfer sequence of length n−2 over labels 1..n. Each sequence is decoded using `decode_prufer()`, then filtered by checking the maximum degree of any vertex. Generation stops once 100 trees have been accepted.

---

## Testing and Debugging Log

### Member 3 — Prüfer Decoding

**Test results:** 7 tests + 2 error-handling tests — all passing.

The first run of the test suite produced **2 failures**:

```
Test  3 [FAIL]  Mixed tree, n=5
         Expected : [(1, 2), (1, 3), (3, 4), (3, 5)]
         Got      : [(1, 2), (1, 4), (1, 3), (3, 5)]

Test  7 [FAIL]  Mixed tree, n=6
         Expected : [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)]
         Got      : [(1, 2), (2, 4), (2, 5), (3, 4), (4, 6)]

Results: 5 passed, 2 failed out of 7 tests.
```

**Investigation:** `decode_prufer_verbose()` was used to trace through both failing codes step by step. For code `[1, 1, 3]` at step 2, the remaining code is `[1, 3]` and the available set is `[1, 3, 4, 5]`. The smallest label not in the code is `4` — not `3`, because `3` still appears in the remaining code. The algorithm was producing the correct output all along.

**Root cause:** The expected values written manually in the test file were wrong. The edge order had been guessed without fully tracing the algorithm.

**Fix:** Updated the two incorrect expected values in `test_decode_prufer.py`:

```python
# Test 3 — before (wrong)
([1, 1, 3], [(1, 2), (1, 3), (3, 5), (3, 4)])

# Test 3 — after (correct)
([1, 1, 3], [(1, 2), (1, 4), (1, 3), (3, 5)])
```

**After fix:**

```
Results: 7 passed, 0 failed out of 7 tests.
Error-handling tests:
  Empty code          — PASS
  Out-of-range label  — PASS
```

**Key takeaway:** The `decode_prufer()` algorithm was correct from the start. Using `decode_prufer_verbose()` to print each step made it straightforward to verify what the correct output should be, rather than guessing expected values manually.

###  Tree Generation

**Test results:** 18 tests — all passing on first run. Tests cover `get_max_degree()` and `generate_trees()` across n=2 through n=7, including edge cases (n=1 error, max_degree=1, stop_at=3).

---

## File Dependencies

```
decode_prufer.py
        ↑
generate_trees.py       encode_prufer.py
        ↑
visualize_trees.py
```


---

## References

1. Cayley, A. (1889). A theorem on trees. *Quarterly Journal of Mathematics*, 23, 376–378.
2. Prüfer, H. (1918). Neuer Beweis eines Satzes über Permutationen. *Archiv der Mathematik und Physik*, 27, 142–144.
3. OEIS Foundation. (2024). A000055 — Number of trees with n unlabeled nodes. *The On-Line Encyclopedia of Integer Sequences*. https://oeis.org/A000055
4. Balázs, E. (2019). *MAT344 Lecture 13: Prüfer sequences and Cayley's formula*. University of Toronto. https://www.math.toronto.edu/balazse/2019_Summer_MAT344/Lec_13.pdf
5. UBC Mathematics. *Prüfer sequences and Cayley's theorem* [Course handout]. University of British Columbia.
6. Borcherds, R. (2021). *Graph Theory 12: Cayley's Tree Theorem* [Video]. YouTube. https://www.youtube.com/watch?v=Wi8IvnlMNxs
7. Python Software Foundation. (2024). *itertools — Functions creating iterators for efficient looping*. Python 3 Documentation. https://docs.python.org/3/library/itertools.html
8. NetworkX Developers. (2024). *NetworkX documentation*. https://networkx.org/documentation/stable/
9. Anthropic. (2024). *Claude AI* [AI assistant]. https://www.anthropic.com

---


