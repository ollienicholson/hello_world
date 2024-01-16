# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    result = []
    
    for i, char in enumerate(s):
        # Create the repeated part of the string
        repeated_part = char.upper() + char.lower() * i
        result.append(repeated_part)
    
    # Join the parts with hyphens and return
    return '-'.join(result)

