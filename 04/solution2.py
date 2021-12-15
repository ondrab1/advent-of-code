def check_board(marks, board_index):
    # horizontally check
    for y, row in marks[board_index].items():
        win = True
        for x, value in enumerate(row):
            if value is None:
                win = False
                break

        if win is True:
            return True

    # vertically check
    column_max_index = max(len(item) for item in marks[board_index].values())
    for x in range(0, column_max_index):
        win = True
        for y, row in marks[board_index].items():
            if row[x] is None:
                win = False
                break

        if win is True:
            return True

    return False


lines = open("input.txt").read().splitlines()

numbers = []
boards = {}

# parse board
board_index = -1
board_line_index = 0
for index, line in enumerate(lines):
    if index == 0:
        numbers = line.split(',')
        continue

    if line == '':
        board_index += 1
        board_line_index = 0
        continue

    if board_index > -1:
        if board_index not in boards:
            boards[board_index] = {}

        boards[board_index][board_line_index] = list(filter(None, line.split(' ')))
        board_line_index += 1

marks = {x: {y: [None for z in boards[x][y]] for y in boards[x].keys()} for x in boards.keys()}
won_boards = {}

won_number = None
won_board = None
for number in numbers:
    # do marks
    for board_index, rows in boards.items():
        if board_index in won_boards:
            continue

        for y, row in rows.items():
            for x, value in enumerate(row):
                if value == number:
                    marks[board_index][y][x] = value

        result = check_board(marks, board_index)
        if result is True:
            won_board = board_index
            won_number = int(number)
            won_boards[board_index] = True

unmarked_numbers = []
for y, row in boards[won_board].items():
    for x, value in enumerate(row):
        if marks[won_board][y][x] is None:
            unmarked_numbers.append(int(value))

unmarked_sum = sum(unmarked_numbers)

# print(unmarked_sum, won_number, won_board)
print(unmarked_sum * int(won_number))
