def str_duplicate(st):
    result=""
    for char in st:
        if char not in result:
            result=result+char
    return result   
print(str_duplicate("programming"))