## ======= Think Python: Ch 10: Exercises =======

# === ex 10-1 ===
# write a function:
# function takes a list of lists of integers and adds up the elements from all of the nested lists
# https://github.com/AllenDowney/ThinkPython2/blob/master/code/list_exercises.py

t = [[1, 2], [3], [4, 5, 6]]

numbers_t = 1, 2, 3, 4, 5, 1, 4, 5
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
anagrams = ['listen', 'silent']


def nested_sum(t):
    total = 0
    for item in t:
        # wrapping item in sum helps iterate through a nested list
        total += sum(item)
    return total


# print(nested_sum(t))


# === ex 10-2 ===
# function calculates cumulative sum of list
def cumulative_sum(t):
    total = 0
    res = []
    for x in t:
        # total = total + x. Words for lists, not for nested lists
        total += x
        res.append(total)
    return res


# print(cumulative_sum(numbers))

# === ex 10-3 ===


def middle(t):
    '''
    This function should return all but the first and last elements of t
    t: list
    returns: new list
    '''
    # return t[:-1] # removes the LAST item in the list, and returns the remaining elements in the list
    # return t[-1] # returns ONLY the last item in the list
    # return t[1]  # returns ONLY index 1
    # return t[0]  # returns ONLY index 0
    return t[
        1:-1
    ]  # start at index 1, finish at index index -2. Returns all but the first and last elements in a list


# print(middle(numbers_t))

# === ex 10-4 ===


def chop(t: list) -> None:
    '''
    Removed the first and last element of t
    
    takes a list
    t: list
    numbers_list: list

    returns: None
    '''
    del t[0]
    del t[-1]


# print(chop(numbers_list)) # returns none
# print(numbers_list) # prints the chopped list

# === ex 10-5 ===


def is_sorted(t: bool) -> bool:
    '''
    Check whether a list is sorted.
    
    t: list
    
    returns: Boolean
    '''
    return t == sorted(t)


# print(is_sorted(t))

# === ex 10-6 ===


def is_anagraam(word1: str or list, word2: str or list) -> bool:
    '''
    Check whether two words are anagrams
    
    word1: string or list
    word2: string or list
    
    returns boolean
    '''
    return sorted(word1) == sorted(word2)


# print(is_anagraam('listen', 'silent'))
# print(is_anagraam('fired', 'fried'))
# print(is_anagraam('sent', 'send'))


def has_duplicates(s: str or list) -> bool:
    '''
    Returns True is any element appears more than once in a sequence
    
    s: string or list
    
    returns: bool
    '''
    # make a copy of t to avoid modiying the parameter
    t = list(s)
    t.sort()

    # check for adjacent elements that are equal
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    # if no duplicates return false
    return False


print(has_duplicates('abbcd'))
print(has_duplicates('abcde'))
