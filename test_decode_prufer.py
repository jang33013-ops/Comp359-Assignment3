# tis a test code for the decode_pufer 
# to check if ecerythinh woorks corecttly 

from decode_prufer import decode_prufer
tests = [
    # (code, expected_edges, description)
    ([1, 1],       [(1, 2), (1, 3), (1, 4)],               "Star centred at 1, n=4"),
    ([2, 3],       [(1, 2), (2, 3), (3, 4)],               "Path 1-2-3-4, n=4"),
    ([1, 1, 3],    [(1, 2), (1, 4), (1, 3), (3, 5)],       "Mixed tree, n=5"),
    ([2, 3, 4],    [(1, 2), (2, 3), (3, 4), (4, 5)],       "Path 1-2-3-4-5, n=5"),
    ([3, 3, 3, 3], [(1, 3), (2, 3), (3, 4), (3, 5), (3, 6)], "Star centred at 3, n=6"),
    ([2],          [(1, 2), (2, 3)],                        "Minimal tree, n=3"),
    ([2, 4, 2, 4], [(1, 2), (2, 4), (2, 5), (3, 4), (4, 6)], "Mixed tree, n=6"),
]
def run_tests():
    passed = 0
    failed = 0
    print("=" * 60)
    print("RUNNING TESTS  —  decode_prufer()")
    print("=" * 60)
    for i, (code, expected, desc) in enumerate(tests, 1):
        result = decode_prufer(code)
        ok = sorted(result) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        print(f"Test {i:2d} [{status}]  {desc}")
        print(f"         code={code}  →  {result}")
        if not ok:
            print(f"         Expected : {sorted(expected)}")
            print(f"         Got      : {sorted(result)}")
    print("-" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests.")
    print()
    print("Error-handling tests:")  #  test if we get an error 

    try:
        decode_prufer([])
        print("  Empty code          — FAIL (should have raised ValueError)")
    except ValueError as e:
        print(f"  Empty code          — PASS  ({e})")

    try:
        decode_prufer([5, 5])                                                  # n=4, label 5 out of range
        print("  Out-of-range label  — FAIL (should have raised ValueError)")
    except ValueError as e:
        print(f"  Out-of-range label  — PASS  ({e})")
        


if __name__ == "__main__":
    run_tests()
