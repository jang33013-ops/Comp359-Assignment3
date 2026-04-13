from generate_trees import generate_trees, get_max_degree

def test_max_degree():                                        # Tests for get_max_degree()
    print("=" * 60)
    print("TESTING get_max_degree()")
    print("=" * 60)
    tests = [                                                     # (edges, n, expected_max_degree, description)
        ([(1, 2), (1, 3), (1, 4)], 4, 3, "Star at 1 — degree 3"),
        ([(1, 2), (2, 3), (3, 4)], 4, 2, "Path 1-2-3-4 — max degree 2"),
        ([(1, 2)],                 2, 1, "Single edge n=2 — degree 1"),
        ([(1, 2), (1, 3), (1, 4), (1, 5)], 5, 4, "Star degree 4 — should fail filter"),
    ]
    passed = 0
    failed = 0
    for edges, n, expected, desc in tests:
        result = get_max_degree(edges, n)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok: passed += 1
        else:  failed += 1
        print(f"  [{status}]  {desc}")
        if not ok:
            print(f"         Expected {expected}, got {result}")
    print(f"\n  {passed} passed, {failed} failed\n")

def test_generate_trees():                                        # Tests for generate_trees()
    print("=" * 60)
    print("TESTING generate_trees()")
    print("=" * 60)
    passed = 0
    failed = 0
    def check(label, condition, detail=""):
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  [PASS]  {label}")
        else:
            failed += 1
            print(f"  [FAIL]  {label}")
            if detail:
                print(f"          {detail}")
    accepted, stopped, checked = generate_trees(2)                           #  n=2: single edge, no Prüfer code 
    check("n=2 returns exactly 1 tree",   len(accepted) == 1)
    check("n=2 tree is [(1,2)]",          accepted[0] == [(1, 2)])
    check("n=2 stopped_early is False",   stopped == False)
    accepted, stopped, checked = generate_trees(3)                            #  n=3: 3 trees total, all have max degree <= 3 
    check("n=3 accepts all 3 trees",      len(accepted) == 3)
    check("n=3 stopped_early is False",   stopped == False)
    check("n=3 checked 3 sequences",      checked == 3)
    accepted, stopped, checked = generate_trees(4)                             #  n=4: 4^2=16 Prüfer sequences, all trees have max degree <= 3 
    check("n=4 accepts all 16 trees",     len(accepted) == 16)
    check("n=4 stopped_early is False",   stopped == False)
    check("n=4 all max degree <= 3",      all(get_max_degree(e, 4) <= 3 for e in accepted))
    accepted, stopped, checked = generate_trees(4, max_degree=1)                       #  no tree on 4 vertices has max degree 1 
    check("n=4 max_degree=1 → 0 accepted", len(accepted) == 0)
    accepted, stopped, checked = generate_trees(4, max_degree=2)                       #  n=4, max_degree=2: only paths allowed 
    check("n=4 max_degree=2 all have degree<=2",
          all(get_max_degree(e, 4) <= 2 for e in accepted))
    accepted, stopped, checked = generate_trees(4, stop_at=3)                          #  stop_at=3 on n=4 
    check("stop_at=3 returns exactly 3",  len(accepted) == 3)
    check("stop_at=3 stopped_early True", stopped == True)
    accepted, stopped, checked = generate_trees(7, max_degree=3, stop_at=100)          #  n=7 for 100 trees
    check("n=7 accepts exactly 100 trees",  len(accepted) == 100)
    check("n=7 stopped_early is True",      stopped == True)
    check("n=7 all max degree <= 3",        all(get_max_degree(e, 7) <= 3 for e in accepted))
    check("n=7 all trees have 6 edges",     all(len(e) == 6 for e in accepted))
    
    try:                                                                              # error handling
        generate_trees(1)
        print("  [FAIL]  n=1 should raise ValueError")
        failed += 1
    except ValueError:
        print("  [PASS]  n=1 raises ValueError")
        passed += 1

    print(f"\n  {passed} passed, {failed} failed\n")
