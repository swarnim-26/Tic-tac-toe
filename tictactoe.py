from tkinter import *
import random

def next_turn(row , column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player== players[0]:
            buttons[row][column]['text']= player
            if check_winner() is False:
                player = players[1]
                label.config(text=(player[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(player[0] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text="It's a Tie!")
        else:
            buttons[row][column]['text']= player
            if check_winner() is False:
                player = players[0]
                label.config(text=(player[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(player[0] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text="It's a Tie!")  

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            buttons[i][0].config(bg="green")
            buttons[i][1].config(bg="green")
            buttons[i][2].config(bg="green")

        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            buttons[0][i].config(bg="green")
            buttons[1][i].config(bg="green")
            buttons[2][i].config(bg="green")    
            return True
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] != "":
            buttons[0][j].config(bg="green")
            buttons[1][j].config(bg="green")
            buttons[2][j].config(bg="green")
            return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True
        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True 
        elif empty_space() is False:
            for i in range(3):
                for j in range(3):
                    buttons[i][j].config(bg="red")
            return "Tie"
        else:
            return False   
def empty_space():
    space=9
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] != "":
                space -= 1

    if space == 0:
        return False     
    else:
        return True
    
def click(row, column):
    next_turn(row, column)
def reset():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="SystemButtonFace")  



window=Tk()
window.title("Tic Tac Toe")
window.geometry("800x800")
players=["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label= Label(text=player + " turn" , font = ("Arial", 20))
label.pack(side=TOP)

reset_button = Button(text="Restart", font=("consolas", 20), command=lambda: reset())
reset_button.pack(side=TOP)

frame= Frame(window)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                               command=lambda row=i, col=j: click(row, col))
        buttons[i][j].grid(row=i, column=j)


window.mainloop()