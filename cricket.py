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
        print("Cricket Challenge Rules")
        print("Batting Rules:")
        print("1. As the batsman, your goal is to score runs by entering numbers.")
        print("2. You can continue batting until you either get out or decide to declare.")
        print("3. Each number you enter represents the runs you score on that delivery.")
        print("4. However, if the number you enter matches the number chosen by the computer, you'll be declared out, so choose your numbers wisely!\n")

        print("Bowling Rules:")
        print("1. As the bowler, your aim is to dismiss the batsman by guessing the number they've entered.")
        print("2. Enter a number of your own, attempting to match the batsman's number to get them out.")
        print("3. Accurately guessing the batsman's number will result in them being declared out.\n")

        print("Game Dynamics:")
        print("1. The game proceeds with alternating turns between batting and bowling.")
        print("2. There is no limit to the number of deliveries per player; the game continues until the batsman is dismissed or wins.\n")

        print("User Interface:")
        print("1. Enjoy a modern and intuitive interface designed for easy interaction.")
        print("2. Simply input your chosen number using the provided interface to make your move.")
        print("3. Clear and concise feedback will keep you informed of the game's progress and your performance.\n")

        print("Get ready to immerse yourself in the excitement of our Cricket Challenge! Step up to the crease and prove your mettle in this thrilling battle of numbers!")

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
