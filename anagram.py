str1="Elbow"
str2="Below"
str1=str1.lower()
str2=str2.lower()
if (len(str1)==len(str2)):
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)    
    if (sorted_str1==sorted_str2):
        print(f"{str1} and {str2} are anagram") 
    else:
        print(f"{str1} and {str2} are not anagram")