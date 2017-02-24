def queen(desk):
    for i in range(8):
        for j in range(8):
            if i != j:
                if desk[i][0] - desk[i][1] == desk[j][0] - desk[j][1] or \
                                        -desk[i][0] - desk[i][1] == -desk[j][0] - desk[j][1]:
                    return 'YES'
                for k in range(2):
                    if desk[i][k] == desk[j][k]:
                        return 'YES'
    return 'NO'
print(queen([list(map(int, input().split())) for i in range(8)]))
