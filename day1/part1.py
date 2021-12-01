with open("./input.txt", 'r') as infile:
    cnt = 0
    prev = int(infile.readline())
    for line in infile:
        cnt += 1 if int(line) > prev else 0
        prev = int(line)
    print(cnt)

