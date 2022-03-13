class Game():
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.status = True
        self.turn = 0

    def run(self):
        self.showboard()
        if self.turn % 2 == 0:
            self.p1choice()
        else:
            self.p2choice()

        if self.finishgame():
            winner = str()
            if self.turn % 2 == 0:
                winner = 'X'
            else:
                winner = 'O'
            self.showboard()
            print('The game finished !!! The winner is : {}'.format(winner))
            self.status = False
        self.turn += 1
    def showboard(self):
        for i in self.board:
            print(i)

    def p1choice(self):
        row = int(input('X player input row number :'))
        while row < 1 or row > 3:
            row = int(input('Row number must be between 1 and 3'))
        column = int(input('X player input column number :'))
        while column < 1 or column > 3:
            column = int(input('Column number must be between 1 and 3'))

        while self.isfull(row,column):
            print('This place is full !')
            row = int(input('X player input row number :'))
            while row < 1 or row > 3:
                row = int(input('Row number must be between 1 and 3'))
            column = int(input('X player input column number :'))
            while column < 1 or column > 3:
                column = int(input('Column number must be between 1 and 3'))
        self.board[row-1][column-1] = 'X'
    def p2choice(self):
        row = int(input('O player inbut row number :'))
        while row < 1 or row > 3:
            row = int(input('Row number must be between 1 and 3'))
        column = int(input('O player input column number :'))
        while column < 1 or column > 3:
            column = int(input('O player input column number :'))

        while self.isfull(row,column):
            print('This place is full !')
            row = int(input('O player inbut row number :'))
            while row < 1 or row > 3:
                row = int(input('Row number must be between 1 and 3'))
            column = int(input('O player input column number :'))
            while column < 1 or column > 3:
                column = int(input('O player input column number :'))
        self.board[row-1][column-1] = 'O'
    def finishgame(self):
        if [self.board[0][0],self.board[0][1],self.board[0][2]] == ['X','X','X'] or [self.board[0][0],self.board[0][1],self.board[0][2]] == ['O','O','O']:
            return True
        if [self.board[1][0],self.board[1][1],self.board[1][2]] == ['X','X','X'] or [self.board[1][0],self.board[1][1],self.board[1][2]] == ['O','O','O']:
            return True
        if [self.board[2][0],self.board[2][1],self.board[2][2]] == ['X','X','X'] or [self.board[2][0],self.board[2][1],self.board[2][2]] == ['O','O','O']:
            return True
        if [self.board[0][0],self.board[1][0],self.board[2][0]] == ['X','X','X'] or [self.board[0][0],self.board[1][0],self.board[2][0]] == ['O','O','O']:
            return True
        if [self.board[0][1],self.board[1][1],self.board[2][1]] == ['X','X','X'] or [self.board[0][1],self.board[1][1],self.board[2][1]] == ['O','O','O']:
            return True
        if [self.board[0][2],self.board[1][2],self.board[2][2]] == ['X','X','X'] or [self.board[0][2],self.board[1][2],self.board[2][2]] == ['O','O','O']:
            return True
        if [self.board[0][0],self.board[1][1],self.board[2][2]] == ['X','X','X'] or [self.board[0][0],self.board[1][1],self.board[2][2]] == ['O','O','O']:
            return True
        if [self.board[0][2],self.board[1][1],self.board[2][0]] == ['X','X','X'] or [self.board[0][2],self.board[1][1],self.board[2][0]] == ['O','O','O']:
            return True

        return False
    def isfull(self,row,column):
        if self.board[row-1][column-1] != ' ':
            return True
        return False


game = Game()

while game.status:
    game.run()