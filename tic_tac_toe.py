#starting
#print('Hello world!')

#to simulate needing a short period of time to process
import time

#####let us set some variables#####
###################################

#player icons
global p1_icon
global p2_icon
p1_icon = ""
p2_icon = ""

#player names
global p1_name
global p2_name
p1_name = "Player 1"
p2_name = "Player 2"

#while loop variables
global keepGoing
keepGoing = True
global keepGoingNextGame
keepGoingNextGame = True
global anotherRound
anotherRound = True


######let us set some lists#####
################################

#loading the list which will hold the contents of the game going forward
initial_board_contents = [1,2,3,4,5,6,7,8,9]

#separating the board variables for easier board initialization
board_contents = initial_board_contents.copy()

#Winning combinations, the set (if spaces are equal to the same player icon)
# of all possible winning board sets
win_states = [[0,4,8],[0,1,2],[3,4,5],[6,7,8]
,[0,3,6],[1,4,7],[2,5,8],[2,4,6]]

#list of acceptables answers to playing another game (at end of the code)
next_game_options = ["yes","y","Y","Yes","YES","no","n","N","No","NO"]

#setting acceptable icon list
acceptable_icons = ["X","O"]

#setting the variable to determine who is up
batter_up = 0
#and a list to iterate through to deliver the proper name and game piece to the board
#player_info = [[p1_name,p1_icon],[p2_name,p2_icon]]


#initializing the board -- setting a numerical board using the board_contents list
#which will be updated as we play the game
def board_print():
    print('\nHere is the current game board!')
    for i in range(3):
        print('      -------------')
        print('row:'+str(i+1),end="")
        for j in range(3):
            print(' |',board_contents[(i*3)+(j)], end = "")
        print(' |', end ="")
        print()
    print('      -------------')


#setting player 1's icon & name
def set_p1():
    global p1_icon
    global p1_name
    p1_name = input('Player 1, what is your name? ')
    for i in range(3):
        p1_icon = input(p1_name+', would you like to be "X"s or "O"s? (Capital "X" & "O" only please) ')
        if p1_icon in acceptable_icons:
            break
        else:
            print(p1_name+' you have ' + str(2-i) + ' chances left to choose')

    #displaying the player 1 icon
    if p1_icon in acceptable_icons:
        print(p1_name+', your icon is ' + p1_icon)
    #and if the player hasn't successfully chosen, 'X' is chosen for them
    else:
        p1_icon = "X"
        print(p1_name+', your icon is',p1_icon)

def set_p2():
    global p2_icon
    global p2_name
    p2_name = input('Player 2, what is your name? ')

    #determining player 2's icon based on being the opposite of the
    #index of player 1's icon
    p2_icon = acceptable_icons[1-acceptable_icons.index(p1_icon)]

    #displaying player 2's icon
    print(p2_name+', your icon is',p2_icon)


def p1_move():
    p1keepGoing = True
    while p1keepGoing:
        while True:
            move = input(p1_name+' what is your move? (1-9) ')
            try: #checking if player 1's move is an integer
                move = int(move)
                break
            except ValueError:
                print('Your answer is not a number 1-9, please enter a number 1-9\n') 
        if move in board_contents: #if the variable move is in the set of the game board
            board_contents[move-1] = p1_icon #then convert the move into an index
            #by subtracting 1 & then set the player icon to the indexed space in "board_contents"
            p1keepGoing = False
        elif board_contents[move-1] in acceptable_icons: #if the space already has an X or O
            print('That space is taken, please choose again\n')
        elif move not in board_contents: #if the user enters an input not in the game board options
            print('Your input is not an option on the game board, please choose again\n')
        
#this function is not currently as updated as p1_move
#and will crash with non integer answers
def p2_move(): #for comments, see "p1_move()" function comments
    move = int(input(p2_name+' what is your move? (1-9) '))
    if move in board_contents:
        board_contents[move-1] = p2_icon
    elif move not in board_contents: #if the user enters an input not in the game board options
        print('Your input is not an option on the game board')
        p2_move()
    elif board_contents[move-1] in acceptable_icons:
        print('that space is taken')
        p2_move()


