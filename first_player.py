# Library imports
import socket
from tkinter import messagebox, Label, Tk, Button
from _thread import start_new_thread

# An object from the socket library
first_player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The host and port that the second player will use to connect
host = "127.0.0.1"
port = 8080

# Binding the host and port and setting a listening limit
first_player_socket.bind((host, port))
first_player_socket.listen(5)

# An instance of the tkinter library to implement the gui
window = Tk()
window.title("Tic Tac Toe: First Player")
window.geometry("350x100")

# Labeling for clarifying
label = Label(window, text="Tic-Tac-Toe Game", font=("sans-serif", 20))
label.grid(row=0, column=0)

firstLabel = Label(window, text="Player1: X", font=("sans-serif", 15))
firstLabel.grid(row=1, column=0)

secondLabel = Label(window, text="Player2: O", font=("sans-serif", 15))
secondLabel.grid(row=2, column=0)

# This turn value is to keep track of whose turn it is
# From firstClick function to ninthClick function they're all functions handling 
# the 9 buttons of our game
turn = True
def firstClick():
    global turn
    if turn == True and firstBtn["text"] == " ":
        firstBtn["text"] = 'X'
        value = '1'
        client.send(value.encode('utf-8'))
        turn = False
        check()

# This is an instanace for creating a button
firstBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=firstClick)
firstBtn.grid(row = 0, column = 1)

def secondClick():
    global turn
    if turn == True and secondBtn["text"] == " ":
        secondBtn["text"] = 'X'
        value = '2'
        client.send(value.encode('utf-8'))
        turn = False
        check()
    

secondBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=secondClick)
secondBtn.grid(row = 0, column = 2)

def thirdClick():
    global turn
    if turn == True and thirdBtn["text"] == " ":
        thirdBtn["text"] = 'X'
        value = '3'
        client.send(value.encode('utf-8'))
        turn = False
        check()
    

thirdBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=thirdClick)
thirdBtn.grid(row = 0, column = 3)

def fourthClick():
    global turn
    if turn == True and fourthBtn["text"] == " ":
        fourthBtn["text"] = 'X'
        value = '4'
        client.send(value.encode('utf-8'))
        turn = False
        check()

fourthBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=fourthClick)
fourthBtn.grid(row = 1, column = 1)

def fifthClick():
    global turn
    if turn == True and fifthBtn["text"] == " ":
        fifthBtn["text"] = 'X'
        value = '5'
        client.send(value.encode('utf-8'))
        turn = False
        check()

fifthBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=fifthClick)
fifthBtn.grid(row = 1, column = 2)

def sixthClick():
    global turn
    if turn == True and sixthBtn["text"] == " ":
        sixthBtn["text"] = 'X'
        value = '6'
        client.send(value.encode('utf-8'))
        turn = False
        check()

sixthBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=sixthClick)
sixthBtn.grid(row = 1, column = 3)

def seventhClick():
    global turn
    if turn == True and seventhBtn["text"] == " ":
        seventhBtn["text"] = 'X'
        value = '7'
        client.send(value.encode('utf-8'))
        turn = False
        check()

seventhBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=seventhClick)
seventhBtn.grid(row = 2, column = 1)

def eighthClick():
    global turn
    if turn == True and eighthBtn["text"] == " ":
        eighthBtn["text"] = 'X'
        value = '8'
        client.send(value.encode('utf-8'))
        turn = False
        check()

eighthBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=eighthClick)
eighthBtn.grid(row = 2, column = 2)

def ninthClick():
    global turn
    if turn == True and ninthBtn["text"] == " ":
        ninthBtn["text"] = 'X'
        value = '9'
        client.send(value.encode('utf-8'))
        turn = False
        check()

ninthBtn = Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=ninthClick)
ninthBtn.grid(row = 2, column = 3)

