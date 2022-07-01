def print_rows():
    number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
    for row in number_board:
        print(' | ' + ' | '.join(row) + ' | ')



print(print_rows())
