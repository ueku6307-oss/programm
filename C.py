x, a, b, c, d = map(int, input().split())

people = [a, b, c, d]
pos = [0, x, 2 * x, 3 * x]
peri = 4 * x

half = (sum(people) + 1) // 2
acc = 0
point = 0
for i in range(4):
    acc += people[i]
    if acc >= half:
        point = pos[i]
        break

ans = 0
for i in range(4):
    dist = abs(point - pos[i])
    ans += people[i] * min(dist, peri - dist)

print(ans)
