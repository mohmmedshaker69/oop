class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("please enter your name [only letters]: ")
            if name.isalpha():
                self.name = name
                break
            print("only letters allowed!")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name} choose a symbol [only one letter!]: ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol
                break
            print("only one symbol allowed!")


class Menu:
    def main_menu(self):
        print("welcome press enter")
        while True:
            choice = input("type 1 to start and 2 for quit: ")
            if choice in ["1", "2"]:
                return int(choice)
            print("1 or 2 only!")

    def end_game_menu(self):
        print("the end, press enter")
        while True:
            choice = input("type 1 to restart or 2 to quit: ")
            if choice in ["1", "2"]:
                return int(choice)
            print("1 or 2 only!")


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("_"*5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for player in self.players:
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.end_game_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn with symbol {player.symbol}")
        while True:
            try:
                cell_choice = int(input("choose num [1 to 9]: "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("invalid move")
            except ValueError:
                print("from 1 to 9 only!")

        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print("Thank you for playing!")


if __name__ == "__main__":
    game = Game()
    game.start_game()
