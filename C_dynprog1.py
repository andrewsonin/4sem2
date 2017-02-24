def recursion(n):
    if n <= 2:
        return 0
    f_list, g_list = [0, 0], [0, 0]
    for i in range(2, n):
        f_list.append(f_list[-1] + 2 * g_list[-2] + 1)
        g_list.append(f_list[-3] + 2 * g_list[-1] - 1)
    return f_list[-1]
print(recursion(int(input())))
