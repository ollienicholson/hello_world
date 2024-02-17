# from curses.ascii import isdigit
#type:ignore
from sympy import false


num_list = []

previous_line = None
current_line = None
next_line = None

with open("day.txt" , "r") as file:

    

    
    for line in file:

    
        previous_line = current_line
        current_line = next_line
        next_line = line.strip()
        
        if not current_line:
            continue
        

        
        start_index = None
        end_index = None
        for j in range(len(current_line)):
            if current_line[j].isdigit():
                if start_index is None: # not the same as, if not start_index
                    start_index = j
                end_index = j
            else:
                if end_index is not None:
                    number=int(current_line[start_index:end_index+1])
                    for k in range(max(start_index-1,0), min(len(next_line),end_index+2)):
                        if (not next_line[k].isdigit() and next_line[k] != '.') or (previous_line and not previous_line[k].isdigit() and previous_line[k] != '.') or (not current_line[k].isdigit() and current_line[k] != '.'):
                            num_list.append(number)
                            break

                start_index = None
                end_index = None
                
previous_line = current_line
current_line = next_line      
for j in range(len(current_line)):
    if current_line[j].isdigit():
        if start_index is None: # not the same as, if not start_index
            start_index = j
        end_index = j
    else:
        if end_index is not None:
            number=int(current_line[start_index:end_index+1])
            for k in range(max(start_index-1,0), min(len(next_line),end_index+2)):
                if (not next_line[k].isdigit() and next_line[k] != '.') or (previous_line and not previous_line[k].isdigit() and previous_line[k] != '.') or (not current_line[k].isdigit() and current_line[k] != '.'):
                    num_list.append(number)
                    break

        start_index = None
        end_index = None
        

    
print(num_list)
sum = 0
for num in num_list:
    sum += num
print(sum)
        
                    
            
            
                