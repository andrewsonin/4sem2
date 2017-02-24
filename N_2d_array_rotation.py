operational_list, support_list = [], []
n, m = tuple(map(int, input().split()))
for i in range(n):
    operational_list.append(list(map(int, input().split())))
for j in range(m):
    for k in range(1, n + 1):
        support_list.append(operational_list[-k][j])
    print(*support_list)
    support_list = []
