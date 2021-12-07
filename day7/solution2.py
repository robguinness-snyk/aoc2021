import os
import sys

def calc_fuel(steps):
    r = range(1, steps + 1)
    return sum(r)


def calc_fuel_from_positions(pos1, pos2):
    return calc_fuel(abs(pos1 - pos2))


test_data = [(16, 5, 66), (1, 5, 10), (2, 5, 6), (0, 5, 15)]

for t in test_data:
    actual = calc_fuel_from_positions(t[0], t[1])
    assert actual == t[2], f"expected {t[2]}, got {actual}"

with open(os.path.join('.', 'day7', 'input'), 'r') as fp:
    content = fp.readline()

positions = list(int(c) for c in content.split(','))
max_position = max(positions)

test_solutions = range(0, max_position)
min_solution = sys.maxsize

fuel = 0
for t in test_solutions:
    for p in positions:
        steps = abs(p - t)
        fuel += calc_fuel(steps)
    if fuel < min_solution:
        print(
            f"Solution {t} uses fuel {fuel}, which is better than "
            f"{min_solution}."
        )
        min_solution = fuel
        solution = t
        fuel = 0
print(f"The solution is {min_solution}!")


