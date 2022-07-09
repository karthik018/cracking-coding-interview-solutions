# description: Write a method to replace all the spaces in a string with '%20'.

def urlify(s, tl):
    s = list(s)
    spaces = 0
    for i in range(tl):
        if s[i] == ' ':
            spaces += 1
    
    indx = tl + spaces * 2
    for i in range(tl-1, -1, -1):
        if s[i] == ' ':
            s[indx-1] = '0'
            s[indx-2] = '2'
            s[indx-3] = '%'
            indx -= 3
        else:
            s[indx-1] = s[i]
            indx -= 1

    return ''.join(s)

if __name__ == "__main__":
    s = input()
    tl = int(input())
    res = urlify(s, tl)
    print(res)