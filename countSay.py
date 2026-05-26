#Leetcode Question: 38. Count and Say
def count_and_say(n):
    result = "1"

    for iter in range(n - 1):
        new_result = ""
        count = 1

        for i in range(1, len(result)):
            print('result[i]',result[i])
            if result[i] == result[i - 1]:
                count += 1
                print('count++',count)
            else:
                print('else count',count)
                new_result += str(count) + result[i - 1]
                count = 1

        # add last group
        new_result += str(count) + result[-1]
        print('new_result',new_result)
        result = new_result
        print('result',result)

    return result


print(count_and_say(4))  # Output: "111221"