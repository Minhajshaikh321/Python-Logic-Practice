#Leetcode Question: 20. Valid Parentheses   
def valid_parenthisis(s):
    stack=[]
    hashmap = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        print('ch',ch)
        if ch not in hashmap:
            print('stack append',ch)
            stack.append(ch)
            print('Stack',stack)
        else:
            if not stack: 
                print('else stack not')
                return False
            else:
                popped=stack.pop()
                print('popped',popped)
                print('compare ',popped,hashmap[ch])
                if popped!=hashmap[ch]:
                    return False
    return not stack
valid_parenthisis("{)]")
#Time O(n)  