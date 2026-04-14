#Leetcode Question: 125. Valid Palindrome
def valid_pallindrome(s):
    filter_str=""
    for ch in s:
        if ch.isalnum():
            filter_str+=ch.lower()
    return filter_str==filter_str[::-1]
s="A man, a plan, a canal: Panama"  
print(valid_pallindrome(s))

#Time complexity: O(n) where n is the length of the input string. We iterate through the string once to filter out non-alphanumeric characters and convert to lowercase, and then we check if the filtered string is a palindrome, which also takes O(n) time.