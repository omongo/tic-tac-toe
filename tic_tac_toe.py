class TicTacToe:
    def __init__(self):
        self.current_turn = 'X'
        self.next_turn = 'O'
        self.board = Board()
        self.result = None

    def choose(self, x, y):
        if self.result:
            return
        i = (x * 3) + y
        try:
            self.board[i] = self.current_turn
        except (IndexError, TypeError) as e:
            print(e)
            return
        self.change_turn()

    def change_turn(self):
        self.current_turn, self.next_turn = self.next_turn, self.current_turn

    def finished(self):
        board = self.board.to_str()
        pair = self.next_turn * 3
        patterns = (board[0:3:1], board[3:6:1], board[6:9:1], board[0:7:3],
                    board[1:8:3], board[2:9:3], board[0:9:4], board[2:7:2])
        if ' ' not in board:
            self.result = 'Draw'
            return True
        if pair in patterns:
            self.result = self.next_turn + ' wins.'
            return True
        else:
            return False

    def get_current_turn(self):
        return self.current_turn

    def get_board(self):
        return self.board

    def get_result(self):
        return self.result

    def __repr__(self):
       return "Current Turn: " + str(self.current_turn) + '\n' + \
              "Result: " + str(self.result) + '\n' + \
              "Board:\n" + str(self.board)

    def __str__(self):
        return str(self.board)

class Board:
    def __init__(self, n=9):
        self.data = [' '] * n

    def to_str(self):
        return ''.join(self.data)

    def get_data(self):
        return self.data

    def __getitem__(self, y):
        return self.data[y]

    def __setitem__(self, i, y):
        if self.data[i] == ' ':
            self.data[i] = y
        else:
            raise TypeError('This position was already marked.')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (str(self.data[0:3]) + '\n' +
                str(self.data[3:6]) + '\n' +
                str(self.data[6:9]))

if __name__ == '__main__':
    game = TicTacToe()
    seperators = {',', ' '}
    while not game.finished():
        print(game)
        raw = input('Enter a position for {}: '.format(game.get_current_turn()))
        if len(raw) != 3 or raw[1] not in seperators:
            continue
        try:
            x = int(raw[0])
            y = int(raw[2])
        except ValueError as e:
            print(e)
            continue
        finally:
            game.choose(x, y)
    print(game)
    print(game.get_result())
