the_tuple = (1,2,3,4)
the_list = list(the_tuple)
print(the_tuple)
print(the_list)

second_list = list(i for i in the_tuple)
print(second_list)