# https://adventofcode.com/2020/day/1

# input - 200 lines

def part1(fname):
    difference = {}
    with open(fname) as f:
        for line in f:
            x = int(line)
            d = 2020 - x
            if x in difference:
                return x * difference[x]
            else:
                difference[d] = x

print(part1("2020-01_input.txt"))

def part2(fname):
    inputs = [int(x) for x in open(fname)]
    difference = {}
    for i in inputs:
        for j in inputs:
            if i != j:
                d = 2020 - i - j
                difference[d] = (i, j)
        if i in difference:
            return i * difference[i][0] * difference[i][1]

print(part2("2020-01_input.txt"))
