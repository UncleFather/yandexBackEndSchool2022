fi = open("input.txt",  "r")
s = fi.readline()
fi.close()
#s = input()
b = 0
for s1 in s:
    if s1 == "(":
        b += 1
    elif s1 == ")":
        b -= 1
if b == -1:
    k = 0
    for i in range(len(s)):
        if s[i] == ")":
            k = i
            break
    b = 0
    fl = True
    for i in range(len(s)):
        if i != k:
            if s[i] == "(":
                b += 1
            elif s[i] == ")":
                b -= 1
            if b < 0:
                fl = False
    if b != 0:
        fl = False
    if fl:
        print(k + 1)
    else:
        print(-1)
elif b == 1:
    l = -1
    while s[l + 1] != "(":
        l += 1
    r = len(s) - 1
    while r - l > 1:
        m = (r + l) // 2
        b = 0
        fl = True
        for i in range(len(s)):
            if i != m:
                if s[i] == "(":
                    b += 1
                elif s[i] == ")":
                    b -= 1
                if b < 0:
                    fl = False
            elif s[i] != "(":
                b -= 1
                if s[i] == ")":
                    b -= 1
                if b < 0:
                    fl = False
        if b != 0:
            fl = False
        if fl:
            r = m
        else:
            l = m
    b = 0
    fl = True
    for i in range(len(s)):
        if i != r:
            if s[i] == "(":
                b += 1
            elif s[i] == ")":
                b -= 1
            if b < 0:
                fl = False
    if b != 0:
        fl = False
    if fl:
        print(r + 1)
    else:
        print(-1)
else:
    print(-1)