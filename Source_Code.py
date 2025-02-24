player_again = "Y"   #This 	variable puts our program in while loop.
playing_field = 1    #This variable allows our program to enter a while loop that checks the size of the field.
playing_area = [3,5,7] 
start_game = 0      #This variable allows the game to continue until one of the players wins.      
area = []

def area_for_all(field):
    index_num = field*2 + 3
    for i in range(index_num):
        tempora_area = [""] * (index_num)
        area.append(tempora_area)
    #It creates two dimensional lists for our playing field.
    underscore = {0:"  _",1 :"__",2:"_",3:"___",4:"_",5:"___",6:"_",7:"___",8:"_",9:"___",10:"_",11:"___",12:"_",13:"___",14:"_",15:"________",16:"_ "}
    abc = {0:"-",1:"- ",2:" A",3:" - ",4:" B ",5:" - ",6:" C ",7:" - ",8:"D",9:" - ",10:"  E",11:" - ",12:" F ",13:" - ",14:"G ",15:" -",16:"- "}
    matrix = {1:" | ",2:"",3:"  |  ",4:"",5:"  |  ",6:"",7:"  |  ",8:"",9:"  |  ",10:"",11:"  |  ",12:"",13:"  |  ",14:"",15:"  |"}
    #It creates the empty appearance of our playing field.
    for y in range(index_num):
        if y == 0:
            for x in range(index_num):
                if x == index_num-1:
                    area[y][x] = abc[16]
                else:
                    area[y][x] = abc[x]
        elif y == index_num-1:
            for x in range(index_num):
                if x == index_num-1:
                    area[y][x] = abc[16]
                else:
                    area[y][x] = abc[x]
            
        elif y % 2 == 0:
            for x in range(index_num):
                if x == index_num-1:
                    area[y][x] = y//2
                elif x == 0 :
                    area[y][x] = y//2
                else:
                    area[y][x] = matrix[x]
        else:
            for x in range(index_num):
                if x == index_num-1:
                    area[y][x] = underscore[16]
                else:
                    area[y][x] = underscore[x]
    #It creates the first image of the playing field.
    return area, index_num

def area_show(area,index_num):      #This function reads the playing field from the list and prints it on the screen
    for y in range (index_num):
        print("\n")
        for x in range(index_num):
            print(area[y][x],end="")

def contin():    #This function asks players if they want to continue or end the game.
    player_again = input("Would you like to play again(Y/N)?: ")
    while player_again not in ["Y","N"]:
        player_again = input("Can you write correct format(Y/N): ")
    return player_again

def playing_field_supervisor(playing_field,playing_area):    #This function checks whether the size of the playing    
    while playing_field not in playing_area :                #field has been entered correctly
        try:  
            playing_field = int(input("Enter the row/column number of the playing field (3, 5, 7): "))
        except ValueError:  
              playing_field = int(input("Please enter only numbers: "))
    return playing_field

