from constants import Symbol
from pprint import pprint

class Cell:
    def __init__(self, row_num, col_num, name) -> None:
        self.row_num = row_num
        self.col_num = col_num
        self.name = name
        self.is_filled = False
        self.value = None

    def __repr__(self) -> str:
        obj_repr = {"name": self.name, "position": (self.row_num, self.col_num), "value": self.value}
        return f'{obj_repr}'
    
class Board:
    def __init__(self, dimensions=3):
        self.dimensions = dimensions
        self.flattened_cells = []
        self.cells = self.initialize_cells()
        self.fill_number = 0
    def is_empty(self):
        return self.fill_number == 0

    def is_not_empty(self):
        return self.fill_number <= 9
    
    def is_cell_filled(self, name):
        cell_in_context = self.get_cell_from_name(name)
        return cell_in_context.is_filled
    
    def get_cell_from_name(self, name):
        return next(filter(lambda x: x.name == name, [cell for cell in self.flattened_cells]))
    
    def insert_move(self, name, player):
        cell_in_context = self.get_cell_from_name(name)
        cell_in_context.value = player.symbol
        cell_in_context.is_filled = True
        self.fill_number += 1
    
    def initialize_cells(self):
        cells = []
        alpha_value = 65
        for i in range(3):
            cols = []
            for j in range(3):
                cell = Cell(i, j, name=chr(alpha_value))
                alpha_value += 1
                cols.append(cell)
                self.flattened_cells.append(cell)
            cells.append(cols)
        return cells
    
    def print_board(self):
        board = self.cells
        for i in range(3):
            string_with_cols = f" {board[i][0].value} | {board[i][1].value} | {board[i][2].value} "
            print(f" {board[i][0].value} | {board[i][1].value} | {board[i][2].value} ")
            if i < 2:
                print("-"*len(string_with_cols))



class Player:
    def __init__(self, symbol='') -> None:
        self.symbol = symbol

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.players = self.initialize_players()
        self.winner = None

    def initialize_players(self):
        return [Player(symbol=Symbol.DOT.value), Player(symbol=Symbol.CROSS.value)]

    def show_board(self):
        self.board.print_board()
    
    def is_not_valid(self, move):
        if move not in "ABCDEFGHI":
            return True
        return self.board.is_cell_filled(move)

    def is_game_over(self):
        b = self.board.cells
        print("inside game over")
        print(b)
        for i in range(3):
            if b[i][0].value == b[i][1].value == b[i][2].value:
                filter_val = list(filter(lambda x: x.symbol == b[i][0].value and b[0][i].value is not None, self.players))
                self.winner = filter_val[0] if filter_val else None
                return True if self.winner else False
            if b[0][i].value == b[1][i].value == b[2][i].value:
                filter_val = list(filter(lambda x: x.symbol == b[0][i].value and b[0][i].value is not None, self.players))
                self.winner = filter_val[0] if filter_val else None
                return True if self.winner else False
        if b[0][0].value == b[1][1].value == b[2][2].value:
            filter_val = list(filter(lambda x: x.symbol == b[0][0].value and b[0][0].value is not None, self.players))
            self.winner = filter_val[0] if filter_val else None
            return True if self.winner else False
        if b[0][-1].value == b[1][1].value == b[2][0].value:
            filter_val = list(filter(lambda x: x.symbol == b[0][0].value and b[0][0].value is not None, self.players))
            self.winner = filter_val[0] if filter_val else None
            return True if self.winner else False
        return False

    
    def play(self):
        move_num = 1
        print(self.board.fill_number)
        while self.board.is_not_empty():
            print(f"Move no. {move_num}")
            self.show_board()
            move_p1 = input(f"Name the place where you want to add the value, {self.players[0]}")
            while self.is_not_valid(move_p1):
                move_p1 = input(f"Not a valid move! Try again!\nName the place where you want to add the value, {self.players[0]}")
            self.board.insert_move(move_p1, self.players[0])
            if self.is_game_over():
                break
            move_p2 = input(f"Name the place where you want to add the value, {self.players[1]}")
            while self.is_not_valid(move_p2):
                move_p2 = input(f"Not a valid move! Try again!\nName the place where you want to add the value, {self.players[1]}")
            self.board.insert_move(move_p2, self.players[1])
            if self.is_game_over():
                break
            move_num += 1
            print("\n\n")
        if self.is_game_over() or self.board.is_not_empty():
            if self.winner is not None:
                print(f"Game over: winner is {self.winner}")
                self.show_board()
            else:
                print(f"Game over: No one won!")
                self.show_board()
        
            

            


if __name__ == "__main__":
    game = TicTacToe()
    game.play()