#checking if the board has reached a win state
def check_winner():
    #cycling through the compiling of indices that would indicate a win state
    #and checking if the current board is in any of those states
    for i in range(len(win_states)):
        if board_contents[win_states[i][0]] == \
        board_contents[win_states[i][1]] == board_contents[win_states[i][2]]:
            print('winner!')  #handsomely reward the winner if so
            print('winner!')
            print('winner!')
            global keepGoing
            keepGoing = False #and end the loop, to end the current game.

#initial game setup.
#[establishing a new board, welcoming, setting players, & printing board]
def game_setup():
    global board_contents
    board_contents = initial_board_contents.copy()
    print('\n-#-#--#-#--#-#--#-#--#-#-\nHello and welcome to Tic Tac Toe Deluxe\n')
    set_p1()
    set_p2()
    global player_info
    player_info = [[p1_name,p1_icon],[p2_name,p2_icon]]
    board_print()

#checking if the user wants to play again after a full completed round
def lets_play_again():
    while anotherRound:
        global newGame
        newGame = input('Do you want to play another game? (Please answer with "Yes" or "No") ')
        if newGame in next_game_options:
            break
        else:
            print('Please enter either "Yes" or "No"\n')
    if newGame in next_game_options[0:5]: #did the user enter yes of some form?
        keepGoingNextGame = True
        global keepGoing
        keepGoing = True        
    elif newGame in next_game_options[5:]: #did the user enter no of some form?
        keepGoingNextGame = False
        print('\nThanks for playing, have a great day!\n\n') #outgoing notes
        time.sleep(.5)
        print('ending...\n')
        time.sleep(.8)
        print('See you next time\nGoodbye!\n')

#uncomment this function to run current test
#testcenter()
#print('\n[now passed the testcenter() function; now entering, "#main"]')

###############################################################
#####Attempting to replace the p1_move & p2_move functions#####
###############################################################
#Building a general/non specific player move function
def player_move():
    global player_info
    global batter_up
    playerKeepGoing = True
    while playerKeepGoing:
        while True:
            #global batter_up
            move = input(player_info[batter_up][0]+' what is your move? (1-9) ')
            try:
                move = int(move)
                break
            except ValueError:
                print('Your answer is not a number 1-9, please enter a number 1-9\n') 
        if move in board_contents: #if the variable move is in the set of the game board
            board_contents[move-1] = player_info[batter_up][1] #then convert the move into an index #
            #by subtracting 1 & then set the player icon to the indexed space in "board_contents"
            playerKeepGoing = False
            board_print()
            check_winner()
            if batter_up == 0:
                batter_up = 1
            elif batter_up == 1:
                batter_up = 0
        elif board_contents[move-1] in acceptable_icons: #if the space already has an X or O
            print('That space is taken, please choose again\n')
        elif move not in board_contents: #if the user enters an input not in the game board options
            print('Your input is not an option on the game board, please choose again\n')
###############################################################
###############################################################



################################################################################
#main#
################################################################################
while keepGoingNextGame:
    game_setup()
    while keepGoing:
        #p1_move()
        #board_print()
        #check_winner()
        player_move() #comment out this and uncomment the others in this while loop to get back to normal
        if keepGoing is False:
            print('Congratulations',p1_name+'!\n')
            break
        
        #p2_move()
        #board_print()
        #check_winner()
        #if keepGoing is False:
            #print('Congratulations',p2_name+'!\n')
    lets_play_again()


###############################################################
#THIS IS A TESTING CENTER
def testcenter():
    set_p1()
    set_p2()
    board_print()

    player_move()
    print('first move passed')
    board_print()
    player_move()
    print('second move passed')
    board_print()
    player_move()
    player_move()
    player_move()
    player_move()
    player_move()
    print('seventh move passed, success')
    board_print()
    check_winner()

    print('last fullgame test line')
    #p1_move()
    #board_print()
    #check_winner()

    #p1_move()
    #board_print()
    #check_winner()

    #p1_move()
    #board_print()
    #check_winner()
###############################################################