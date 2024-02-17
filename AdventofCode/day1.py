# min 50 starrs by dec 25


# Assume commands.txt contains Python commands
val = 0
all_counts = []
with open('codes.txt', 'r') as file:
    for line in file:
        if line != '\n':
            val += int(line)
        else:
            all_counts.append(val)
            val = 0
            
all_counts.sort(reverse=True)

final = all_counts[:3]

sum = 0
for i in final:
    sum += i
# part one answer 67027

print(sum)