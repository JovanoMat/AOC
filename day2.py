# get input via file and save as string
file = open("day2input.txt", "r");
allMoves = file.read();
file.close()

# define needed variables, which save if the move is mine (true/false), mine and my opponents moves and my total score
myScore = 0;
myGo = False;
oppMove = " ";
myMove = " ";

# define nice to have variables
roundCounter = 0;
drawCounter = 0;
winCounter = 0;
loseCounter = 0;
# check all moves 
for move in allMoves:
    # skip all whitespaces and newliens
    if move == "\n" or move == " ":
        continue;
    # if its not my go, assign the move to the opponent and set mygo to true
    elif myGo == False:
        oppMove = move;
        myGo = True;
    else:
    # if its my move assign the move to my move, since its my move, it means one round ended, so the result can be calculated 
        roundCounter += 1;
        myMove = move;


        # first get my guaranteed points
        if myMove == "X":
            myScore += 1
        elif myMove == "Y":
            myScore += 2
        elif myMove == "Z":
            myScore += 3

        # get additional points by checking if it was a draw
        if oppMove == "A" and myMove == "X" or oppMove == "B" and myMove == "Y" or oppMove == "C" and myMove == "Z":
            myScore += 3;
            drawCounter += 1;
        # a loss
        elif oppMove == "A" and myMove == "Z" or oppMove == "B" and myMove == "X" or oppMove == "C" and myMove == "Y":
            myScore += 0;
            loseCounter += 1;
        # or a win
        else:
            myScore += 6;
            winCounter += 1;
        
        # set myGo to false for next round to begin
        myGo = False;

print("First strategy:")
print("I ended up with a total of", myScore, "points!", "I played", roundCounter, "rounds, of which I won", winCounter, "times, lost", loseCounter, "times and drew", drawCounter, "times!");


# Second strategy
print(" ")
print("Second strategy:")	


# reset all variables
roundCounter = 0;
drawCounter = 0;
winCounter = 0;
loseCounter = 0;

myScore = 0;

# check all moves 
for move in allMoves:
    # skip all whitespaces and newliens
    if move == "\n" or move == " ":
        continue;
    # if its not my go, assign the move to the opponent and set mygo to true
    elif myGo == False:
        oppMove = move;
        myGo = True;
    else:
    # if its my move assign the move to my move, since its my move, it means one round ended, so the result can be calculated 
        roundCounter += 1;
        myMove = move;

        # if I need to lose
        if myMove == "X":
            # find out whick move I have to play in order to lose
            if oppMove == "A":
                myMove = "Z";
            elif oppMove == "B":
                myMove = "X";
            else: 
                myMove = "Y";

            # my points by losing
            loseCounter += 1;
            myScore += 0;

        # if I need to draw
        elif myMove == "Y":
            if oppMove == "A":
                myMove = "X";
            elif oppMove == "B":
                myMove = "Y";
            else: 
                myMove = "Z";
        
            # my points my drawing
            drawCounter += 1;
            myScore += 3;

        # if I need to win
        elif myMove == "Z":
            if oppMove == "A":
                myMove = "Y";
            elif oppMove == "B":
                myMove = "Z";
            else: 
                myMove = "X";
        
            # my points my winning
            winCounter += 1;
            myScore += 6;


        # get additional guaranteed points
        if myMove == "X":
            myScore += 1
        elif myMove == "Y":
            myScore += 2
        elif myMove == "Z":
            myScore += 3

        
        # set myGo to false for next round to begin
        myGo = False;

print("I ended up with a total of", myScore, "points!", "I played", roundCounter, "rounds, of which I won", winCounter, "times, lost", loseCounter, "times and drew", drawCounter, "times!");


