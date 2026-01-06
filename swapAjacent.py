"""Swap the adjacent element of itarable using function take indexing as a arguments"""

def swap_element(lst,num1,num2):
    try:
        lst[num1], lst[num2] = lst[num2], lst[num1]
        return lst
    except IndexError:
        return "Error: One or both indices are out of range."   
print(swap_element([21,22,23,24,25],1,3))