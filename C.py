x, a, b, c, d = map(int, input().split())

people = [a, b, c, d]
corners = [0, x, 2 * x, 3 * x]

total = 0
summ = 0
for i in range(4):
    total += people[i]
    summ += people[i] * corners[i]

if total == 0:
    print(0)
else:
    point = summ // total

    ans = 0
    for i in range(4):
        ans += people[i] * abs(point - corners[i])

    print(ans)
