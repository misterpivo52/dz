import tkinter as tk

# Символи Юнікоду для шахових фігур
UNICODE_PIECES = {
    'white': {
        'King': '♔', 'Queen': '♕', 'Rook': '♖', 'Bishop': '♗', 'Knight': '♘', 'Pawn': '♙'
    },
    'black': {
        'King': '♚', 'Queen': '♛', 'Rook': '♜', 'Bishop': '♝', 'Knight': '♞', 'Pawn': '♟'
    }
}

# Базовий клас для шахової фігури
class Piece:
    def __init__(self, color, x, y):
        self.color = color  # 'white' або 'black'
        self.x = x  # поточна x позиція на дошці (0-7)
        self.y = y  # поточна y позиція на дошці (0-7)
        self.has_moved = False  # Прапорець, який показує, чи фігура вже переміщалася

    def get_position(self):
        return self.x, self.y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.has_moved = True

# Класи для кожної шахової фігури
class Pawn(Piece):
    def is_valid_move(self, new_x, new_y, board):
        direction = -1 if self.color == 'white' else 1
        if new_y == self.y and board[new_x][new_y] is None:
            if new_x == self.x + direction:
                return True
            if new_x == self.x + 2 * direction and not self.has_moved and board[self.x + direction][new_y] is None:
                return True
        if new_x == self.x + direction and abs(new_y - self.y) == 1 and board[new_x][new_y] is not None:
            return True
        return False

class Knight(Piece):
    def is_valid_move(self, new_x, new_y, board):
        dx = abs(self.x - new_x)
        dy = abs(self.y - new_y)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

class Bishop(Piece):
    def is_valid_move(self, new_x, new_y, board):
        return abs(self.x - new_x) == abs(self.y - new_y)

class Rook(Piece):
    def is_valid_move(self, new_x, new_y, board):
        return self.x == new_x or self.y == new_y

class Queen(Piece):
    def is_valid_move(self, new_x, new_y, board):
        return (self.x == new_x or self.y == new_y) or (abs(self.x - new_x) == abs(self.y - new_y))

class King(Piece):
    def is_valid_move(self, new_x, new_y, board):
        if max(abs(self.x - new_x), abs(self.y - new_y)) == 1:
            return True
        if not self.has_moved and (new_x == self.x) and (abs(new_y - self.y) == 2):
            rook_y = 0 if new_y < self.y else 7
            rook = board[self.x][rook_y]
            if isinstance(rook, Rook) and not rook.has_moved:
                step = 1 if new_y > self.y else -1
                for i in range(self.y + step, rook_y, step):
                    if board[self.x][i] is not None:
                        return False
                return True
        return False

# Клас шахової дошки
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece):
        x, y = piece.get_position()
        self.board[x][y] = piece

    def move_piece(self, old_x, old_y, new_x, new_y):
        piece = self.board[old_x][old_y]
        if piece and piece.is_valid_move(new_x, new_y, self.board):
            if not self.causes_check(piece.color, old_x, old_y, new_x, new_y):
                if isinstance(piece, King) and abs(new_y - piece.y) == 2:
                    rook_y = 0 if new_y < piece.y else 7
                    new_rook_y = piece.y - 1 if rook_y == 0 else piece.y + 1
                    rook = self.board[piece.x][rook_y]
                    self.board[piece.x][rook_y] = None
                    self.board[piece.x][new_rook_y] = rook
                    rook.move(piece.x, new_rook_y)
                self.board[old_x][old_y] = None
                self.board[new_x][new_y] = piece
                piece.move(new_x, new_y)
                return True
        return False

    def get_piece_at(self, x, y):
        return self.board[x][y]

    def find_king(self, color):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if isinstance(piece, King) and piece.color == color:
                    return piece
        return None

    def is_in_check(self, color):
        king = self.find_king(color)
        if not king:
            return False
        king_x, king_y = king.get_position()
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color != color and self.is_attacking_king(piece, king_x, king_y):
                    return True
        return False

    def is_attacking_king(self, piece, king_x, king_y):
        if isinstance(piece, (Rook, Queen)):
            if piece.x == king_x:
                step = 1 if piece.y < king_y else -1
                for y in range(piece.y + step, king_y, step):
                    if self.board[king_x][y] is not None:
                        return False
                return True
            if piece.y == king_y:
                step = 1 if piece.x < king_x else -1
                for x in range(piece.x + step, king_x, step):
                    if self.board[x][king_y] is not None:
                        return False
                return True

        if isinstance(piece, (Bishop, Queen)):
            if abs(piece.x - king_x) == abs(piece.y - king_y):
                x_step = 1 if piece.x < king_x else -1
                y_step = 1 if piece.y < king_y else -1
                for step in range(1, abs(piece.x - king_x)):
                    if self.board[piece.x + step * x_step][piece.y + step * y_step] is not None:
                        return False
                return True

        if isinstance(piece, Knight):
            return piece.is_valid_move(king_x, king_y, self.board)

        if isinstance(piece, Pawn):
            direction = -1 if piece.color == 'white' else 1
            return (king_x == piece.x + direction and abs(king_y - piece.y) == 1)

        return False

    def causes_check(self, color, old_x, old_y, new_x, new_y):
        temp_board = Board()
        for i in range(8):
            for j in range(8):
                temp_board.board[i][j] = self.board[i][j]
        temp_board.board[new_x][new_y] = temp_board.board[old_x][old_y]
        temp_board.board[old_x][old_y] = None
        return temp_board.is_in_check(color)

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color == color:
                    for new_x in range(8):
                        for new_y in range(8):
                            if piece.is_valid_move(new_x, new_y, self.board) and not self.causes_check(color, i, j, new_x, new_y):
                                return False
        return True

