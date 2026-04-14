#Leetcode Question: 14. Longest Common Prefix
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        print('word',word)
        while word[:len(prefix)] != prefix:
            print('prefix',prefix,'prefix[-1]',prefix[:-1])
            prefix = prefix[:-1]   # reduce prefix

            if prefix == "":
                return ""

    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"