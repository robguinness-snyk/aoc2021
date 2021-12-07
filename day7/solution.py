import os
import sys

with open(os.path.join('.', 'day7', 'input'), 'r') as fp:
    content = fp.readline()

positions = list(int(c) for c in content.split(','))
max_position = max(positions)

test_solutions = range(0, max_position)
min_solution = sys.maxsize

fuel = 0
for t in test_solutions:
    for p in positions:
        fuel += abs(p - t)
    if fuel < min_solution:
        print(
            f"Solution {t} uses fuel {fuel}, which is better than "
            f"{min_solution}."
        )
        min_solution = fuel
        solution = t
        fuel = 0
print(f"The solution is {min_solution}!")
