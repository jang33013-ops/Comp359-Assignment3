# COMP359 — Assignment 3: Labeled Trees and Prüfer Sequences

## Overview

This assignment explores the theory and computation of labeled and unlabeled trees. We use Prüfer sequences to count, encode, decode, generate, and visualize labeled trees on n vertices, connecting the combinatorial theory of Cayley's formula to practical implementations.

The central results are:
- The number of labeled trees on n vertices is **n^(n−2)** (Cayley's formula)
- Every labeled tree corresponds to exactly one Prüfer sequence of length n−2
- There is no simple closed formula for unlabeled trees (counted up to isomorphism)

---

## Group Members

| Member | Name | GitHub | Responsibility |
|--------|------|--------|----------------|
| Member 1 | *(fill in)* | *(fill in)* | Cayley's formula and labeled tree theory |
| Member 2 | *(fill in)* | *(fill in)* | Unlabeled trees and formula comparison |
| Member 3 | *(fill in)* | *(fill in)* | Prüfer code decoding and tree reconstruction |
| Member 4 | *(fill in)* | *(fill in)* | Prüfer code encoding and one-to-one correspondence |
| Member 5 | *(fill in)* | *(fill in)* | Tree generation and filtering |
| Member 6 | *(fill in)* | *(fill in)* | Visualization, colours, and final integration |

---

## Repository Structure

```
.
├── README.md                   ← this file
├── PLAN.md                     ← Kanban task board (plan of work)
├── DEBUGGING.md                ← debugging log for Member 3
│
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

### Member 2 — Labeled vs Unlabeled Comparison

```bash
python comparison.py
```

Prints a table comparing labeled tree counts (Cayley's formula) against unlabeled tree counts for n = 1 to 7.

### Member 3 — Decode a Prüfer Code

```bash
python decode_prufer.py       # runs step-by-step examples
python test_decode_prufer.py  # runs all 7 tests + error handling
```

`decode_prufer(code)` takes a Prüfer sequence and returns an edge list. Example:

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

`encode_prufer(edges, n)` takes an edge list and returns the Prüfer sequence. Encoding then decoding gives back the original tree.

### Member 5 — Generate All Labeled Trees

```bash
python generate_trees.py       # generates n=7 trees with max degree 3
python test_generate_trees.py  # runs all 18 tests
```

`generate_trees(n, max_degree=3, stop_at=100)` generates all Prüfer sequences for n vertices, decodes each into a tree, filters by maximum degree, and stops at 100 accepted trees. Example:

```python
from generate_trees import generate_trees
accepted, stopped_early, total_checked = generate_trees(7, max_degree=3, stop_at=100)
# → 100 trees, stopped_early=True, total_checked=191
```

### Member 6 — Visualize the Trees

```bash
python visualize_trees.py
```

Takes the accepted trees from Member 5 for n=7 with max degree 3, draws each tree with coloured vertices instead of numeric labels, and saves the images.

---

## Key Results

| n | Labeled trees (n^(n−2)) | Unlabeled trees |
|---|------------------------|-----------------|
| 1 | 1 | 1 |
| 2 | 1 | 1 |
| 3 | 3 | 1 |
| 4 | 16 | 2 |
| 5 | 125 | 3 |
| 6 | 1,296 | 6 |
| 7 | 823,543 | 11 |

For n=7 with max degree ≤ 3, generation stops at **100 accepted trees** after checking 191 Prüfer sequences.

---

## How the Prüfer Decoding Algorithm Works

Given a Prüfer sequence of length n−2 with labels 1..n:

1. Build the set of all available labels {1, 2, ..., n}
2. Repeat n−2 times:
   - Find the smallest label **not** in the remaining code — this is a leaf
   - Connect the leaf to the first element of the code
   - Remove the leaf from available; remove the first element from the code
3. Connect the final two remaining labels as the last edge

**Example** — code `[1, 1, 3]` on 5 vertices:

| Step | Remaining code | Leaf | Edge added |
|------|---------------|------|------------|
| 1 | [1, 1, 3] | 2 | (1, 2) |
| 2 | [1, 3] | 4 | (1, 4) |
| 3 | [3] | 1 | (1, 3) |
| Final | — | — | (3, 5) |

Result: `[(1, 2), (1, 4), (1, 3), (3, 5)]`

---

## File Dependencies

```
decode_prufer.py
    ↑
generate_trees.py     encode_prufer.py
    ↑
visualize_trees.py
```

All files must be in the same directory when running.

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
9. Anthropic. (2024). *Claude AI* [AI assistant used for code development and documentation]. https://www.anthropic.com

---

