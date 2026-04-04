# COMP359 — Assignment 3: Labeled Trees and Prüfer Sequences

## What This Assignment Is About

A **tree** is a connected graph with no cycles. When we label the vertices with numbers 1 to n, two trees that look the same shape but have different numbers on their vertices count as different trees — these are called **labeled trees**. A natural question is: how many labeled trees exist on n vertices?

The answer is surprisingly clean: exactly **n^(n−2)**. This is Cayley's formula. For example, there are 3^1 = 3 labeled trees on 3 vertices, and 4^2 = 16 on 4 vertices. The formula works because of a beautiful one-to-one correspondence between labeled trees and **Prüfer sequences** — a compact numerical encoding of any tree. Our assignment is built around understanding this correspondence and implementing it in Python.

---

## Group Members

| Member | Name | GitHub | Responsibility |
|--------|------|--------|----------------|
| Member 1 | Gavin McNaughton | alashir | Cayley's formula and labeled tree theory write-up |
| Member 2 | *(fill in)* | *(fill in)* | Unlabeled trees and formula comparison |
| Member 3 | Mayank | Mayank_18 | Prüfer code decoding and tree reconstruction |
| Member 4 | Kartik Bhanot | kartikb11 | Prüfer code encoding and one-to-one correspondence |
| Member 5 | Mayank | Mayank_18 | Tree generation and filtering |
| Member 6 | Simran Bola | simran12m | Visualization, colours, and final integration |

---

## Repository Structure

```
.
├── README.md                   ← this file
├── PLAN.md                     ← Kanban task board
├── WORKLOG.md                  ← testing and debugging log with screenshots
├── Theory Write-up             ← Member 1: Cayley's Formula theory document
│
├── comparison.py               ← Member 2: labeled vs unlabeled comparison
│
├── decode_prufer.py            ← Member 3: Prüfer decoding implementation
├── test_decode_prufer.py       ← Member 3: test cases for decoding
│
├── encode_pruferM4.py          ← Member 4: Prüfer encoding implementation
├── test_encode_prufer.py       ← Member 4: test cases for encoding
│
├── generate_trees.py           ← Member 5: tree generation and filtering
├── test_generate_trees.py      ← Member 5: test cases for generation
│
├── tree_visualization.py       ← Member 6: drawing and image output
└── results/                    ← Member 6: saved PNG images of all 100 trees
    ├── tree_1.png
    ├── tree_2.png
    ├── ...
    └── tree_100.png
```

---

## How to Run

### Requirements

```bash
pip install networkx matplotlib
```

`itertools` is part of the Python standard library — no install needed.

All files must be in the same directory since `generate_trees.py` imports from `decode_prufer.py`.

### Running Each Part

```bash
python comparison.py            # Member 2: labeled vs unlabeled table
python decode_prufer.py         # Member 3: step-by-step decoding examples
python test_decode_prufer.py    # Member 3: 7 tests + 2 error-handling tests
python encode_pruferM4.py       # Member 4: encoding examples
python test_encode_prufer.py    # Member 4: encoding tests
python generate_trees.py        # Member 5: generate n=7 trees
python test_generate_trees.py   # Member 5: 18 tests
python tree_visualization.py    # Member 6: draw and save tree images to results/
```

---

## What We Did and Why

### Member 1 — Cayley's Formula 

The number of labeled trees on n vertices is n^(n−2). This is proven using the Prüfer sequence bijection: since every labeled tree maps to a unique sequence of length n−2 over labels 1..n, and there are n^(n−2) such sequences, there must be exactly n^(n−2) labeled trees. The bijection works in both directions — every sequence decodes to exactly one tree, and every tree encodes to exactly one sequence — which is what makes it a proof.

Member 1 prepared the full theory write-up (see `Theory Write-up` in the repo), built the example table for n = 1 to 7, and produced a presentation slide connecting the formula to the Prüfer correspondence.

---

### Member 2 — Labeled vs Unlabeled Trees

Labeled trees are easy to count because labels make trees distinguishable — rotating or reflecting a tree gives a different labeled tree if the vertex numbers change position. Unlabeled trees only care about shape, so trees that are mirror images or rotations of each other count as one.

