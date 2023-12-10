sum = 0

with open('day2.txt', 'r') as file:
    for line in file:
        for char in line:
            if char.isnumeric():
                first_num  = char
                break
        for char in reversed(line):
            if char.isnumeric():
                last_num = char
                break
        final = int(first_num + last_num)
        
        sum += final
        
print(sum)
