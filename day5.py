s = open("inputs/day5_input.txt", "r").read()


def bin_recur(s, l, u, direction):
    assert direction in ['row', 'col']
    lower_half = 'F' if direction == 'row' else 'L'
    if u == l:
        return u
    elif s[0] == lower_half:
        new_u = u - (u - l)//2 - 1
        return bin_recur(s[1:], l, new_u, direction)
    else:
        new_l = l + (u - l)//2 + 1
        return bin_recur(s[1:], new_l, u, direction)


m = [8 * bin_recur(x[:7], 0, 127, 'row') + bin_recur(x[7:], 0, 7, 'col') for x in s.split()]
ans1 = max(m)
ans2 = [x for x in range(min(m), max(m)+1) if x not in m][0]

print(f"The answer for Part 1 is: {ans1}")
print(f"The answer for Part 2 is: {ans2}")