This makes unlabeled trees much harder to count. There is no simple closed formula equivalent to n^(n−2). The counts must be looked up from sequences like OEIS A000055:

| n | Labeled (n^(n−2)) | Unlabeled |
|---|-------------------|-----------|
| 1 | 1 | 1 |
| 2 | 1 | 1 |
| 3 | 3 | 1 |
| 4 | 16 | 2 |
| 5 | 125 | 3 |
| 6 | 1,296 | 6 |
| 7 | 823,543 | 11 |

Notice how the labeled count explodes (823,543 for n=7) while the unlabeled count stays small (only 11 distinct shapes). Member 2 implemented `comparison.py` to print this table and explain why the gap exists.

---

### Member 3 — Decoding a Prüfer Sequence

A Prüfer sequence is a list of n−2 numbers, each between 1 and n. Decoding it means reconstructing the original labeled tree — producing an edge list like `[(1, 2), (1, 3), (3, 4)]`.

**Why the algorithm works:** every leaf (a vertex with degree 1) in a labeled tree must be the smallest label that does not appear in the remaining Prüfer sequence at any step. This is because a vertex appears in the Prüfer sequence exactly once for each neighbour it has except its last one — so a label missing from the sequence must currently be a leaf. We repeatedly peel off the smallest such leaf, connect it to the next element in the code, and continue until two vertices remain.

**The algorithm step by step:**

1. Compute n = len(code) + 2. Build available = {1, 2, ..., n}
2. Repeat n−2 times:
   - Find the smallest label in available that does NOT appear in the remaining code → this is the leaf
   - Add edge (leaf, code[0]) to the tree
   - Remove leaf from available; remove code[0] from the front of the code
3. Connect the final two labels left in available as the last edge

**Example — decoding `[1, 1, 3]` on 5 vertices:**

| Step | Remaining code | Available | Leaf | Edge added |
|------|---------------|-----------|------|------------|
| 1 | [1, 1, 3] | {1,2,3,4,5} | 2 | (1, 2) |
| 2 | [1, 3] | {1,3,4,5} | 4 | (1, 4) |
| 3 | [3] | {1,3,5} | 1 | (1, 3) |
| Final | — | {3,5} | — | (3, 5) |

Result: `[(1, 2), (1, 4), (1, 3), (3, 5)]`

At step 2, the leaf is 4 — not 3 — because 3 still appears in the remaining code `[1, 3]`, meaning vertex 3 still has more connections to make.

**Implementation:**

```python
from decode_prufer import decode_prufer
decode_prufer([1, 1, 3])
# → [(1, 2), (1, 4), (1, 3), (3, 5)]
```

A second function `decode_prufer_verbose(code)` prints every step of the algorithm, which was used during debugging to verify correctness.

---

### Member 4 — Encoding a Tree into a Prüfer Sequence 

Encoding is the reverse direction: given a labeled tree as an edge list, produce its Prüfer sequence. The algorithm mirrors the decoding process — repeatedly find the leaf with the smallest label, record its neighbour, remove it, and repeat until two vertices remain.

The important thing Member 4 verified is that **encoding then decoding gives back the original tree**, and **decoding then encoding gives back the original code**. This round-trip check confirms the bijection is working correctly in both directions, which is what proves Cayley's formula — every sequence maps to exactly one tree and vice versa.

---

### Member 5 — Generating All Labeled Trees

With decoding working, generating all labeled trees on n vertices is straightforward: produce every possible Prüfer sequence of length n−2 and decode each one. Since labels range from 1 to n and the sequence has length n−2, there are exactly n^(n−2) sequences — one per labeled tree.

Member 5 used `itertools.product` to generate every sequence, decoded each using Member 3's `decode_prufer()`, and filtered out any tree where a vertex has degree greater than 3. Generation stops as soon as 100 trees have been accepted.

**Why the filtering works:** the maximum degree of a vertex equals the number of times its label appears in the Prüfer sequence plus one (for its last edge). So a vertex with degree 4 or more would appear at least 3 times in the code. Filtering by max degree simply checks this after decoding.

