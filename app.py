from tkinter import *
from PIL import Image, ImageTk
from random import randint

############################# Window Frame ##################################################
win = Tk()
win.title(" Rock paper and scissor")
win.geometry('1040x700')
win.configure(background='white')

############################## Code ##################################################

choices =["rock","paper","scissor"]
def updateChoice(x):
 
#For computer
 compChoice= choices[randint(0,2)]
 if compChoice == "rock":
  cm_label.configure(image=img1_comp)
 elif compChoice == "paper":
  cm_label.configure(image=img2_comp)
 else:
  cm_label.configure(image=img3_comp)

# For Player
 if x=="rock":
  pl_label.configure(image=img1)
 elif x=="paper":
  pl_label.configure(image=img2)
 else:
  pl_label.configure(image=img3)

 checkwin(x,compChoice)

 #update Result message
def updateMessage(x):
 Result['text'] = x

def updateplayerscore():
 score = int(Player_score["text"])
 score +=1
 Player_score["text"]=str(score)

def updatecompscore():
 score = int(comp_score["text"])
 score +=1
 comp_score["text"]=str(score)

def checkwin(player,computer):
 if player == computer:
     updateMessage("its a tie !!")
 elif player == "rock":
  if computer == "paper":
     updateMessage("Computer wins :(")
     updatecompscore()
  else:
     updateMessage("You Win :)")
     updateplayerscore()
 elif player == "paper":
   if computer =="scissor":
     updateMessage("Computer wins :(")
     updatecompscore()
   else:
     updateMessage("You Win :)")
     updateplayerscore()
 elif player== "scissor":
   if computer =="rock":
     updateMessage("Computer wins :(")
     updatecompscore
   else:
     updateMessage("You Win :)")
     updateplayerscore()
 else:
  pass
############################# Images ####################################

img1=ImageTk.PhotoImage(Image.open("images/rock.png"))
img2=ImageTk.PhotoImage(Image.open("images/paper.png"))
img3=ImageTk.PhotoImage(Image.open("images/scissors.png"))

img1_comp=ImageTk.PhotoImage(Image.open("images/rock.png"))
img2_comp=ImageTk.PhotoImage(Image.open("images/paper.png"))
img3_comp=ImageTk.PhotoImage(Image.open("images/scissors.png"))

#################################### labels ####################################

rps_label=Label(win,text='Rock paper scissor Game',fg='black',bg='white',font=("Times new roman",20,"bold"))
rps_label.pack()
computer=Label(win, text='COMPUTER',bg='white',fg='black', font=("Times new roman",20,"bold"))
computer.place(x=114,y=500)
player=Label(win, text='PLAYER',bg='white',fg='black', font=("Times new roman",20,"bold"))
player.place(x=797,y=500)
Result=Label(win,fg='black', font=("Times new roman",20,"bold"))
Result.place(x=440,y=448)
score=Label(win, text='Score',fg='black', font=("Times new roman",20,"bold"))
score.place(x=489,y=158)
comp_score=Label(win, text=0,fg='black', font=("Times new roman",20,"bold"))
comp_score.place(x=449,y=285)
Player_score=Label(win, text=0,fg='black', font=("Times new roman",20,"bold"))
Player_score.place(x=559,y=285)
cm_label=Label(win,image=img1)
cm_label.place(x=95,y=210)
pl_label=Label(win,image=img3)
pl_label.place(x=748,y=210)

############################### Buttons ###################################
button_rock = Button(win,width=16, 
height=3,text="ROCK",font=("arial",10,"bold"),bg="purple",fg="white",command=
lambda:updateChoice("rock"))
button_rock.place(x=193,y=600)
button_paper = Button(win,width=16,
height=3,text="PAPER",font=("arial",10,"bold"),bg="purple",fg="white",command=
lambda:updateChoice("paper"))
button_paper.place(x=432,y=600)
button_scissor = Button(win,width=16,
height=3,text="SCISSOR",font=("arial",10,"bold"),bg="purple",fg="white",command=
lambda:updateChoice("scissor"))
button_scissor.place(x=671,y=600)
win.mainloop()