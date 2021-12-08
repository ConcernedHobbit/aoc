class BingoNumber:
    def __init__(self, num: int):
        self.number = num
        self.marked = False

    def mark_if(self, num: int):
        if self.number == num:
            self.marked = True

    def mark(self):
        self.marked = True

    def __repr__(self):
        if self.marked:
            return f'<{str(self.number).rjust(2, " ")}>'
        else:
            return f'[{str(self.number).rjust(2, " ")}]'

    def __bool__(self):
        return self.marked

class Board:
    def __init__(self):
        self.board = []
    
    def add_row(self, row: list):
        new_row = []
        for num in row:
            new_row.append(BingoNumber(num))
        self.board.append(new_row)

    def mark_number(self, num: int):
        for row in self.board:
            for number in row:
                number.mark_if(num)

    def won_row(self, row: int):
        return all([bool(num) for num in self.board[row]])

    def won_column(self, column: int):
        return all([bool(row[column]) for row in self.board])

    @property
    def unmarked(self):
        nums = []
        for row in self.board:
            for number in row:
                if not number:
                    nums.append(number.number)
        return nums

    @property
    def has_won(self):
        rows = any([self.won_row(i) for i in range(len(self.board))])
        columns = any([self.won_column(i) for i in range(len(self.board[0]))])
        return any([rows, columns])

    def __repr__(self):
        s = ''
        for row in self.board:
            for number in row:
                s += str(number)
            s += '\n'
        return s[:-1]

numbers = []
boards = []
current_board = Board()
for line in open('day4.txt'):
    line = line.strip()

    if not numbers:
        numbers = [int(n) for n in line.split(',')]
        continue

    if len(line) == 0 and len(current_board.board) > 0:
        boards.append(current_board)
        current_board = Board()
        continue

    if len(line) > 0:
        row = [int(n) for n in line.split()]
        current_board.add_row(row)
boards.append(current_board)

num_boards = len(boards)
part = 1
for num in numbers:
    for board in boards:
        board.mark_number(num)
        if board.has_won:
            if len(boards) in (num_boards, 1):
                print(board)
                print(f'Part {part}: {sum(board.unmarked)} * {num} = {sum(board.unmarked) * num}')
                print()
                part += 1
            boards = [b for b in boards if b is not board]
