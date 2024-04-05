from tkinter import *
import random
class EggCatcher:
    def __init__(self):
        # To get window 
        self.root = Tk()
        self.root.title("Egg Catcher")
        self.height=600
        self.width=500
        # To get screen width of device so can center the window
        self.x1=self.root.winfo_screenwidth()
        self.y1=self.root.winfo_screenheight()
        x=(self.x1/2)-(self.width/2)
        y=(self.y1/2)-(self.height/2)
        # Set window at middle of the screen
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        # Set canvas height width 
        self.canvas=Canvas(self.root,width=500,height=600)
        # To make rectangular catcher with blue color
        self.catcher=self.canvas.create_rectangle(10, 570, 90, 590,outline = "black", fill = "blue",width = 2)
        # To make Golden Egg
        self.egg=self.canvas.create_oval(20, 10, 60, 70,outline = "red", fill = "Yellow",width = 2)
        self.score=0
        # To show score in canvas at North(Upper) section of canvas 
        self.score_text = self.canvas.create_text(50, 20, text="Score: " + str(self.score),anchor="n")
        # Set coords of Score
        self.canvas.coords(self.score_text, 400, 10)
        # Set window to appear at front of all window instead of back of the other windows
        self.root.attributes("-topmost", True) 
    def move_left(self):
        # Move left the catcher to left
        # print(self.canvas.coords(self.catcher))
        if self.canvas.coords(self.catcher)[0]>=20:
            self.canvas.move(self.catcher, -20, 0)
    def move_right(self):
        # Move left the catcher to left
        if self.canvas.coords(self.catcher)[2]<=480:
            self.canvas.move(self.catcher, 20, 0)
        
    def moveEgg(self,egg,score):
        # Move Egg to down 3 pixel
        self.canvas.move(self.egg,0,3) 
        self.catchercoords=self.canvas.coords(self.catcher)
        self.eggcoords=self.canvas.coords(egg)
        # to see if egg is in line with catcher that catcher can catch
        if self.catchercoords[0]<=(self.eggcoords[0]+20) and self.catchercoords[2]>=(self.eggcoords[0]+20) and self.catchercoords[1]<self.eggcoords[3] and self.catchercoords[3]>self.eggcoords[3]:
            # One point for Egg Caught
            self.score+=1
            # Change score
            self.canvas.itemconfig(self.score_text, text="Score: " + str(self.score)) 
            # Delete Egg
            self.canvas.delete(egg)
            # Generate New Egg's Position
            x1=random.randrange(20,440)
            # Generate New Egg at New Position
            self.egg=self.canvas.create_oval(x1, 10, (x1+40), 70,outline = "red", fill = "Yellow",width = 2)
            # Call Move Egg Method so New Egg Can Drop Down
            self.moveEgg(self.egg,self.score)
            return True
        # Check if Egg is Outside of catcher if Yes then Egg Not caught
        elif self.catchercoords[1]<self.eggcoords[3] and (self.catchercoords[0]>(self.eggcoords[0]+20) or self.catchercoords[2]<(self.eggcoords[0]+20)) :
            print("Egg Not Caught ! Your Final Score is : ",self.score)
            self.canvas.delete(egg)
            # Destroy Window When Egg Not caught
            self.root.destroy()
            return False
        # Call Move Egg method after 10 Milliseconds so Egg Can Drop Down smoothly
        self.canvas.after(10, self.moveEgg,egg,score)
    def main(self):
        # Make Button for make catcher move left right
        self.left_button = Button(self.root, text="<-", command=self.move_left, width=5, height=1,bg="red", fg="white")
        self.left_button.place(x=10, y=0)

        self.right_button = Button(self.root, text="->", command=self.move_right, width=5, height=1 ,bg="red", fg="white")
        self.right_button.place(x=50, y=0)
        self.moveEgg(self.egg,self.score)
        self.canvas.pack()
        self.root.mainloop()
 
