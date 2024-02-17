# day 2 2023 advent of code

max_values = {"red": 12, "green": 13, "blue": 14}

count = 1

RED = int(12)
GREEN = int(13)
BLUE = int(14)

sum_ids = 0

with open('games.txt', 'r') as file:
    for line in file:
        # split game ID from collection of numbers
        split_line = line.strip().split(":")

        # returns only the collection of numbers
        numbers = split_line[1]
        
        games = numbers.split(";")
        
        print("games: ", games)
        
        green_valid = True
        blue_valid = True
        red_valid = True
        
        colour = ""
        min_values = {}
        # iterate through each row of games and return each hand
        for hand_1 in games:
            hand_1 = hand_1.split(", ")
            
            print("hands:", hand_1)
            for item in hand_1:
                value, colour = item.strip().split(" ")
                
                # convert value to integer
                value = int(value)
                
                # get the min value for each colour for each game
                
                # update the mininum value for the current color in the dictionary
                if colour not in min_values or count < min_values[colour]:
                    min_values[colour] = count
                
                        
                if colour == "red" and value > 12:
                    red_valid = False
                if colour == "blue" and value > 14:
                    blue_valid = False
                if colour == "green" and value > 13:
                    green_valid = False        
                    
                
        if red_valid and blue_valid and green_valid == True:
            sum_ids += count
            print("CORRECT")
        else:
            print("NOT")
             
            
        count += 1
        print("Count:", count)
        print("Sum ids", sum_ids)
        
