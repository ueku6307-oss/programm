n = int(input())

total = 0
count = 1
for size in range(n, -1, -1):
    total += count
    count *= size

print(total)
