def maximize(length, element):
    summa, element = 0, sorted(element)[length//2:]
    for obj in element:
        summa += obj
    return summa
print(maximize(int(input()), list(map(int, input().split()))))
