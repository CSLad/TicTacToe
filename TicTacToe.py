import random


class TicTacToe:
    def __init__(self, ai):
        self.table = "  |   |  \n  |   |  \n  |   |  "
        self.index = {1:0, 2:4, 3:8, 4:10, 5:14, 6:18, 7:20, 8:24, 9:28}
        self.moves = []
        self.ai = (ai == 1)
        self.player_input = []
        print(self.table)

    def game(self, p):
        if p:
            print("player 1 your turn")
            inp = int(input("Enter a number between 1 - 9"))
        else:
            if not self.ai:
                print("player 2 your turn")
                inp = int(input("Enter a number between 1 - 9"))
            else:
                if len(self.player_input) < 2:
                    if 5 not in self.moves: inp = 5
                    elif 1 not in self.moves: inp = 1
                    elif 3 not in self.moves: inp = 3
                    elif 7 not in self.moves: inp = 7
                    elif 9 not in self.moves: inp = 9
                    else:
                        inp = random.randint(1,9)
                        while inp in self.moves: inp = random.randint(1,9)
                else:
                    if 1 in self.player_input and 2 in self.player_input and 3 not in self.moves: inp = 3
                    elif 1 in self.player_input and 3 in self.player_input and 2 not in self.moves: inp = 2
                    elif 2 in self.player_input and 3 in self.player_input and 1 not in self.moves: inp = 1
                    elif 1 in self.player_input and 7 in self.player_input and 5 not in self.moves: inp = 5
                    elif 1 in self.player_input and 4 in self.player_input and 7 not in self.moves: inp = 7
                    elif 4 in self.player_input and 7 in self.player_input and 1 not in self.moves: inp = 1
                    elif 2 in self.player_input and 8 in self.player_input and 5 not in self.moves: inp = 5
                    elif 2 in self.player_input and 5 in self.player_input and 8 not in self.moves: inp = 8
                    elif 5 in self.player_input and 8 in self.player_input and 2 not in self.moves: inp = 2
                    elif 3 in self.player_input and 9 in self.player_input and 6 not in self.moves: inp = 6
                    elif 3 in self.player_input and 6 in self.player_input and 9 not in self.moves: inp = 9
                    elif 6 in self.player_input and 9 in self.player_input and 3 not in self.moves: inp = 3
                    elif 4 in self.player_input and 6 in self.player_input and 5 not in self.moves: inp = 5
                    elif 4 in self.player_input and 5 in self.player_input and 6 not in self.moves: inp = 6
                    elif 5 in self.player_input and 6 in self.player_input and 4 not in self.moves: inp = 4
                    elif 7 in self.player_input and 9 in self.player_input and 8 not in self.moves: inp = 8
                    elif 7 in self.player_input and 8 in self.player_input and 9 not in self.moves: inp = 9
                    elif 8 in self.player_input and 9 in self.player_input and 7 not in self.moves: inp = 7
                    elif 1 in self.player_input and 9 in self.player_input and 5 not in self.moves: inp = 5
                    elif 1 in self.player_input and 5 in self.player_input and 9 not in self.moves: inp = 9
                    elif 5 in self.player_input and 9 in self.player_input and 1 not in self.moves: inp = 1
                    elif 3 in self.player_input and 7 in self.player_input and 5 not in self.moves: inp = 5
                    elif 3 in self.player_input and 5 in self.player_input and 7 not in self.moves: inp = 7
                    elif 5 in self.player_input and 7 in self.player_input and 3 not in self.moves: inp = 3
                    else:
                        if 5 not in self.moves:
                            inp = 5
                        elif 1 not in self.moves:
                            inp = 1
                        elif 3 not in self.moves:
                            inp = 3
                        elif 7 not in self.moves:
                            inp = 7
                        elif 9 not in self.moves:
                            inp = 9
                        else:
                            inp = random.randint(1, 9)
                            while inp in self.moves: inp = random.randint(1, 9)

                    if inp in self.moves:
                        if 5 not in self.moves:
                            inp = 5
                        elif 1 not in self.moves:
                            inp = 1
                        elif 3 not in self.moves:
                            inp = 3
                        elif 7 not in self.moves:
                            inp = 7
                        elif 9 not in self.moves:
                            inp = 9
                        else:
                            inp = random.randint(1, 9)
                            while inp in self.moves: inp = random.randint(1, 9)

        if inp not in self.moves: self.moves.append(inp)
        else:
            print("invalid move")
            self.game(p)
        temp = list(self.table)
        if p:
            f = "X"
            p = False
            self.player_input.append(inp)
        else:
            f = "O"
            p = True

        temp[self.index[inp]] = f
        self.table = "".join(temp)
        print(self.table)
        c1 = (self.table[0] == self.table[8] == self.table[4] and self.table[0] != " ")
        c2 = (self.table[0] == self.table[10] == self.table[20] and self.table[0] != " ")
        c3 = (self.table[4] == self.table[14] == self.table[24] and self.table[4] != " ")
        c4 = (self.table[8] == self.table[18] == self.table[28] and self.table[8] != " ")
        c5 = (self.table[10] == self.table[14] == self.table[18] and self.table[10] != " ")
        c6 = (self.table[20] == self.table[24] == self.table[28] and self.table[20] != " ")
        c7 = (self.table[0] == self.table[14] == self.table[28] and self.table[0] != " ")
        c8 = (self.table[8] == self.table[14] == self.table[20] and self.table[20] != " ")
        if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8:
            if not p:
                print("player 1 wins!")
                return
            if self.ai:
                print("AI WINS!")
                return
            else:
                print("player 2 wins!")
                return
        elif len(self.moves) != 9:
            print()
            self.game(p)
        else: print("DRAW!")


ai = int(input("Ai or player, 1 or 0?"))
t = TicTacToe(ai)
t.game(True)


