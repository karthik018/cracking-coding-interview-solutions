# description: Given two strings, write a method to decide if one is permutation of the other.

from collections import defaultdict

def check_permutation(s, p):
    if len(s) != len(p):
        return False
    
    s = s.lower()
    p = p.lower()
    hash_mp = defaultdict(int)
    for c in s:
        hash_mp[c] += 1

    for c in p:
        hash_mp[c] -= 1

    for k, v in hash_mp.items():
        if v != 0:
            return False
    
    return True

if __name__ == "__main__":
    s = input()
    p = input()
    res = check_permutation(s, p)
    print(res)