def character_supervisor() :    #This function checks if the player names have been entered correctly.
    user_symbol = input("Enter a capital letter to represent player (except O):")
    user_symbol1 = user_symbol.upper()
    while not(user_symbol1 in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"] ):
        user_symbol = input("Enter a capital letter to represent player (except O):")
        user_symbol1 = user_symbol.upper()
    return user_symbol1

def direction_supervisor(a):     #This function checks whether the big stone have the correct direction.
    directions = input(f"Player {a}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ")
    direction = directions.upper()
    while not (direction  in ("N","S","E","W","NE","NW","SE","SW")) :
        directions = input("Please enter the correct direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ")
        direction = directions.upper()
    return direction

def direction(player,first_x,first_y):
    directions = direction_supervisor(player)   #It allows us to find the coordinate of the place where the player wants to go. 
    if directions =="N":
        first_x += 0
        first_y -= 2
    elif directions =="S":
        first_x += 0
        first_y += 2
    elif directions =="E":
        first_x += 2
        first_y += 0
    elif directions =="W":
        first_x -= 2
        first_y -= 0
    elif directions =="NE":
        first_x += 2
        first_y -= 2
    elif directions =="NW":
        first_x -= 2
        first_y -= 2
    elif directions =="SE":
        first_x += 2
        first_y += 2
    else:
        first_x -= 2
        first_y += 2
    return first_x,first_y,directions

def reverse_direction(directions,first_x,first_y):      #It finds the old coordinates of the big stone.
    if directions =="N":
        first_x += 0
        first_y += 2
    elif directions =="S":
        first_x += 0
        first_y -= 2
    elif directions =="E":
        first_x -= 2
        first_y += 0
    elif directions =="W":
        first_x += 2
        first_y -= 0
    elif directions =="NE":
        first_x -= 2
        first_y += 2
    elif directions =="NW":
        first_x += 2
        first_y += 2
    elif directions =="SE":
        first_x -= 2
        first_y -= 2
    else:
        first_x += 2
        first_y -= 2
    
    return first_x,first_y

def environment(y,x):    #This function checks whether there is space around the big stone and change the value of the win variable if there is no space.
    if area[y-2][x] !="" and area[y+2][x] !="" and area[y][x+2]!="" and area[y][x-2]!="" and area[y-2][x+2]!="" and area[y-2][x-2]!="" and area[y+2][x+2]!="" and area[y+2][x-2]!="" :
        win = 1
    else:
        win = 0
    return win

def small_ston(player1,area,index_num):  #This function allows us to place the small stone on the playing field
    small_stone_flag = 1
    while small_stone_flag == 1 :     
        small_stone = "2zw"
        location_letter = "ABCDEFG"
        location_num = "1234567"
        while not (len(small_stone) == 2 and small_stone[0] in location_num):   #It allows the player to make the right move.
            small_stone = input(f"Player {player1}, please enter the location where you want to place a small stone (like 1A):")
            if len(small_stone) == 2 and small_stone[1] in location_letter and small_stone[0] in location_num:
                small_stone1 = small_stone[1].upper()
                break
        small_stone1 = small_stone[1].upper()   
        index_number = location_letter.find(small_stone1)
        if area[int(small_stone[0])*2][int(index_number)*2+2] == "" :  #If the place where he chooses is empty, It allows to place the small stone.
            area[int(small_stone[0])*2][int(index_number)*2+2] = "O"
            small_stone_flag = 0
    area_show(area,index_num)

def player(first_x,first_y,player1):            
    flag = True
    while flag == True :
        last_x , last_y, directions = direction(player1,first_x,first_y)
        if area[last_y][last_x] == "":      #It asks if the place where the big stone wants to go is empty.
            area[last_y][last_x] = player1
            area[first_y][first_x] = ""     #It allows the old place to become empty
            area_show(area,index_num)
            small_ston(player1,area,index_num)
            break
        else:
            last_x , last_y = reverse_direction(directions,first_x,first_y)
    return last_x ,last_y

first_player = character_supervisor()       #Players are asked for input on the name of the big stone.
second_player = character_supervisor()      #Players are asked for input on the name of the big stone.
while first_player ==  second_player :
    print("Enter a capital letter to represent player (except O and first player letter):")
    second_player = character_supervisor()

while player_again != "N":
      
    field = playing_field_supervisor(playing_field,playing_area)
    if field == 3 :
        area, index_num = area_for_all(field)
        area[2][4] = first_player
        area[6][4] = second_player
        f_x = 4         #f_x = holds the index value of the first player's big stone on the x-axis.
        f_y = 2         #f_y = holds the index value of the first player's big stone on the y-axis.
        s_x = 4         #s_x  =holds the index value of the second player's big stone on the x-axis.
        s_y = 6         #s_y = holds the index value of the second player's big stone on the y-axis.
    elif field == 5 :
        area ,index_num = area_for_all(field)
        area[2][6] = first_player
        area[10][6] = second_player
        f_x = 6
        f_y = 2
        s_x = 6
        s_y = 10
    else :
        area , index_num = area_for_all(field)
        area[2][8] = first_player
        area[14][8] = second_player
        f_x = 8
        f_y = 2
        s_x = 8
        s_y = 14
    area_show(area,index_num)

    while start_game == 0:      #It allows players to make moves until one of them wins.
        win = environment(f_y,f_x)
        if win == 1:        #Players are checked before playing to make sure they are not surrounded by empty space.
            print("Second player won the game.")
            break
        else:
            last_x ,last_y = player(f_x,f_y,first_player)
            f_x = last_x
            f_y = last_y
        win = environment(s_y,s_x)
        if win == 1:
            print("First player won the game.")
            break
        else:
            last_x , last_y = player(s_x,s_y,second_player)
            s_y = last_y
            s_x = last_x
    area = []       #It resets the map in case players continue the game.
    player_again = contin()




























