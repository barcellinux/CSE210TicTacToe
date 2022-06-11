'''
Tic-Tac-Toe
CSE-210 Programming with Classes - Brad Lythgoe
Author: Rafael Barcellos Machado
'''

def main():
  board = [] #creates the board as an empty array
  for i in range(9): #uses a loop to populate the array with numbers from 1 to 9
        board.append(i + 1)
  gameOver = False #sets the gameOver variable to false so that we can play the game 
  while not gameOver: #sets a loop to keep playing while the gameOver variable is not true
    printBoard(board)
    gameOver = checkVictory("O", board)
    if gameOver == True:
      break
    print("Player X, choose a number.")
    turn("X", board)
    
    printBoard(board)
    gameOver = checkVictory("X", board)
    if gameOver == True:
      break
    print("Player O, choose a number.")
    turn("O", board)

def printBoard(board): #This function prints the board
    print()
    print('', board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print('', board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print('', board[6], "|", board[7], "|", board[8])
    print()

def getNumber(): #This function will check if the user's input is a number from 1 to 9
  while True:
    number = input()
    try:
      number  = int(number)
      if number in range(1, 10):
        return number
      else:
        print("\nThat number is not on the board.")
    except ValueError:
      print("\nThat's not a number. Try again.")
      continue

def turn(player, board): #this function is repeated each turn to replace a number on the board with X or O and checks if the input number has already been chosen
  chosenNumber = getNumber() - 1
  if board[chosenNumber] == "X" or board[chosenNumber] == "O":
    print("\nThis number has already been chosen. Try a different number.")
    printBoard(board)
    turn(player, board)
  else:
    board[chosenNumber] = player

def checkVictory(player, board): #this function checks who won the game
  magicBox = [4, 9, 2, 3, 5, 7, 8, 1, 6] #This array will be used to calculate who won the game  
  turns = 0
  for x in range(9):
    for y in range(9):
      for z in range(9):
        if x != y and y != z and z != x:
          if board[x] == player and board[y] == player and board[z] == player:
            if magicBox[x] + magicBox[y] + magicBox[z] == 15:
              print("Player", player ,"has won!\n")
              return True
  for a in range(9):
     if board[a] == "X" or board[a] == "O":
       turns += 1
     if turns == 9:
       print("It's a draw!\n")
       return True

main()