# Description: implement algorithm to determine if a string has all unique characters.
# Note: What if we can't use another data structure.

def is_unique(s):
    s = list(s)
    s.sort()
    n = len(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
            return False
    return True


if __name__ == '__main__':
    s = input()
    res = is_unique(s)
    print(res)