# COMP 359 Assignment 3: Labeled Trees and Prüfer Sequences

## Group Members

Name | GitHub | Responsibility |
|------|--------|----------------|
| Gavin McNaughton | alashir | Cayley's formula, Prufer Codes, Tree Visualization |
| Jang Toor| jang33013-ops | Unlabeled trees and formula comparison |
| Dhananjay Sharma | Dhananjay-FK | Prüfer code decoding and tree reconstruction |
| Kartik Bhanot | kartikb11 | Prüfer code encoding and one-to-one correspondence |
| Mayank | Mayanksci-18 | Tree generation and filtering |
| Simran Bola | simran12m | Visualization, colours, and final integration |

---

## How to Run

### Requirements

```bash
pip install networkx matplotlib
```

### Project files and their purpose

```bash
python comparison.py            # labeled vs unlabeled table
python decode_prufer.py         # step-by-step decoding examples
python test_decode_prufer.py    # 7 tests + 2 error-handling tests
python encode_pruferM4.py       # encoding examples
python test_encode_prufer.py    # encoding tests
python generate_trees.py        # generate n=7 trees
python test_generate_trees.py   # 18 tests
python tree_visualization.py    # draw one combined image in results/
```

### Generating the final result

```bash
python generate_trees.py
python tree_visualization.py
```
---

## Gavin McNaughton — Cayley's Formula, Connection to Prufer Codes

### Cayley’s Formula

Cayley’s Formula states that the number of labeled trees on n vertices = n^(n-2) (Cayley, 1889). Using this formula, then, we can surmise that for any integer n ≥ 1, the total number of distinct labeled trees will be T(n) = n^(n-2). This means that the number of distinct labeled trees grows exponentially with n. For example: at n = 3 there are 3 trees, and at n = 5 there are 125 trees.

### Connection to Prüfer Codes

The main idea behind Cayley’s Formula is its connection to Prüfer codes (Prüfer, 1918). A Prüfer code is a sequence of length n - 2 that uniquely represents a labeled tree on n vertices. This indicates to us that each entry in the sequence must be an integer between 1 and n, with the sequence itself being composed of exactly n - 2 elements. Interestingly, there is a one-to-one connection between the number of labeled trees on n vertices and the number of Prüfer codes of length n - 2. This means that every labeled tree corresponds to exactly one Prüfer code, and vice versa.

### Why Cayley’s Formula Works

Since each position in a Prüfer code can be any of the possible n labels, and there are n - 2 positions, the total number of possible Prüfer codes is n × n × … × n = n^(n−2). Due to this one-to-one correspondence, this number also correlates to the amount of labeled trees.

---

## Jang Toor — Labeled vs Unlabeled Trees

A labeled tree refers to a tree in which each vertex has been labeled to distinguish it from others (1, 2, 3, 4, etc). In this case, trees with the same shape will be counted as different if the labels are arranged differently. To count all of these unique trees, we must apply Cayley’s formula.

In the case of unlabeled trees, structure is the only thing that matters. Two trees are considered the same if a one-to-one correspondence exists between their vertices, assuming adjacency is preserved. This is called graph isomorphism. This makes unlabeled trees much harder to count. There is no simple closed formula equivalent to n^(n−2). The counts must be looked up from sequences like OEIS A000055 (OEIS, 2024). Below is a table (n = 1 to 7) for both labeled and unlabeled:

| n | Labeled (n^(n−2)) | Unlabeled |
|---|-------------------|-----------|
| 1 | 1                 | 1         |
| 2 | 1                 | 1         |
| 3 | 3                 | 1         |
| 4 | 16                | 2         |
| 5 | 125               | 3         |
| 6 | 1,296             | 6         |
| 7 | 16,807            | 11        |

---

##  Dhananjay Sharma — Decoding a Prüfer Sequence

Decoding a Prüfer sequence means reconstructing the original labeled tree, producing an edge list like `[(1, 2), (1, 3), (3, 4)]`.

### Why the algorithm works
Every leaf (a vertex with degree 1) in a labeled tree must be the smallest label that does not appear in the remaining Prüfer sequence at any step. This is because a vertex appears in the Prüfer sequence exactly once for each neighbour it has except its last one — so a label missing from the sequence must currently be a leaf. We repeatedly peel off the smallest such leaf, connect it to the next element in the code, and continue until two vertices remain.

### The algorithm step by step

1. Compute n = len(code) + 2. Build available = {1, 2, ..., n}
2. Repeat n−2 times:
   - Find the smallest label in available that does NOT appear in the remaining code → this is the leaf
   - Add edge (leaf, code[0]) to the tree
   - Remove leaf from available; remove code[0] from the front of the code
3. Connect the final two labels left in available as the last edge

### Example: decoding `[1, 1, 3]` on 5 vertices

| Step | Remaining code | Available | Leaf | Edge added |
|------|---------------|-----------|------|------------|
| 1 | [1, 1, 3] | {1,2,3,4,5} | 2 | (1, 2) |
| 2 | [1, 3] | {1,3,4,5} | 4 | (1, 4) |
| 3 | [3] | {1,3,5} | 1 | (1, 3) |
| Final | — | {3,5} | — | (3, 5) |

Result: `[(1, 2), (1, 4), (1, 3), (3, 5)]`

At step 2, the leaf is 4 — not 3 — because 3 still appears in the remaining code `[1, 3]`, meaning vertex 3 still has more connections to make.

