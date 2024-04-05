import random
score=0
class InvalidValueException(Exception):
    pass
class Cricket():
    def __init__(self):
        self.score=0
        # If User or pc score is -1 then It's Batting still remain 
        self.user_score=-1
        self.pc_score=-1
        self.temp_score=0
        self.temp_pc_score=0
    # Method to Print Rules
    def printRules(self):
        print("+ + ---------------------------------------------------------------------------------------------------------------------- + +")
        print("+ + ---------------------------------------------------------------------------------------------------------------------- + +")
        print("+ + \tRules: \t\t\t\t\t\t\t\t\t\t\t\t\t\t   + +")
        print("+ + \tUser Should enter Number for scoring that number into runs while batting.\t\t\t\t\t   + +")
        print("+ + \tComputer will show a number if both number are same then batsman gets out.\t\t\t\t\t   + +")
        print("+ + \tSame Rule Will apply for User's Bowling User Have to guess same number of pc to get it OUT\t\t\t   + +")
        print("+ + ---------------------------------------------------------------------------------------------------------------------- + +")
        print("+ + ---------------------------------------------------------------------------------------------------------------------- + +")
    def userBowling(self):
        while True: 
            # Get User's Bowling Input For different delivery variation that which delivery User choose to Bowl 
            self.user_choice=int(input("Enter Integer Between 0 to 6 to get pc OUT: "))
            if self.user_choice>6 or self.user_choice<0:
                raise InvalidValueException("You Entered Invalid Value")
            self.pc_choice=random.choice([0,1,2,3,4,5,6])
            if self.user_choice==self.pc_choice :
                if self.pc_score==-1:
                    self.pc_score=0
                print("It is Out")
                break
            elif ((self.pc_score+self.pc_choice>self.user_score) and self.user_score!=-1):
                print("Computer Scored ",self.pc_choice," Runs")
                if self.pc_score==-1:
                    self.pc_score=0
                self.pc_score+=self.pc_choice
                return self.pc_score
            else:
                if self.pc_score==-1:
                    self.pc_score=0
                print("Computer Scored ",self.pc_choice," Runs")
                self.pc_score+=self.pc_choice
                print(" Computer total runs : ",self.pc_score)
                if self.user_score!=-1:
                    print(" User total runs : ",self.user_score)
        return self.pc_score
    def userBatting(self):
        while True: 
            self.user_choice=int(input("Enter Integer Between 0 to 6 to score runs: "))
            if self.user_choice>6 or self.user_choice<0:
                raise InvalidValueException()
            self.pc_choice=random.choice([0,1,2,3,4,5,6])
            if self.user_choice==self.pc_choice:
                if self.user_score==-1:
                    self.user_score=0
                print("You Are OUT!!!!")
                break
            elif ((self.user_score+self.user_choice>self.pc_score) and self.pc_score!=-1):
                print("User Scored ",self.user_choice," Runs")
                if self.user_score==-1:
                    self.user_score=0
                self.user_score+=self.user_choice
                return self.user_score
            else:
                if self.user_score==-1:
                    self.user_score=0
                print("User Scored ",self.user_choice," Runs")
                self.user_score+=self.user_choice
                print("User total runs : ",self.user_score)
                if self.pc_score!=-1:
                    print(" Computer total runs : ",self.pc_score)
        return self.user_score
    def tossTime(self):
        print("\n\nWohoooo! It's a Toss Time: ")
        print("Enter 1 for Head: ")
        print("Enter 2 for Tails: ")
        user_toss=int(input("Enter Your Call: "))
        if user_toss>2 or user_toss<1:
            raise InvalidValueException
        toss=random.choice([1,2])
        if user_toss==toss:
            return True
        else:
            print("Oops!! You Lost the Toss 😥 It is ",("Head" if toss==1 else "Tails"))
            return False
    def tossChoiceSelection(self):
        if self.tossTime():
            print("Yeah! You Won the Toss What do You Want? ")
            print("Enter 1 for Batting: ")
            print("Enter 2 for Bowling: ")
            user_toss_choice=int(input("Enter Your Preference: "))
            if user_toss_choice>2 or user_toss_choice<1:
                raise InvalidValueException
            if user_toss_choice==1:
                print("You Are Batting First")  
                return True
            elif user_toss_choice==2:
                print("You Are Bowling First")  
                return False
        else:
            computer_toss_choice=random.choice([1,2])
            if computer_toss_choice==1:
                print("You Are Bowling First")  
                return False
            elif computer_toss_choice==2:
                print("You Are Batting First")  
                return True
    def matchStart(self):
        if self.tossChoiceSelection():
            self.temp_score=self.userBatting()
            self.user_score=self.temp_score
            print("\nYou Are Now Bowling defend the target of ",self.user_score+1," Runs. ")
            self.temp_pc_score=self.userBowling()
            self.winner()           
        else:
            temp_pc_score=self.userBowling()
            self.pc_score=temp_pc_score
            print("\nYou Are Now Batting chase the target of ",self.pc_score+1," Runs.")
            self.temp_score=self.userBatting()
            self.winner()
    def winner(self):
        if self.user_score>self.pc_score:
            print("User Won the match ")
            print("User's Score: ",self.user_score)
            print("Commputer's Score: ",self.pc_score)
        elif self.user_score<self.pc_score:
            print("Computer Won the match ")
            print("Computer's Score: ",self.pc_score)
            print("User's Score: ",self.user_score)
        else:
            print("Draw")
            print("Commputer's Score: ",self.temp_pc_score)
            print("User's Score: ",self.temp_score)
