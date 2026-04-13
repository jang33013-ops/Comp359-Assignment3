# COMP359 — Assignment 3: Plan of Work

## Task Board

### Gavin: Cayley's Formula and Labeled Tree Theory

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Research Cayley's formula (n^(n−2)) |
| | | Study connection between labeled trees and Prüfer codes |
| | | Prepare theory write-up |
| | | Build example table for n = 1 to 7 |
| | Prepare presentation slide|  |

---

###  Jang: Unlabeled Trees and Formula Comparison

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Research unlabeled tree counts (OEIS A000055) |
| | | Explain why no simple closed formula exists for unlabeled trees |
| | | Implement comparison.py |
| | | Build labeled vs unlabeled comparison table |
| |Prepare presentation slide |  |

---

### Dhananjay: Prüfer Code Decoding and Tree Reconstruction

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Study Prüfer decoding algorithm (MAT344 Lecture 13) |
| | | Implement decode_prufer(code) |
| | | Implement decode_prufer_verbose() for step-by-step tracing |
| | | Write test cases in test_decode_prufer.py |
| | | Debug failing tests (Test 3 and Test 7) |
| | | Write DEBUGGING.md |
| |Prepare presentation slide |  |
---

### Kartik: Prüfer Code Encoding and One-to-One Correspondence

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Study Prüfer encoding algorithm |
| | | Implement encode_prufer(edges, n) |
| | | Verify encode → decode gives back original tree |
| | | Write test cases in test_encode_prufer.py |
| | | Prepare examples showing both directions (tree→code, code→tree) |
| |Prepare presentation slide |  |
---

### Mayank: Tree Generation and Filtering

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Study itertools.product for Prüfer sequence generation |
| | | Implement get_max_degree(edges, n) |
| | | Implement generate_trees(n, max_degree, stop_at) |
| | | Add stop-at-100 rule |
| | | Write test cases in test_generate_trees.py |
| | | Verify n=7 with max degree 3 produces 100 accepted trees |
| |Prepare presentation slide |  |
---

### Gavin & Simran: Visualization, Colours, and Final Integration

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Set up NetworkX and matplotlib |
| | | Take accepted trees from Member 5 |
| | | Replace numeric labels with colours |
| | | Draw all trees for n=7 with max degree 3 |
| | | Save final images |
| | | Combine all members' work into final submission |
| | | Review README and repo for consistency |
| |Prepare presentation slide |  |
---

## Overall Timeline

| Task | Owner | Status |
|------|-------|--------|
| Set up shared GitHub repo | All | Done |
| Cayley's formula write-up | Gavin | Done |
| Unlabeled trees comparison | Jang | Done |
| decode_prufer() implementation | Dhananjay | Done |
| decode_prufer() tests + debugging | Dhananjay | Done |
| encode_prufer() implementation | Kartik | Done |
| generate_trees() implementation | Mayank | Done |
| generate_trees() tests | Mayank | Done |
| Tree visualization images | Gavin & Simran | Done |
| README.md | All | Done |
| PLAN.md | All | Done |
| Final review and submission | All | Done |

Member 5 depends on Member 3's `decode_prufer()`.
Member 6 depends on Member 5's `generate_trees()`.
All other members can work independently.
