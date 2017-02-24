N, dictionary = int(input()), dict()
for i in range(N):
    operable_list = input().split()
    dictionary.update({operable_list[0]: operable_list[1]})
for j in range(N):
    operable_list = input().split()
    print(dictionary[operable_list[0]], operable_list[1])
