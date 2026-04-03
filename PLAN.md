# COMP359 — Assignment 3: Plan of Work

## Task Board

### Member 1 — Cayley's Formula and Labeled Tree Theory

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Research Cayley's formula (n^(n−2)) |
| | | Study connection between labeled trees and Prüfer codes |
| | | Prepare theory write-up |
| | | Build example table for n = 1 to 7 |
| | Prepare presentation slide|  |

---

### Member 2 — Unlabeled Trees and Formula Comparison

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Research unlabeled tree counts (OEIS A000055) |
| | | Explain why no simple closed formula exists for unlabeled trees |
| | | Implement comparison.py |
| | | Build labeled vs unlabeled comparison table |
| |Prepare presentation slide |  |

---

### Member 3 — Prüfer Code Decoding and Tree Reconstruction

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

### Member 4 — Prüfer Code Encoding and One-to-One Correspondence

| To Do | In Progress | Done |
|-------|-------------|------|
| | | Study Prüfer encoding algorithm |
| | | Implement encode_prufer(edges, n) |
| | | Verify encode → decode gives back original tree |
| | | Write test cases in test_encode_prufer.py |
| | | Prepare examples showing both directions (tree→code, code→tree) |
| |Prepare presentation slide |  |
---

### Member 5 — Tree Generation and Filtering

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

### Member 6 — Visualization, Colours, and Final Integration

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
| Cayley's formula write-up | Member 1 | Done |
| Unlabeled trees comparison | Member 2 | Done |
| decode_prufer() implementation | Member 3 | Done |
| decode_prufer() tests + debugging | Member 3 | Done |
| encode_prufer() implementation | Member 4 | Done |
| generate_trees() implementation | Member 5 | Done |
| generate_trees() tests | Member 5 | Done |
| Tree visualization images | Member 6 | Done |
| README.md | All | Done |
| PLAN.md | All | Done |
| Final review and submission | All | Done |

---

## Dependencies Between Members

```
Member 1 (theory)
    ↓
Member 2 (unlabeled comparison)     Member 3 (decode)
                                         ↓
                    Member 4 (encode) ←→ Member 5 (generate)
                                         ↓
                                    Member 6 (visualize)
```

Member 5 depends on Member 3's `decode_prufer()`.
Member 6 depends on Member 5's `generate_trees()`.
All other members can work independently.
