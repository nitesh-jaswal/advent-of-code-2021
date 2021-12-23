from typing import List, Tuple
import numpy as np
# TODO: Explore if there is a linear algebraic method of solving this

def parse_input():
    with open("input.txt", 'r') as infile:
        input_coords = [[[int(xy) for xy in coord.strip().split(',')] for coord in line.split('->')] for line in infile]
        return(input_coords)

def check_horizontal_or_vertical(coord_pair: List[List[int]]) -> bool:
        return ((coord_pair[0][0] == coord_pair[1][0]) | (coord_pair[0][1] == coord_pair[1][1]))

def get_path(coord: List[List[int]]) -> List[Tuple[List[int], List[int]]]:
    start = coord[0]
    end = coord[1]
    segments = []
    # print(f"Start: {start}, End: {end}")
    while start[0] != end[0] or start[1] != end[1]:
        x_path = y_path = []
        y_diff = end[1]- start[1]
        x_diff = end[0]- start[0]
        y_diff_sign = np.sign(y_diff)
        x_diff_sign = np.sign(x_diff)
        # print(f"XDiff: {x_diff}, Y_Diff: {y_diff}")
        if x_diff == 0:
            x_path = [end[0]]
            y_path = [start[1] + (y_diff_sign * i) for i in range(abs(y_diff))]
            start[1] = start[1] + y_diff
        elif y_diff == 0:
            y_path = [end[1]]
            x_path = [start[0] + (x_diff_sign * i) for i in range(abs(x_diff))]
            start[0] = start[0] + x_diff
        else:
            if x_diff > 0 and y_diff > 0:
                range_iter = x_diff if x_diff < y_diff else y_diff
                x_path = [start[0] + i for i in range(range_iter)]
                y_path = [start[1] + i for i in range(range_iter)]
                start = [start[0] + range_iter, start[1] + range_iter]
            elif x_diff < 0 and y_diff > 0:
                range_iter = abs(x_diff) if abs(x_diff) < abs(y_diff) else abs(y_diff)
                x_path = [start[0] - i for i in range(range_iter)]
                y_path = [start[1] + i for i in range(range_iter)]
                start = [start[0] - range_iter, start[1] + range_iter]
            elif x_diff < 0 and y_diff < 0:
                range_iter = abs(x_diff) if abs(x_diff) < abs(y_diff) else abs(y_diff)
                x_path = [start[0] - i for i in range(range_iter)]
                y_path = [start[1] - i for i in range(range_iter)]
                start = [start[0] - range_iter, start[1] - range_iter]
            elif x_diff > 0 and y_diff < 0:
                range_iter = abs(x_diff) if abs(x_diff) < abs(y_diff) else abs(y_diff)
                x_path = [start[0] + i for i in range(range_iter)]
                y_path = [start[1] - i for i in range(range_iter)]
                start = [start[0] + range_iter, start[1] - range_iter]
        segments += [(x_path, y_path)]
    return(segments)

def part1():
    input_coords = [coord for coord in parse_input() if check_horizontal_or_vertical(coord)]
    grid_size = 1000
    grid = np.zeros(shape=(grid_size, grid_size))
    for coord in input_coords:
        for x_path, y_path in get_path(coord):
            grid[y_path, x_path] += 1
        grid[coord[1][1], coord[1][0]] += 1
    print(f"Grid: {np.sum(grid >= 2)}")    


def part2():
    input_coords = parse_input()
    grid_size = 1000
    grid = np.zeros(shape=(grid_size, grid_size))
    for coord in input_coords:
        for x_path, y_path in get_path(coord):
            grid[y_path, x_path] += 1
        grid[coord[1][1], coord[1][0]] += 1
    print(f"Grid: {np.sum(grid >= 2)}")    

print("Part 1")
part1()
print("Part 2")
part2()