# Графічний інтерфейс через Tkinter
class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Шахова гра")
        self.board = Board()
        self.create_widgets()
        self.current_player = 'white'
        self.selected_piece = None

    def create_widgets(self):
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                button = tk.Button(self.root, text="", width=6, height=3, command=lambda i=i, j=j: self.cell_clicked(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.log_text = tk.Text(self.root, height=8, width=50)
        self.log_text.grid(row=8, column=0, columnspan=8)
        self.log_text.insert(tk.END, "Гра почалася. Ходять білі.\n")

        self.cancel_button = tk.Button(self.root, text="Скасувати вибір", command=self.cancel_selection)
        self.cancel_button.grid(row=9, column=0, columnspan=4)

        self.castling_button = tk.Button(self.root, text="Зробити рокіровку", command=self.castling)
        self.castling_button.grid(row=9, column=4, columnspan=4)

        self.setup_pieces()
        self.update_board()

    def setup_pieces(self):
        for i in range(8):
            self.board.place_piece(Pawn('white', 6, i))
            self.board.place_piece(Pawn('black', 1, i))

        self.board.place_piece(Rook('white', 7, 0))
        self.board.place_piece(Rook('white', 7, 7))
        self.board.place_piece(Rook('black', 0, 0))
        self.board.place_piece(Rook('black', 0, 7))

        self.board.place_piece(Knight('white', 7, 1))
        self.board.place_piece(Knight('white', 7, 6))
        self.board.place_piece(Knight('black', 0, 1))
        self.board.place_piece(Knight('black', 0, 6))

        self.board.place_piece(Bishop('white', 7, 2))
        self.board.place_piece(Bishop('white', 7, 5))
        self.board.place_piece(Bishop('black', 0, 2))
        self.board.place_piece(Bishop('black', 0, 5))

        self.board.place_piece(Queen('white', 7, 3))
        self.board.place_piece(Queen('black', 0, 3))

        self.board.place_piece(King('white', 7, 4))
        self.board.place_piece(King('black', 0, 4))

    def cell_clicked(self, x, y):
        piece = self.board.get_piece_at(x, y)
        if self.selected_piece:
            if self.board.move_piece(self.selected_piece.x, self.selected_piece.y, x, y):
                self.log_move(self.selected_piece, x, y)
                self.update_board()
                self.selected_piece = None
                if self.board.is_checkmate(self.current_player):
                    self.log_text.insert(tk.END, f"Мат! {self.current_player.capitalize()} програли.\n")
                self.toggle_player()
            else:
                self.log_text.insert(tk.END, "Неможливий хід! Спробуйте знову.\n")
        elif piece and piece.color == self.current_player:
            self.selected_piece = piece
            self.log_text.insert(tk.END, f"Вибрано {UNICODE_PIECES[piece.color][piece.__class__.__name__]} на ({x}, {y}).\n")
        else:
            self.log_text.insert(tk.END, "Помилка! Хибний вибір.\n")

    def update_board(self):
        for i in range(8):
            for j in range(8):
                piece = self.board.get_piece_at(i, j)
                if piece:
                    self.buttons[i][j].config(text=UNICODE_PIECES[piece.color][piece.__class__.__name__])
                else:
                    self.buttons[i][j].config(text="")
                # Забарвлення клітинки
                color = 'white' if (i + j) % 2 == 0 else 'gray'
                self.buttons[i][j].config(bg=color)

    def log_move(self, piece, x, y):
        self.log_text.insert(tk.END, f"{piece.color.capitalize()} {piece.__class__.__name__} пересунуто на ({x}, {y}).\n")

    def toggle_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        self.log_text.insert(tk.END, f"Ходять {self.current_player.capitalize()}.\n")
        if self.board.is_in_check(self.current_player):
            self.log_text.insert(tk.END, f"Шах {self.current_player.capitalize()} королю!\n")

    def cancel_selection(self):
        if self.selected_piece:
            self.log_text.insert(tk.END, "Вибір фігури скасовано.\n")
            self.selected_piece = None
        else:
            self.log_text.insert(tk.END, "Немає вибраної фігури для скасування.\n")

    def castling(self):
        if isinstance(self.selected_piece, King) and not self.selected_piece.has_moved:
            y_direction = 7 if self.selected_piece.color == 'white' else 0
            if self.board.move_piece(self.selected_piece.x, self.selected_piece.y, self.selected_piece.x, 6):
                self.log_move(self.selected_piece, self.selected_piece.x, 6)
                self.update_board()
                self.toggle_player()
            elif self.board.move_piece(self.selected_piece.x, self.selected_piece.y, self.selected_piece.x, 2):
                self.log_move(self.selected_piece, self.selected_piece.x, 2)
                self.update_board()
                self.toggle_player()
            else:
                self.log_text.insert(tk.END, "Рокіровка неможлива!\n")
        else:
            self.log_text.insert(tk.END, "Для рокіровки виберіть короля.\n")

# Запуск програми
if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()