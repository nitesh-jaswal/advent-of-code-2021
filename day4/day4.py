from typing import List, Tuple

class Board():

    SIZE = 5

    def __init__(self, input_lines: List):
        self._board = [[int(num) for num in line.split(' ') if num != ''] for line in input_lines]

    def _check_if_solved(self) -> bool:
        sz = Board.SIZE
        return \
        any([all([num is None for num in row]) for row in self._board ]) | \
        any([all([self._board[j][i] is None for j in range(sz)]) for i in range(sz)])

    
    def _replace_number_if_present(self, number: int):
        for i, row in enumerate(self._board):
            if number in row:
                index = self._board[i].index(number)
                self._board[i][index] = None
    
    def _calculate_score(self) -> int:
        return sum([sum([num for num in row if num != None]) for row in self._board])
    
    def play(self, number: int) -> Tuple[bool, int]:
        self. _replace_number_if_present(number=number)
        is_solved = self._check_if_solved() 
        score = None
        if is_solved:
            score = self._calculate_score()
        return ((is_solved, score))


def parse_input() -> Tuple[List, List]:
    boards = []
    input_nums = []
    with open("input.txt", 'r') as infile:
        input_nums += [int(num) for num in infile.readline().rstrip().split(',')]
        infile.readline()
        input_lines = []
        for line in infile:
            line = line.rstrip()
            if len(line) == 0:
                # print(input_lines)
                boards += [Board(input_lines=input_lines)]
                input_lines = []
                continue
            input_lines += [line]
        boards += [Board(input_lines=input_lines)]
    return((input_nums, boards))

def part1():
    input_nums, boards = parse_input()
    for number in input_nums:
        # print(number)
        for i, board in enumerate(boards):
            is_solved, score = board.play(number)
            # print(f"{i}, SOLVED: {is_solved}, SCORE: {score}")
            if is_solved:
                print(score*number)
                return 1

def part2():
    input_nums, boards = parse_input()
    for number in input_nums:
        # print(number)
        remove_index = []
        for i, board in enumerate(boards):
            is_solved, score = board.play(number)
            # print(f"{i}, SOLVED: {is_solved}, SCORE: {score}")
            if is_solved:
                remove_index += [i]
                if len(boards) == 1:
                    print(score*number)
                    return 1
        boards = [boards[i] for i in range(len(boards)) if i not in remove_index]
        
                
# part1()
part2()

# test = Board(['1 2 3 4 5',  '6 7 8 9 10',  '11 12 13 14 15',  '16 17 18 19 20',  '21 22 23 24 25'])
# print(test._board)
# test.play(1)
# print(test._board)
# test.play(6)
# test.play(11)
# test.play(16)
# test.play(21)
# test.play(2)
# test.play(3)
# test.play(4)
# test.play(5)

# print(test._board)
# print(test._check_if_solved())