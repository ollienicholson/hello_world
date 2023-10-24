# Sort the odd

# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def sort_array(source):
    odd_list = []
    new_list = []
    
    for i, num in enumerate(source):
        if num % 2 != 0:
            odd_list.append(num)
            new_list.append(i)    
            
    odd_list.sort()

    for i, num in zip(new_list, odd_list):
        source[i] = num
    return source
            
print(sort_array(numbers), "this works")

#  -- other options ==

def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

def sort_array(source_array):
    odd = []
    for i in source_array:
        if i % 2 == 1:
            odd.append(i)
    odd.sort()
    x=0
    for j in range(len(source_array)):
        if source_array[j]%2==1:
            source_array[j]=odd[x]
            x+=1
            
    return source_array
