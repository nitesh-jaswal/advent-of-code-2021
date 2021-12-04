def part1():
    line_cnt = 1
    with open("input.txt", 'r') as infile:
        line = infile.readline().rstrip()
        col_num = [[int(i)] for i in line]
        for line in infile:
            line_cnt += 1
            line = line.rstrip()
            for i in range(0, len(line)):
                col_num[i] += [int(line[i])] 
    freq_num = [str(int(sum(col)>=(line_cnt//2))) for col in col_num]
    l_freq_num = ['0' if i == '1' else '1' for i in freq_num]
    gamma = int(''.join(freq_num), 2)
    epsilon = int(''.join(l_freq_num), 2)
    print(gamma*epsilon)

def part2():
    line_cnt = 1
    bit_len = None
    with open("input.txt", 'r') as infile:
        line = infile.readline().rstrip()
        bit_len = len(line)
        col_num = [[int(i)] for i in line]
        for line in infile:
            line_cnt += 1
            line = line.rstrip()
            for i in range(0, len(line)):
                col_num[i] += [int(line[i])] 
       
    # O2
    filter_num = [[i, 1] for i in range(line_cnt)]    
    for i in range(bit_len):
        s = [col_num[i][j[0]] if j[1] == 1 else None for j in filter_num ]
        filtered_s = [k for k in s if k is not None]
        filtered_freq_num = int(sum(filtered_s)>=(len(filtered_s)/2))
        # print(filtered_s)
        filter_num = [[index, int(digit == filtered_freq_num)] for index, digit in enumerate(s)]
        only_ones = [j[0]+1 for j in filter_num if j[1] == 1]
        # print(only_ones)
        if len(only_ones) == 1:
            # print(i)
            break
    [_index] = [j[0] for j in filter_num if j[1] == 1]
    # print(_index)
    o2gen = int(''.join([str(col_num[i][_index]) for i in range(bit_len)]), 2)
    print(f"O2: {o2gen}")

    # CO2
    filter_num = [[i, 1] for i in range(line_cnt)]
    for i in range(bit_len):
        s = [col_num[i][j[0]] if j[1] == 1 else None for j in filter_num ]
        filtered_s = [k for k in s if k is not None]
        filtered_freq_num = int(sum(filtered_s)<(len(filtered_s)/2))
        # print(filtered_s)
        filter_num = [[index, int(digit == filtered_freq_num)] for index, digit in enumerate(s)]
        only_ones = [j[0]+1 for j in filter_num if j[1] == 1]
        # print(only_ones)
        if len(only_ones) == 1:
            # print(i)
            break
    [_index] = [j[0] for j in filter_num if j[1] == 1]
    # print(_index)
    co2gen = int(''.join([str(col_num[i][_index]) for i in range(bit_len)]), 2)
    print(f"CO2: {co2gen}")
    print(co2gen*o2gen)

print("************PART 1************")
part1()
print("************PART 2************")
part2()