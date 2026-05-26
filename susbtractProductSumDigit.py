#leetcode 1281 Subtract the Product and Sum of Digits of an Integer
def subtractProductAndSum(n):
    p=1
    s=0
    while n:
        digit=n%10
        p*=digit
        s+=digit
        n//=10
    return p-s
print(subtractProductAndSum(234))
