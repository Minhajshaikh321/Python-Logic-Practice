#Leetcode Question: 1047. Remove All Adjacent Duplicates In String
def remove_adjacent_duplicate(st):
    stack=[]
    for char in st:
        if stack and stack[-1]==char:
            stack.pop()  # remove last char
        else:
            stack.append(char)  # add char to stack
    return ''.join(stack)  # convert stack to string
print(remove_adjacent_duplicate("abbaca"))  # Output: "ca"