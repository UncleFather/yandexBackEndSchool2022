from queue import Queue

def go(x, y):
    if ans[x - 1][y] == ".":
        ans[x - 1][y] = "U"
        go(x - 1, y)
    if ans[x + 1][y] == ".":
        ans[x + 1][y] = "D"
        go(x + 1, y)
    if ans[x][y - 1] == ".":
        ans[x][y - 1] = "L"
        go(x, y - 1)
    if ans[x][y + 1] == ".":
        ans[x][y + 1] = "R"
        go(x, y + 1)
    return

n, m = map(int, input().split())
ans = [[c for c in input()] for i in range(n)]
i1 = -1
j1 = -1
for i in range(n):
    for j in range(m):
        if ans[i][j] == "S":
            i1 = i
            j1 = j
q = Queue()
q.put([i1, j1])
while not q.empty():
    t = q.get()
    x = t[0]
    y = t[1]
    if ans[x - 1][y] == ".":
        ans[x - 1][y] = "U"
        q.put([x - 1, y])
    if ans[x + 1][y] == ".":
        ans[x + 1][y] = "D"
        q.put([x + 1, y])
    if ans[x][y - 1] == ".":
        ans[x][y - 1] = "L"
        q.put([x, y - 1])
    if ans[x][y + 1] == ".":
        ans[x][y + 1] = "R"
        q.put([x, y + 1])
for ans1 in ans:
    for ans2 in ans1:
        print(ans2, end = "")
    print()