### Implementation

```python
from decode_prufer import decode_prufer
decode_prufer([1, 1, 3])
# → [(1, 2), (1, 4), (1, 3), (3, 5)]
```

A second function `decode_prufer_verbose(code)` prints every step of the algorithm, which was used during debugging to verify correctness.

---

## Kartik Bhanot — Encoding a Tree into a Prüfer Sequence 

Encoding acts in the reverse direction; given a labeled tree as an edge list, produce its Prüfer sequence. The algorithm mirrors the decoding process: repeatedly finding the leaf with the smallest label, recording its neighbour, removing it, and repeating until two vertices remain.

In this part of the project, we proved that encoding -> decoding gives back the original tree. The opposite is true as well, returning the original code. This round-trip check confirms the bijection is working correctly in both directions, proving Cayley's formula; every sequence maps to exactly one tree and vice versa.

---

## Mayank — Generating All Labeled Trees

With decoding working, generating all labeled trees on n vertices was straightforward: produce every possible Prüfer sequence of length n−2 then decode each one. `itertools.product` was used to generate the sequences, which would then be decoded using Dhananjay's `decode_prufer()` function, before filtering out all trees including a vertex with degree > 3. In our case, generation stops as soon as 100 trees have been accepted.

### Why the filtering works
The maximum degree of a vertex equals the number of times its label appears in the Prüfer sequence plus one (for its last edge). So a vertex with degree 4 or more would appear at least 3 times in the code. Filtering by max degree simply checks this after decoding.

### Results for n=7

```
Prüfer sequences checked : 191
Trees accepted           : 100
Stopped early            : True
```

Only 191 of the 16,807 possible sequences needed to be checked before hitting 100 accepted trees.

### Usage

```python
from generate_trees import generate_trees
accepted, stopped_early, total_checked = generate_trees(7, max_degree=3, stop_at=100)
```

---

## Gavin McNaughton & Simran Bola — Visualization 

Numeric vertex labels were replaced with colours so the nodes could stay small enough to fit cleanly in a large image.

```python
COLORS = ["red", "blue", "green", "orange", "purple", "cyan", "magenta"]
NODE_COLOR_MAP = {i + 1: COLORS[i] for i in range(N_VERTICES)}
```

We then loaded all 100 graphs from `generate_trees.py` using `load_graphs()`, and combined them with `draw_combined_image()`. The two main libraries we used here were NetworkX and MatPlotLib. NetworkX was used to create graph objects, add edges, compute each layout, and draw each graph (NetworkX Development Team, n.d.). Matplotlib was used for subplot creation, titles/formatting, layout adjustments, and saving the final image (Matplotlib Development Team, n.d.). The final output was a single image file, shown below:

![Final Result](results/all_trees_n7_maxdeg3.png)
---

## Testing and Debugging

### Dhananjay — Prüfer Decoding Tests

Seven test cases were written covering stars, paths, mixed trees, and the minimal n=3 case. Two error-handling tests checked that invalid inputs (empty code, out-of-range label) raised `ValueError` correctly.

The first test run produced 2 failures:

```
Test  3 [FAIL]  Mixed tree, n=5
         Expected : [(1, 2), (1, 3), (3, 4), (3, 5)]
         Got      : [(1, 2), (1, 4), (1, 3), (3, 5)]

Test  7 [FAIL]  Mixed tree, n=6
         Expected : [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)]
         Got      : [(1, 2), (2, 4), (2, 5), (3, 4), (4, 6)]

Results: 5 passed, 2 failed out of 7 tests.
```

`decode_prufer_verbose()` was used to trace both failing codes step by step. The trace confirmed the algorithm was producing the correct output. The mistake was in the manually written expected values in the test file. The expected edges had been guessed without fully tracing the algorithm.

After fixing the two expected values:

```
Results: 7 passed, 0 failed out of 7 tests.
Error-handling tests:
  Empty code          — PASS
  Out-of-range label  — PASS
```

**Key takeaway:** The `decode_prufer()` algorithm was correct from the start. Using `decode_prufer_verbose()` to print each step made it straightforward to verify what the correct output should be, rather than guessing expected values manually.

### Mayank — Generation Tests

18 tests were written covering `get_max_degree()` and `generate_trees()` across multiple values of n, including edge cases like n=2, max_degree=1, and stop_at=3. All 18 passed on the first run.

---

## References

1. Cayley, A. (1889). *A theorem on trees*. Quarterly Journal of Mathematics, 23, 376–378.
2. Prüfer, H. (1918). *Neuer Beweis eines Satzes über Permutationen*. Archiv der Mathematik und Physik, 27, 142–144.
3. OEIS Foundation. (2024). *A000055 — Number of trees with n unlabeled nodes*. The On-Line Encyclopedia of Integer Sequences. https://oeis.org/A000055
4. Python Software Foundation. (2024). *itertools — Functions creating iterators for efficient looping*. Python 3 Documentation. https://docs.python.org/3/library/itertools.html
5. NetworkX Development Team. (n.d.). *Tutorial*. https://networkx.org/documentation/stable/tutorial.html
6. Matplotlib Development Team. (n.d.). *Tutorials*. https://matplotlib.org/stable/tutorials/index.html
7. Anthropic. (2024). *Claude AI* [AI assistant]. https://www.anthropic.com
