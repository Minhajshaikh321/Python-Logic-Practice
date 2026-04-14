#Interview Question:Given a string, count the number of unique characters in the string.
#  str1="Hello" output=3

def unique_character_str(str1):
    char_count={}
    for i in str1:
        if i not in char_count:
            char_count[i]=1
        else:
            char_count[i]+=1
    unique_count=0
    for value in char_count.values():
        if value==1:
            unique_count+=1
    return unique_count

unique_character_str('Hello')
#Time complexity: O(n) where n is the length of the string. We iterate through the string once to count the characters and then iterate through the character counts to count unique characters.
#Space complexity: O(n) in the worst case, if all characters in the string are unique, we will store each character in the dictionary. In the best case, if all characters are the same, we will only store one character in the dictionary, resulting in O(1) space complexity.