# This is where i receive the message which consists of a number as a char
# that char indicates which button was clicked from either the first player
# or from the second player, when a player clicks a button the turn value turns the opposite
# that prevents the player playing unless the other player has used his move
def receive_thread(client):
    global turn
    while True:
        # This is the step i get the number that indicates that the other player has clicked a button
        message = client.recv(2048).decode('utf-8')
        if message == '1' and firstBtn["text"] == " ":
            firstBtn["text"] = 'O'
            turn = True
        elif message == '2' and secondBtn["text"] == " ":
            secondBtn["text"] = 'O'
            turn = True
        elif message == '3' and thirdBtn["text"] == " ":
            thirdBtn["text"] = 'O'
            turn = True
        elif message == '4' and fourthBtn["text"] == " ":
            fourthBtn["text"] = 'O'
            turn = True
        elif message == '5' and fifthBtn["text"] == " ":
            fifthBtn["text"] = 'O'
            turn = True
        elif message == '6' and sixthBtn["text"] == " ":
            sixthBtn["text"] = 'O'
            turn = True
        elif message == '7' and seventhBtn["text"] == " ":
            seventhBtn["text"] = 'O'
            turn = True
        elif message == '8' and eighthBtn["text"] == " ":
            eighthBtn["text"] = 'O'
            turn = True
        elif message == '9' and ninthBtn["text"] == " ":
            ninthBtn["text"] = 'O'
            turn = True
        check()

# Here is a flag so that i can kick the players out if they reached 9 moves without having a winner
# the check method is for clarifying whether a player has won or not
flag = 0
def check():
    global flag
    b1 = firstBtn["text"]
    b2 = secondBtn["text"]
    b3 = thirdBtn["text"]
    b4 = fourthBtn["text"]
    b5 = fifthBtn["text"]
    b6 = sixthBtn["text"]
    b7 = seventhBtn["text"]
    b8 = eighthBtn["text"]
    b9 = ninthBtn["text"]

    flag = flag + 1
    winner = 0

    if ((b1 == b2 and b2 == b3 and b1 == 'O') or (b1 == b2 and b2 == b3 and b1 == 'X')):
        winner = 1
        win(b1)
    elif ((b4 == b5 and b5 == b6 and b4 == 'O') or (b4 == b5 and b5 == b6 and b4 == 'X')):
        winner = 1
        win(b4)
    elif ((b7 == b8 and b8 == b9 and b7 == 'O') or (b7 == b8 and b8 == b9 and b7 == 'X')):
        winner = 1
        win(b7)
    elif ((b1 == b4 and b4 == b7 and b1 == 'O') or (b1 == b4 and b4 == b7 and b1 == 'X')):
        winner = 1
        win(b1)
    elif ((b2 == b5 and b5 == b8 and b2 == 'O') or (b2 == b5 and b5 == b8 and b2 == 'X')):
        winner = 1
        win(b2)
    elif ((b3 == b6 and b6 == b9 and b3 == 'O') or (b3 == b6 and b6 == b9 and b3 == 'X')):
        winner = 1
        win(b3)
    elif ((b1 == b5 and b5 == b9 and b1 == 'O') or (b1 == b5 and b5 == b9 and b1 == 'X')):
        winner = 1
        win(b1)
    elif ((b3 == b5 and b5 == b7 and b3 == 'O') or (b3 == b5 and b5 == b7 and b3 == 'X')):
        winner = 1
        win(b3)
    
    if flag == 9 and winner != 1:
        messagebox.showinfo("Dead End!!", "You have reached a dead end where no one can win.")
        window.destroy()
# The function gets the result of the checking from the check function and declares the winner
def win(player):
    if player == 'X':
        playerNumber = 1
    else:
        playerNumber = 2
    messagebox.showinfo(f"CONGRATULATIONS", f"PLAYER{playerNumber}: '{player}'. You have won the game!!")
    window.destroy()

# Socket accept
# Starting a new thread to keep receiving messages
client, address = first_player_socket.accept()
start_new_thread(receive_thread, (client,))

# The last line at our code and its from the tkinter library
window.mainloop()

# The second_player is the same as the first_player, we just changes some simple steps like
# replacing the binding with connecting and replacing the X and O values