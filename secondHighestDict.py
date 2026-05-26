d = {"tutor": 3, "tutorials": 15, "point": 9, "tutorialspoint": 19}
def second_highest_dict(d):
    values=list(d.values())
    max1=max(values[0],values[1])
    print(max1)
    max2=min(values[0],values[1])
    print(max2)
    for i in range(2,len(values)):
        if values[i]>max1:
            max2=max1
            max1=values[i]
        elif values[i]>max2:
            max2=values[i]
    return max2

print("Method 1:Second highest number in the dictionary is:", second_highest_dict(d))

def secondHighestDict(d):
    score1=score2=0
    for key in d:
        if d[key]>score1: # if current value is greater than score1, then update score2 to score1 and score1 to current value
            score2=score1
            score1=d[key]
        elif d[key]>score2 and d[key]!=score1: # to handle case when all values are same
            score2=d[key]
    return score2   
print("Method 2:Second highest number in the dictionary is:", secondHighestDict(d))