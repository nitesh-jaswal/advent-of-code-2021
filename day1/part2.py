with open("./input.txt", 'r') as infile:
    cnt = 0
    window = []
    for i in range(0,4):
        window.append(int(infile.readline()))
    for i, line in enumerate(infile):
        cnt += 1 if sum(window[1:4]) > sum(window[0:3]) else 0        
        window.pop(0)
        window.append(int(line))
    cnt += 1 if sum(window[1:4]) > sum(window[0:3]) else 0
    print(cnt)


