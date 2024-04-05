import random
class TicTacToe:
    def __init__(self):
        #Which sign at which index and which index remains
        self.board_place=[0,1,2,3,4,5,6,7,8]
        #All Win Situations
        self.win_situations=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]   
    def main(self):
        #list for showing which place in board is empty
        self.l=[0,1,2,3,4,5,6,7,8]
        # User's turn = 1 Computer's turn = 0
        self.turn=0
        while True: 
            print("\n\n\n")
            # Prints Board 
            self.printboard()
            if self.turn==1:
                a=int(input("Enter Index where you want to Put X: "))
                # Check if Space is Occupied or Not
                if self.board_place[a]=="X" or self.board_place[a]=="O":
                    print("This space is Occupied")
                else:
                    self.board_place[a]="X"
                    self.l.remove(a)
                    self.turn= 0 if self.turn==1 else 1
            else:
                # Call Method to get index from computer's choice
                self.num=self.computer_logic()
                print("Computer choice is :",self.num)
                self.board_place[self.num]="O"
                self.l.remove(self.num)
                self.turn= 0 if self.turn==1 else 1
            # Check if either user or computer won 
            self.user_won=self.isWon("X")
            self.computer_won=self.isWon("O")
            if len(self.l)==0:
                self.printboard()
                print("Draw")
                break
            if self.user_won:
                self.printboard()
                print("User Won")
                break
            elif self.computer_won:
                self.printboard()
                print("Computer Won")
                break

    def printboard(self):
        print("\n\n\n",self.board_place[0],"|",self.board_place[1],"|",self.board_place[2],"")
        print("---|---|---")
        print("",self.board_place[3],"|",self.board_place[4],"|",self.board_place[5],"")
        print("---|---|---")
        print("",self.board_place[6],"|",self.board_place[7],"|",self.board_place[8],"")
    def isWon(self,sign):
        # From win_situation any situation mathches or not
        for i in self.win_situations:
            if self.board_place[i[0]]==sign and self.board_place[i[1]]==sign and self.board_place[i[2]]==sign:
                return True
        return False  
    def computer_logic(self):
        #check if computer's pair is generating or not . If is then it will try to make pair
        for i in self.win_situations:
            if self.board_place[i[0]]=="O" and self.board_place[i[1]]=="O" and self.board_place[i[2]]!="X" and self.board_place[i[2]]!="O":
                if i[2] in self.l:
                    self.num=i[2]
                    return self.num
            elif self.board_place[i[1]]=="O" and self.board_place[i[2]]=="O" and self.board_place[i[0]]!="X" and self.board_place[i[0]]!="O":
                if i[0] in self.l:
                    self.num=i[0]
                    return self.num
            elif self.board_place[i[0]]=="O" and self.board_place[i[2]]=="O" and self.board_place[i[1]]!="X" and self.board_place[i[1]]!="O":
                if i[1] in self.l:
                    self.num=i[1]
                    return self.num
        #check if User's pair is generating or not. If is then try to block it
        for i in self.win_situations:
            if self.board_place[i[0]]=="X" and self.board_place[i[1]]=="X" and self.board_place[i[2]]!="O" and self.board_place[i[2]]!="X":
                if i[2] in self.l:
                    self.num=i[2]
                    return self.num
            elif self.board_place[i[1]]=="X" and self.board_place[i[2]]=="X" and self.board_place[i[0]]!="O" and self.board_place[i[0]]!="X":
                if i[0] in self.l:
                    self.num=i[0]
                    return self.num
            elif self.board_place[i[0]]=="X" and self.board_place[i[2]]=="X" and self.board_place[i[1]]!="O"and self.board_place[i[1]]!="X":
                if i[1] in self.l:
                    self.num=i[1]
                    return self.num
        # Checks if for win situation one index have O and other two index aren't occupied so it can go for that win situation
        for i in self.win_situations:
            if self.board_place[i[0]]=="O" and self.board_place[i[1]]!="O" and self.board_place[i[2]]!="O" and self.board_place[i[1]]!="X" and self.board_place[i[2]]!="X":
                if i[1] in self.l:
                    self.num=i[1]
                    return self.num
            elif self.board_place[i[0]]!="O" and self.board_place[i[1]]=="O" and self.board_place[i[2]]!="O" and self.board_place[i[1]]!="X" and self.board_place[i[2]]!="X":
                if i[2] in self.l:
                    self.num=i[2]
                    return self.num
            elif self.board_place[i[0]]!="O" and self.board_place[i[1]]!="O" and self.board_place[i[2]]=="O" and self.board_place[i[1]]!="X" and self.board_place[i[2]]!="X":
                if i[0] in self.l:
                    self.num=i[0]
                    return self.num
        #while no pair is becoming
        self.num=random.choice(self.l)
        return self.num

      