import copy

name = "Gnaneswar"

my_list = [[1,2,3],[4,5,6],[7,8,9]]

new_list = copy.deepcopy(my_list)

my_list[2][2] = 26
print(new_list)
print(my_list)