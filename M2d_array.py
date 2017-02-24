def array(operational_tuple, operational_list):
    for i in range(operational_tuple[0]):
        print(*operational_list[i * operational_tuple[1]:i * operational_tuple[1] + operational_tuple[1]])
array(tuple(map(int, input().split())), list(map(int, input().split())))
