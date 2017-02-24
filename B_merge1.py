def merge(left, right):
    len_left, len_right = len(left), len(right)
    operable_list = [None] * (len_left + len_right)
    i = j = k = 0
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            operable_list[k] = left[i]
            i += 1
        else:
            operable_list[k] = right[j]
            j += 1
        k += 1
    operable_list[k:] = left[i:] + right[j:]
    return operable_list
print(*merge(list(map(int, input().split())), list(map(int, input().split()))))
