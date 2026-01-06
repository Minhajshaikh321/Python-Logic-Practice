def reverse_string(s):
    st=" ".join(s.split()[::-1])
    return st

s = "the sky is blue"
print(reverse_string(s))