# COMP359 — Assignment 3: Work Log

This file documents the **process** of building each part of the assignment: what was run, what came out, what went wrong, and how it was fixed. Screenshots are included as direct evidence of the terminal output at each stage.

---

## Jang — comparison.py (Labeled vs Unlabeled Trees)

### First Run: Bug Found

The first run produced incorrect output. The unlabeled column was printing text like `unlabeled =1` instead of just the number:

  ![01](bugs.jpg)

### Final Run: Correct Output

The table now prints correctly with clean integer values in both columns.

  ![02](correct_output.jpg)

---

## Dhananjay — decode_prufer.py (Prüfer Code Decoding)

### Verbose Step-by-Step Output

`decode_prufer_verbose()` was run on three example codes to verify the algorithm was working correctly before writing tests. The screenshot below shows the full trace for codes `[1, 1]`, `[2, 3]`, and `[1, 1, 3]`:

![Member 3 verbose trace](https://github.com/user-attachments/assets/94374044-5c27-462d-b0e4-0614bd831aaa)

Each step shows the remaining code, available labels, which leaf is picked, and which edge is added. This trace was later used to find the root cause of the test failures below.

### First Test Run: 2 Failures

```
============================================================
RUNNING TESTS  —  decode_prufer()
============================================================
Test  1 [PASS]  Star centred at 1, n=4
Test  2 [PASS]  Path 1-2-3-4, n=4
Test  3 [FAIL]  Mixed tree, n=5
         Expected : [(1, 2), (1, 3), (3, 4), (3, 5)]
         Got      : [(1, 2), (1, 4), (1, 3), (3, 5)]
Test  4 [PASS]  Path 1-2-3-4-5, n=5
Test  5 [PASS]  Star centred at 3, n=6
Test  6 [PASS]  Minimal tree, n=3
Test  7 [FAIL]  Mixed tree, n=6
         Expected : [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)]
         Got      : [(1, 2), (2, 4), (2, 5), (3, 4), (4, 6)]
------------------------------------------------------------
Results: 5 passed, 2 failed out of 7 tests.
```

### Investigation

The verbose trace above was used to trace `[1, 1, 3]` step by step. At step 2, the remaining code is `[1, 3]` and the available set is `[1, 3, 4, 5]`. The smallest label **not** in the code is `4` — not `3` — because `3` still appears in the remaining code. The algorithm was producing the correct output all along.

### Root Cause

The expected values written manually in the test file were wrong. The edge order had been guessed without fully tracing the algorithm first.

### Fix

```python
# Test 3 — before (wrong)
([1, 1, 3], [(1, 2), (1, 3), (3, 5), (3, 4)])

# Test 3 — after (correct)
([1, 1, 3], [(1, 2), (1, 4), (1, 3), (3, 5)])

# Test 7 — before (wrong)
([2, 4, 2, 4], [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)])

# Test 7 — after (correct)
([2, 4, 2, 4], [(1, 2), (2, 4), (2, 5), (3, 4), (4, 6)])
```

### Final Test Run: All Passing

![Member 3 all tests passing](https://github.com/user-attachments/assets/041d4c3d-1e70-4af0-a07d-5761753ae92c)

7 tests + 2 error-handling tests all passing. The algorithm was correct from the start — only the expected values in the test file needed fixing.

---

## Kartik — encode_pruferM4.py (Prüfer Code Encoding)

### Test Run reveals all tests passing on first attempt

Three trees were tested: two with known expected codes, one without. The screenshot below shows all three passing:

![Member 4 encode round-trip tests](https://github.com/user-attachments/assets/a556fd92-42b4-490a-952b-2b23da8de89b)

All three confirmed that `encode → decode` gives back the original tree exactly. The round-trip verification proves the bijection is working correctly in both directions. Every tree maps to a unique code and back.

---

## Mayank — generate_trees.py (Tree Generation and Filtering)

### Test Run: All 18 Passing First Time

![Member 5 all 18 tests passing](https://github.com/user-attachments/assets/4a459ef8-4916-4bde-b0a4-736db7a451c0)

4 tests for `get_max_degree()` and 14 tests for `generate_trees()` — all 18 passing on the first run. Tests covered n=2 through n=7, edge cases like max_degree=1, stop_at=3, and the n=1 ValueError.

### Main Case Output: n=7

```
n=7 | checked: 191 | accepted: 100 | stopped early: True

  Tree   1: [(1, 4), (1, 5), (1, 2), (2, 6), (2, 3), (3, 7)]
  Tree   2: [(1, 3), (1, 5), (1, 2), (2, 6), (2, 4), (4, 7)]
  Tree   3: [(1, 3), (1, 4), (1, 2), (2, 6), (2, 5), (5, 7)]
  ...
  Tree 100: [(1, 3), (1, 5), (1, 4), (4, 7), (2, 6), (2, 7)]

  [stopped after 100 accepted trees]
```

191 Prüfer sequences were checked out of 16,807 possible before hitting the 100-tree limit.

---

## Simran & Gavin — tree_visualization.py (Drawing Trees)

ABC

### Final Run Output

```
Accepted 100 trees saved to accepted_trees.json
Matplotlib is building the font cache; this may take a moment.
Loaded 100 trees from accepted_trees.json
Saved combined image: results\all_trees_n7_maxdeg3.png
```

100 trees successfully combined and stored in the results/ folder

---

## Summary

| Member | File | Tests | First Run | Bugs Found | Final Status |
|--------|------|-------|-----------|------------|--------------|
| 2 | comparison.py | manual | failed | 1 — unlabeled column formatting | Fixed ✓ |
| 3 | decode_prufer.py | 7 + 2 error | 5/7 passed | 2 — wrong expected values in tests | Fixed ✓ |
| 4 | encode_pruferM4.py | 3 round-trip | all passed | 0 | Passed first run ✓ |
| 5 | generate_trees.py | 18 | all passed | 0 | Passed first run ✓ |
| 6 | tree_visualization.py | manual | all passed | 0 | Passed first run ✓ |
