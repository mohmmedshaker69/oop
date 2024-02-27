class Player:
    def __init__(self):
        self.name=""
        self.symbol=""
    def choose_name(self):
        while True:
            name=input("please enter your name [only letters]")
            if name.isalpha:
                self.name=name
            break
        print("only letteeesrss i said!!!!!!!!!")

    def choose_symbol(self):
        while True:
            symbol=input(f"{self.name} choose a symbol[only one letter!!!]")
            if symbol.isalpha and len(symbol)==1:
                self.symbol=symbol
                break
            print("one symbol onlyyy!!!!!")


class Menu:
    def main_menu(self):
        print("welcome press enter")
        while True:
            choice=input("type 1 to start and 2 for quit")
            if choice==1 or choice==2:
                return choice
            break
        print("1 or 2 !!!!!")

    def end_game_menu(self):
        print("the end ,press enter")
        while True:
            choice=input("type 1 to restart or 2 to quit")
            if choice==1 or choice==2:
                return choice
            break
        print("1 or 2 !!!!!")


class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board(i,i+3)))
            if i<6:
                print("_"*5)

    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol
            return True
        return False

    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board=[str(i) for i in range(1,10)]


class Game:
    def __init__(self):
        self.players=[Player(), Player()]
        self.board=Board()
        self.menu=Menu()
        self.current_player_index=0
    def start_game(self):
        choice=self.menu.main_menu()
        if choice=="1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        Player.choose_name()
        Player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice=self.menu.end_game_menu()
                if choice==1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        pass
    def check_win(self):
        pass
    def restart_game(self):
        pass
                

    def quit_game(self):
        print("thankyou for playing ")