board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def display_board():
    print("\n")
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

Player = "X"

x = 0

def playcheck():
   global Player
   if x % 2 == 0:
        Player = "O"
   else:
        Player = "X"



while True:
   playcheck()
   display_board()
   t = input(f"{Player}'s Turn: ")
   y = int(t) - 1
   board[y] = f"{Player}"
   x += 1
