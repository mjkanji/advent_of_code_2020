from collections import OrderedDict, defaultdict

s = open("inputs/day8_input.txt", "r").read()

### Part 1
def preprocess(s):
    s = s.split("\n")
    s = [x + " --{}".format(i) for i, x in enumerate(s)]
    return s


def execution_loop(s):
    d = defaultdict(int)
    count = 0
    i = 0
    while i < len(s):
        cmd, arg, idx = s[i].split()
        idx = idx[2:]
        if idx in d.keys():
            # print(count)
            return (count, False)
        else:
            d[idx] += 1
        
        if cmd == 'nop':
            count = count
        elif cmd == 'acc':
            count = count + int(arg[1:]) if arg[0] == '+' else count - int(arg[1:])
        elif cmd == 'jmp':
            i = i + int(arg[1:]) if arg[0] == "+" else i - int(arg[1:])
            continue
        i += 1
    return count
s = preprocess(s)
ans1 = execution_loop(s)[0]
print("The answer to Part 1 is: {}".format(ans1))


### Part 2
loops = []
for i, line in enumerate(s):
    cmd, arg, idx = line.split()
    if cmd == 'nop':
        s_copy = s.copy()
        s_copy[i] = " ".join(['jmp', arg, idx])   
        loops.append(s_copy) 
    elif cmd == 'jmp':
        s_copy = s.copy()
        s_copy[i] = " ".join(['nop', arg, idx])
        loops.append(s_copy)

ans2 = [x for x in [execution_loop(loop) for loop in loops] if type(x) != tuple][0]
print("The answer to Part 2 is: {}".format(ans2))
