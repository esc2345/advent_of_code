# https://adventofcode.com/2020/day/2

import re

def part1(fname):
    valid = 0
    with open(fname) as f:
        for line in f:
            m = re.search('(\d+)-(\d+) ([a-z]): (.+)', line)
            if m is None:
                continue
            i, j, letter, pwd = m.groups()
            if int(i) <= pwd.count(letter) <= int(j):
                valid += 1
    return valid

print(part1("2020-02_input.txt"))

def part2(fname):
    valid = 0
    with open(fname) as f:
        for line in f:
            m = re.search('(\d+)-(\d+) ([a-z]): (.+)', line)
            if m is None:
                continue
            i, j, letter, pwd = m.groups()
            a, b = int(i) - 1, int(j) - 1
            if (pwd[a] == letter) != (pwd[b] == letter):
                valid += 1
    return valid

print(part2("2020-02_input.txt"))