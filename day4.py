import numpy as np
import pandas as pd
import re

s = open("inputs/day4_input.txt", "r").read()
list_of_dicts = [dict([y.split(":") for y in x.split()]) for x in s.split("\n\n")]
df = pd.DataFrame(list_of_dicts)
df.drop(columns=['cid'], inplace=True)
df.dropna(how="any", inplace=True)
ans_1 = len(df)
print("Part A's answer is:", ans_1)


def checker(func, x):
    try:
        return func(x)
    except:
        return False


df.byr = df.byr.apply(lambda x: checker(lambda x:len(x) == 4 and int(x) >= 1920 and int(x) <= 2002, x))
df.iyr = df.iyr.apply(lambda x: checker(lambda x:len(x) == 4 and int(x) >= 2010 and int(x) <= 2020, x))
df.eyr = df.eyr.apply(lambda x: checker(lambda x:len(x) == 4 and int(x) >= 2020 and int(x) <= 2030, x))


def hgt_check(h):
    units = h[-2:]
    num = h[:-2]
    if units == 'cm':
        return int(num) >= 150 and int(num) <= 193
    elif units == 'in':
        return int(num) >= 59 and int(num) <= 76
    else:
        return False

df.hgt = df.hgt.apply(lambda x: checker(hgt_check, x))
df.hcl = df.hcl.apply(lambda x: True if re.search("^#[\da-f]{6}$", x) else False)
df.ecl = df.ecl.apply(lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
df.pid = df.pid.apply(lambda x: True if re.search('^\d{9}$', x) else False)
ans_2 = df.apply(lambda x:x.all(), axis=1).sum()
print("Part B's answer is:", ans_2)
