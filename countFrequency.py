#count the frequency of each character in the string and print the top three most common characters along with their counts.

from collections import Counter
word="aaaaaaaaaabbbbbbcccccdddee"
sorted_word=sorted(word)
frequency=Counter(sorted_word)
for k,v in frequency.most_common(3):
    print(f"{k}:{v}")