#LEETCODE QUESTION: 443. String Compression
def string(s):
    result=""
    count=1
    for i in range(1,len(s)):
        print(f'i {s[i]} i-1 {s[i-1]}')
        if s[i]==s[i-1]:
            count+=1
            print('count++',count)
        else:
            result+=s[i-1]+str(count)
            print('else result',result)
            count=1
    result+=s[-1]+str(count)
    print('lastgroup result',result)
    return result
string("aaabbcc")