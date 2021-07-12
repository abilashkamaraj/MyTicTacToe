from tkinter import *
import tkinter.font as font
import tkinter.messagebox as msg
from PIL import ImageTk, Image
import random

player1_marker,player2_marker,turn='','',''
board=[' ']*10

def space_check(btnumber):
    global board
    return board[btnumber]==' '

def full_board_check():
    global board
    for i in range(1,10):
        if space_check(i):
            return False
    return True

def win_check(marker):
    global board
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

def place_marker(btnumber,marker):
    if space_check(btnumber):
        if btnumber==1:
            board[btnumber]=marker
            button1.config(text=marker)
            return True
        elif btnumber==2:
            board[btnumber]=marker
            button2.config(text=marker)
            return True
        elif btnumber==3:
            board[btnumber]=marker
            button3.config(text=marker)
            return True
        elif btnumber==4:
            board[btnumber]=marker
            button4.config(text=marker)
            return True
        elif btnumber==5:
            board[btnumber]=marker
            button5.config(text=marker)
            return True
        elif btnumber==6:
            board[btnumber]=marker
            button6.config(text=marker)
            return True
        elif btnumber==7:
            board[btnumber]=marker
            button7.config(text=marker)
            return True
        elif btnumber==8:
            board[btnumber]=marker
            button8.config(text=marker)
            return True
        elif btnumber==9:
            board[btnumber]=marker
            button9.config(text=marker)
            return True
    else:
        return False

def game_on(btnumber):
    global turn,player1_marker,player2_marker
    if turn=="Player1":
        if place_marker(btnumber,player1_marker):
            if win_check(player1_marker):
                msg.showinfo("Result","Player 1 wins")
                ask_replay()
            else:
                if full_board_check():
                    msg.showinfo("Result","Match Draw")
                    ask_replay()
                else:
                    turn="Player2"
                    turnIndicator.set(turn+"'s"+" turn")
                    
    else:
        if place_marker(btnumber,player2_marker):
            if win_check(player2_marker):
                msg.showinfo("Result","Player 2 wins")
                ask_replay()
            else:
                if full_board_check():
                    msg.showinfo("Result","Match Draw")
                    ask_replay()
                else:
                    turn="Player1"
                    turnIndicator.set(turn+"'s"+" turn")
            
            
def display_board():
    lbl.pack_forget()
    frame1.pack_forget()
    frame2.pack()
    player1_label.config(text="Player 1:"+player1_marker)
    player2_label.config(text="Player 2:"+player2_marker)
    player1_label.grid(row=0,column=0)
    player2_label.grid(row=0,column=1)
    frame3.pack()
    frame4.pack()

def set_marker(player,marker):
    global player1_marker,player2_marker
    if player==1 and marker=='X':
        player1_marker='X'
        player2_marker='O'
    elif player==1 and marker=='O':
        player1_marker='O'
        player2_marker='X'
    elif player==2 and marker=='X':
        player2_marker='X'
        player1_marker='O'
    elif player==2 and marker=='O':
        player2_marker='O'
        player1_marker='X'
    display_board()

def player_choose():
    global turn
    startbtn.pack_forget()
    gameImg.pack_forget()
    lbl.pack()
    player=random.randint(1,2)
    if player==1:
        lbl.config(text="Player 1 choose the marker; Player 1 goes first")
        turn='Player1'
        turnIndicator.set(turn+"'s"+" turn")
    else:
        lbl.config(text="Player 2 choose the marker; Player 2 goes first")
        turn='Player2'
        turnIndicator.set(turn+"'s"+" turn")
    frame1.pack()
    Xbutton=Button(frame1,text="X",height=10,width=10,fg='red',bd=5,command=lambda:set_marker(player,'X'))
    Obutton=Button(frame1,text="O",height=10,width=10,fg='green',bd=5,command=lambda:set_marker(player,'O'))
    myFont = font.Font(family='Courier', size=20, weight='bold')
    Xbutton['font']=myFont
    Obutton['font']=myFont
    Xbutton.grid(row=0,column=0)
    Obutton.grid(row=0,column=1)

def reconfigButtons():
    button1.config(text='')
    button2.config(text='')
    button3.config(text='')
    button4.config(text='')
    button5.config(text='')
    button6.config(text='')
    button7.config(text='')
    button8.config(text='')
    button9.config(text='')

def ask_replay():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    replaylbl.pack()
    yesButton.pack(pady=5)
    noButton.pack(pady=5)

def replay(choice):
    global board
    global player1_marker,player2_marker,turn
    if choice=='yes':
        replaylbl.pack_forget()
        yesButton.pack_forget()
        noButton.pack_forget()
        board=[' ']*10
        player1_marker,player2_marker,turn='','',''
        reconfigButtons()
        startbtn.pack()
        gameImg.pack()
    else:
        root.destroy()


if __name__=="__main__":
    root = Tk()
    root.title('Tic Tac Toe')
    root.geometry('500x500')
    root.resizable(False,False)
    root.iconbitmap(r'icon.ico')
    Label(root, text='Welcome to Tic Tac Toe',padx=10,pady=20, fg='red',font=("Arial bold",20)).pack()
    startbtn = Button(root,text="start the game",command=player_choose,fg="green",bg="black",pady=10)
    myFont = font.Font(family='Courier', size=20, weight='bold')
    startbtn['font']=myFont
    startbtn.pack()
    img = ImageTk.PhotoImage(Image.open("picture1.png"))
    gameImg = Label(root,image=img)
    gameImg.pack(pady=20)
    lbl = Label(root,fg='green',font=('Helvetica',15),pady=20)
    frame1 = Frame(root)
    frame2 = Frame(root)
    player1_label = Label(frame2,font="times 15",padx=10)
    player2_label = Label(frame2,font="times 15",padx=10)
    frame3 = Frame(root,highlightbackground = "black", highlightthickness = 2,)
    
    button1=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(1))
    button1.grid(row=2,column=0)
    
    button2=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(2))
    button2.grid(row=2,column=1)

    button3=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(3))
    button3.grid(row=2,column=2)
    
    button4=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(4))
    button4.grid(row=1,column=0)
    
    button5=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(5))
    button5.grid(row=1,column=1)
    
    button6=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(6))
    button6.grid(row=1,column=2)
    
    button7=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(7))
    button7.grid(row=0,column=0)
    
    button8=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(8))
    button8.grid(row=0,column=1)
    
    button9=Button(frame3,width=8,height=4,font=('Times 16 bold'),command=lambda:game_on(9))
    button9.grid(row=0,column=2)

    frame4=Frame(root)
    turnIndicator=StringVar()
    turnIndicatorlbl=Label(frame4,bg="black",fg="white",font=('Times 15 bold'),textvariable=turnIndicator)
    turnIndicatorlbl.pack()

    replaylbl=Label(root,font=('Helvetica',15),fg='blue',pady=20,text="Do you want to continue?")
    yesButton=Button(root,text="YES",width=10,fg='green',bd=5,command=lambda:replay('yes'))
    noButton=Button(root,text="NO",width=10,fg='red',bd=5,command=lambda:replay('no'))
    
    root.mainloop()
