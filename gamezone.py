from tkinter import *
from hangman import Hangman
from cricket import Cricket
from tic_tac_toe import TicTacToe
from stone_paper_scissor import SPS
from eggcatcher import EggCatcher

while True:
    try:
        print("\n\n\nWelcome to Gamezone")
        print("Select Game to Play: ")
        print("1. Hangman")
        print("2. Egg Catcher")
        print("3. Tic Tac Toe")
        print("4. Cricket")
        print("5. Stone Paper Scissor")
        print("6. Exit")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            game1=Hangman()
            game1.main()
        elif choice==2:
            game5=EggCatcher()
            game5.main()
        elif choice==3:
            game2=TicTacToe()
            game2.main()
        elif choice==4:
            game3=Cricket()
            game3.printRules()
            game3.matchStart()
        elif choice==5:
            game4=SPS()
            game4.main()
        elif choice==6:
            print("You Are About to Exit...")
            break
        else:
            print("Invalid Choice")
    except Exception as e:
        print("Exception Occured! ", e)
