n = int(input())
grasshoppers = list(map(int, input().split()))
time = int(input())
for i in range(time):
    grasshoppers.insert(-grasshoppers[-1] - 1, grasshoppers[-1])
    grasshoppers.pop()
print(*grasshoppers)
