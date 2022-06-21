n = int(input())
p = {}
for i in range(n):
    s, m = input().split(',')
    p[s] = int(m)
p1 = {}
k = int(input())
for i in range(k):
    c2, q2, p2, r2 = input().split(',')
    if not q2 in p1:
        p1[q2] = []
    p1[q2].append([-int(p2), int(r2), c2])
ans = []
for p2 in p:
    if p2 in p1:
        p1[p2] = sorted(p1[p2])
        for i in range(min(len(p1[p2]), p[p2])):
            ans.append(p1[p2][i][2])
ans = sorted(ans)
for ans1 in ans:
    print(ans1)