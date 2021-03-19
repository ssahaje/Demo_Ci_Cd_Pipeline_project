the_list = [1, 3, 5, 7]
the_tuple = tuple(the_list)
print(the_list)
print(the_tuple)

second_tuple = tuple(i for i in the_list)
print(second_tuple)


# Python3 program to convert a
# list into a tuple
def convert(list):
    return tuple(i for i in list)


# Driver function
list = [1, 2, 3, 4]
print(convert(list))