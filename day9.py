from itertools import combinations, accumulate
import operator

s = open("inputs/day9_input.txt", "r").read()
s = s.split("\n")
s = [int(x) for x in s]
n = 25
preamb = s[:n]
inputs = s[n:]


def is_valid(inp, preamb):
    return inp in [sum(x) for x in combinations(preamb, 2)]


def part1(inputs, preamb):
    assert len(inputs) != 0, 'inputs cannot be an empty list!'

    inp = inputs[0]
    if not is_valid(inp, preamb):
        return inp
    else:
        preamb.pop(0)
        preamb.append(inp)
        return part1(inputs[1:], preamb)


def part2(s, invalid):
    sums = list(accumulate(s, operator.add))
    if invalid in sums:
        idx = sums.index(invalid) + 1
        return min(s[:idx]) + max(s[:idx])
    else:
        return part2(s[1:], invalid)


ans1 = part1(inputs, preamb.copy())
print("The solution to Part 1 is:", ans1)

ans2 = part2(s, ans1)
print("The solution to Part 2 is:", ans2)