**Results for n=7:**

```
Prüfer sequences checked : 191
Trees accepted           : 100
Stopped early            : True
```

Only 191 of the 823,543 possible sequences needed to be checked before hitting 100 accepted trees.

**Usage:**

```python
from generate_trees import generate_trees
accepted, stopped_early, total_checked = generate_trees(7, max_degree=3, stop_at=100)
```

---

### Member 6 — Visualization 

Member 6 takes the 100 accepted trees from Member 5 and draws each one using NetworkX and matplotlib. Numeric vertex labels are replaced with colours so the nodes can stay small enough to fit cleanly in the image. The final output is a set of saved image files showing all filtered trees for n=7 with max degree 3.

---

## Testing and Debugging

### Member 3 — Prüfer Decoding Tests

Seven test cases were written covering stars, paths, mixed trees, and the minimal n=3 case. Two error-handling tests check that invalid inputs (empty code, out-of-range label) raise `ValueError` correctly.

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

`decode_prufer_verbose()` was used to trace both failing codes step by step. The trace confirmed the algorithm was producing the correct output — the mistake was in the manually written expected values in the test file. The expected edges had been guessed without fully tracing the algorithm.

After fixing the two expected values:

```
Results: 7 passed, 0 failed out of 7 tests.
Error-handling tests:
  Empty code          — PASS
  Out-of-range label  — PASS
```

**Key takeaway:** The `decode_prufer()` algorithm was correct from the start. Using `decode_prufer_verbose()` to print each step made it straightforward to verify what the correct output should be, rather than guessing expected values manually.

### Member 5 — Generation Tests

18 tests were written covering `get_max_degree()` and `generate_trees()` across multiple values of n, including edge cases like n=2, max_degree=1, and stop_at=3. All 18 passed on the first run.

---

## File Dependencies

```
decode_prufer.py
        ↑
generate_trees.py       encode_pruferM4.py
        ↓
tree_visualization.py → results/
```

`generate_trees.py` imports `decode_prufer` from `decode_prufer.py`. Member 6's `tree_visualization.py` takes the accepted trees directly from Member 5 and saves all images to the `results/` folder. All other files are independent.

---

## References

1. Cayley, A. (1889). A theorem on trees. *Quarterly Journal of Mathematics*, 23, 376–378.
2. Prüfer, H. (1918). Neuer Beweis eines Satzes über Permutationen. *Archiv der Mathematik und Physik*, 27, 142–144.
3. OEIS Foundation. (2024). A000055 — Number of trees with n unlabeled nodes. *The On-Line Encyclopedia of Integer Sequences*. https://oeis.org/A000055
4. Balázs, E. (2019). *MAT344 Lecture 13: Prüfer sequences and Cayley's formula*. University of Toronto. https://www.math.toronto.edu/balazse/2019_Summer_MAT344/Lec_13.pdf
5. UBC Mathematics. *Prüfer sequences and Cayley's theorem* [Course handout]. University of British Columbia.
6. Borcherds, R. (2021). *Graph Theory 12: Cayley's Tree Theorem* [Video]. YouTube. https://www.youtube.com/watch?v=Wi8IvnlMNxs
7. TheTrevTutor. (2015). *Graph theory 12: Cayley's tree theorem* [Video]. YouTube. https://www.youtube.com/watch?v=Wi8IvnlMNxs
8. Last Moment Tuitions. (2020). *Prufer code generation for labelled trees* [Video]. YouTube. https://www.youtube.com/watch?v=ndqIVWV--yw
9. Dr. Trefor Bazett. (2020). *Cayley's formula and Prüfer sequences* [Video]. YouTube. https://www.youtube.com/watch?v=Ve447EOW8ww
10. Python Software Foundation. (2024). *itertools — Functions creating iterators for efficient looping*. Python 3 Documentation. https://docs.python.org/3/library/itertools.html
11. NetworkX Developers. (2024). *NetworkX documentation*. https://networkx.org/documentation/stable/
12. Anthropic. (2024). *Claude AI* [AI assistant]. https://www.anthropic.com

