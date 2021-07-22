def display_board():
    print('''
    TIC TAC TOE
    *************************
    *   {}   |   {}   |   {}   *
    *  _ _ _| _ _ _ | _ _ _ *
    *   {}   |   {}   |   {}   *  
    *  _ _ _| _ _ _ | _ _ _ *
    *       |       |       *
    *   {}   |   {}   |   {}   * 
    *************************

    '''.format(*positions))

def player_input(player):
    column = input("which column: ")
    row = input("which row: ")
    if player == "one":
        thing = "x"
    else:
        thing = "O" 
    if column == "1" and row == "1" :
        if already_there(0,player) != 0:
            return player_input(player)
        positions[0] = thing   
    elif column == "2" and row == "1" :
        if already_there(1,player) != 0:
            return player_input(player)
        positions[1] = thing  
    elif column == "3" and row == "1" :
        if already_there(2,player) != 0:
            return player_input(player)
        positions[2] = thing  
    elif column == "1" and row == "2" :
        if already_there(3,player) != 0:
            return player_input(player)
        positions[3] = thing  
    elif column == "2" and row == "2" :
        if already_there(4,player) != 0:
            return player_input(player)
        positions[4] = thing  
    elif column == "3" and row == "2" :
        if already_there(5,player) != 0:
            return player_input(player)
        positions[5] = thing  
    elif column == "1" and row == "3" :
        if already_there(6,player) != 0:
            return player_input(player)
        positions[6] = thing  
    elif column == "2" and row == "3" :
        if already_there(7,player) != 0:
            return player_input(player)
        positions[7] = thing  
    elif column == "3" and row == "3" :
        if already_there(8,player) != 0:
            return player_input(player)
        positions[8] = thing 
    # display_board() 

def check_win():
    if (positions[0] == positions[1] == positions[2]) and positions[0] != " ":
        print("you have won")
        return True
    elif positions[3] == positions[4] == positions[5]and positions[3] != " ":
        print("you have won")
        return True
    elif positions[6] == positions[7] == positions[8]and positions[6] != " ":
        print("you have won")
        return True
    elif positions[0] == positions[3] == positions[6]and positions[3] != " ":
        print("you have won")
        return True
    elif positions[1] == positions[4] == positions[7]and positions[1] != " ":
        print("you have won")
        return True
    elif positions[3] == positions[4] == positions[5]and positions[3] != " ":
        print("you have won")
        return True
    elif positions[2] == positions[5] == positions[8]and positions[2] != " ":
        print("you have won")
        return True
    elif positions[0] == positions[4] == positions[8]and positions[0] != " ":
        print("you have won")
        return True
    elif positions[2] == positions[4] == positions[6]and positions[2] != " ":
        print("you have won")
        return True
    else:
        for word in positions:
            if word == " ":
                break
        else:
            print("tie game!")
            return True
           
def already_there(i,player):
    if positions[i] == "x" or positions[i] == "O":
        print('space already taken')
        return 1
    else:
        return 0   

def play():
    count = 0
    while True:
       display_board()
       if check_win():
           break
       if count % 2 == 0:
           print("player one, your turn: ")
           player_input("one")
           count+=1
       else:
           print("player two, your turn: ")
           player_input("two")
           count+=1  

positions = [" ", " "," ", " "," "," "," "," "," " ]
i = 0
play()