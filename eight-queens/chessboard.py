class Chessboard:
    def __init__(self):
        self.board = self.setup_board()

    def __str__(self):
        board_str = ""
        for i in self.board:
            for j in i:
                board_str += "0"
            board_str += "\n"
        return board_str

    def print_board(self):
        return self.__str__()

    def setup_board(self):
        row = [0, 0, 0, 0, 0, 0, 0, 0]
        rows = []
        for i in range(8):
            rows.append(row)
        return rows

    def is_empty(self):
        for i in self.board:
            if not sum(i) == 0:
                return False
        return True

    def place_valid_queen(self):
        if self.is_empty():
            self.board[0][0] = 1

    def queens_are_valid(self):
        for i in self.board:
            for j in i:
                if self.board[i][j] == 1:
                    h = self.check_horizontal_for_queens(i)
                    v = self.check_vertical_for_queens(j)
                    d = self.check_diagonal_for_queens(i, j)
                    return h and v and d

    def check_horizontal_for_queens(self, row):
        return sum(self.board[row]) == 1

    def check_vertical_for_queens(self, column):
        sum_of_queens = 0
        for row in self.board:
            sum_of_queens += row[column]
        return sum_of_queens == 1

    def check_diagonal_for_queens(self, row, column):
        nw = self.traverse_north_west(row, column)
        ne = self.traverse_north_east(row, column)
        sw = self.traverse_south_west(row, column)
        se = self.traverse_south_east(row, column)
        for i in self.board:
            for j in i:
                self.board[i][j]

    def traverse_north_west(self, row, column):
        sum_of_queens = 0
        if row > 0 and column > 0:
            sum_of_queens += self.traverse_north_west(row - 1, column - 1)
        if self.board[row][column] == 1:
            return sum_of_queens + 1
        return sum_of_queens

    def traverse_north_east(self, row, column):
        pass

    def traverse_south_east(self, row, column):
        pass

    def traverse_south_west(self, row, column):
        pass
