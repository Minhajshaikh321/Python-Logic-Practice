word1="abc"
word2="pqrs"
w3=[]
i=0
while i<len(word1) or i<len(word2):
    if i<len(word1):
        w3.append(word1[i])
    if i<len(word2):
        w3.append(word2[i])
    i+=1
print("".join(w3))