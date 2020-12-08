s = open("inputs/day6_input.txt", "r").read()

# Part 1
ans1 = sum([len(set(x.replace("\n", ""))) for x in s.split("\n\n")])
print(f"The solution to Part 1 is: {ans1}")

# Part 2
l2 = [[set(m) for m in x.split()] for x in s.split("\n\n")]
ans2 = sum([len(set.intersection(*x)) for x in l2])
print(f"The solution to Part 2 is: {ans2}")

import functools as f

f.map()