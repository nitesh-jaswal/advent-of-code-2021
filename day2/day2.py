def part1():
    pos = dict(forward=0, down=0, up=0)
    with open("input.txt", 'r') as infile:
        for line in infile:
            s = line.split(' ')
            pos[s[0]] += int(s[1])
    ans = pos['forward'] * (pos['down'] - pos['up'])
    print(ans)

def part2():
    pos = dict(forward=0, down=0, up=0, depth=0)
    with open("input.txt", 'r') as infile:
        for line in infile:
            s = line.split(' ')
            pos[s[0]] += int(s[1])
            if s[0] == "forward":
                pos['depth'] += int(s[1]) * (pos['down'] - pos['up'])
    ans = pos['forward'] * pos['depth']
    print(ans)

def part2_func():
    ...

part1()
part2()