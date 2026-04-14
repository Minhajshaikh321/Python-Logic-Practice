#Interview Question: Given a string, reverse the order of words in the string while maintaining the relative order of the characters within each word.
def reverse_string(s):
    st=" ".join(s.split()[::-1])
    return st

s = "the sky is blue"
print(reverse_string(s))

#Time complexity: O(n) where n is the length of the string. We split the string into words, reverse the list of words, and then join them back together, which all take linear time.