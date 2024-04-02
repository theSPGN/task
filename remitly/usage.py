from solution import Solution

test_files = [
    "example_1.json",
    "example_2.json",
    "example_3.json",
    "example_4.json",
    "example_5.jso",
]
for test in test_files:
    solution = Solution().more_then_one_asterisk(test)
    print(solution, "\n")
