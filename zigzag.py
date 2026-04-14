def zigzag(s,numRows):
    if numRows==1:
        return s
    i=0
    d=1
    rows=[[] for _ in range(numRows)]
    for ch in s:
        rows[i].append(ch)
        if i==0:
            d=1
        elif i==numRows-1:
            d=-1
        i+=d
    res=""
    for i in range(numRows):
        res+="".join(rows[i])
    return res
print(zigzag("PAYPALISHIRING", 3))
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"