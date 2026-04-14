#Interview Question: Given a string, find the length of the longest substring without repeating characters.

def non_repeat(s):
    seen=set()
    l=0
    res=0
    for r in range(len(s)):
        while s[r] in seen:
            print('s[l]',s[l])
            seen.remove(s[l])
            l+=1
            print('remove seen----',seen)
            print('while left valueee',l)
        seen.add(s[r])
        print('add seen+++',seen)
        res=max(res,r-l+1)
        print('res=',res)
    return res
s="aabcb"
non_repeat(s)

#Time complexity: O(n) where n is the length of the string. We traverse the string once with the right pointer and in the worst case, we may traverse it again with the left pointer.
#Space complexity: O(min(m,n)) where m is the size of the character set and n is the length of the string. In the worst case, if all characters in the string are unique, we will store all characters in the set, resulting in O(n) space complexity. However, if the character set is limited (e.g., only lowercase letters), the space complexity can be considered O(1).