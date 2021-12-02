 def part1():   
    with open("./input.txt", 'r') as infile:
        cnt = 0
        prev = int(infile.readline())
        for line in infile:
            cnt += 1 if int(line) > prev else 0
            prev = int(line)
        print(cnt)

def part2():
    with open("./input.txt", 'r') as infile:
        cnt = 0
        window = [int(infile.readline()) for i in range(0,4)]
        for i, line in enumerate(infile):
            cnt += 1 if sum(window[1:4]) > sum(window[0:3]) else 0        
            window.pop(0)
            window.append(int(line))
        cnt += 1 if sum(window[1:4]) > sum(window[0:3]) else 0
        print(cnt)

def part2_func():
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

part1()
part2()
part2_func()