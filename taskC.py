p = eval(input())
q = {"NAME_CONTAINS": "", "PRICE_GREATER_THAN" : "", "PRICE_LESS_THAN" : "", "DATE_BEFORE" : "", "DATE_AFTER" : ""}
for i in range(5):
    q1, v = input().split()
    q[q1] = v
q["PRICE_GREATER_THAN"] = int(q["PRICE_GREATER_THAN"])
q["PRICE_LESS_THAN"] = int(q["PRICE_LESS_THAN"])
p1 = []
q1 = "NAME_CONTAINS"
for p2 in p:
    if q[q1].lower() in p2["name"].lower():
        p1.append(p2)
p = p1
p1 = []
q1 = "PRICE_GREATER_THAN"
for p2 in p:
    if p2["price"] >= q[q1]:
        p1.append(p2)
p = p1
p1 = []
q1 = "PRICE_LESS_THAN"
for p2 in p:
    if p2["price"] <= q[q1]:
        p1.append(p2)
p = p1
p1 = []
q1 = "DATE_BEFORE"
d1, m1, y1 = map(int, q[q1].split('.'))
for p2 in p:
    d2, m2, y2 = map(int, p2["date"].split('.'))
    if y2 < y1:
        p1.append(p2)
    elif y2 == y1 and m2 < m1:
        p1.append(p2)
    elif y2 == y1 and m2 == m1 and d2 <= d1:
        p1.append(p2)
p = p1
p1 = []
q1 = "DATE_AFTER"
d1, m1, y1 = map(int, q[q1].split('.'))
for p2 in p:
    d2, m2, y2 = map(int, p2["date"].split('.'))
    if y2 > y1:
        p1.append(p2)
    elif y2 == y1 and m2 > m1:
        p1.append(p2)
    elif y2 == y1 and m2 == m1 and d2 >= d1:
        p1.append(p2)
p = p1
p1 = []
for p2 in p:
    p1.append([p2["id"], p2])
p1 = sorted(p1)
p = []
for p2 in p1:
    p.append(p2[1])
ans1 = str(p)
ans = ''
for i in ans1:
    if i == '\'':
        ans += '"'
    else:
        ans += i
print(ans)