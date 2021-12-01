# Functional approach to part2
from functools import reduce
from itertools import tee
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

with open("./input.txt", 'r') as infile:
    input_num = [int(line) for line in infile]
win_size = 3
cnt = sum(map(lambda x: x[1] > x[0], pairwise(map(sum, map(lambda x: input_num[x:x+3], range(0, len(input_num) - win_size + 1))))))
print(cnt)
