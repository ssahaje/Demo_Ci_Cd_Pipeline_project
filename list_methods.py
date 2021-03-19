sample_list = [2,7,9,7,5,3,3]

list_item_coumt = sample_list.count(7)
print(list_item_coumt)
copy_sample_list = sample_list.copy()
print(copy_sample_list)
print(sample_list.pop(0))
print(f'After popping up: {sample_list}')
sample_list.sort()
print(f'Sorted list: {sample_list}')
sample_list.reverse()
print(f'Descending after sorting the list: {sample_list}')
sample_list = [2,7,9,7,5,3,3]
sample_list.append(0)
print(f'Item appended at the end of the list: {sample_list}')
print(f'Index of 1st itme: {sample_list.index(2)}')
sample_list.insert(0, 1)
print(f'Inserting item in a list at position 0: {sample_list}')
sample_list = [2,7,9,7,5,3,3]
sample_list.remove(3)
print(f'After removal of specific item, 1st occurance will be removed from the list: {sample_list}')
sample_list = [2,7,9,7,5,3,3]
extend_list_by = [0,1]
sample_list.extend(extend_list_by)
print(f'Extend original list by list items: {sample_list}')
sample_list.append(extend_list_by)
print(f'Append original list by another list: {sample_list}')
# print(help(sample_list))
sample_list = [2,7,9,7,5,3,3]
sample_list.remove(3)
print(f'Remove specific item, in ths case 1st occurance of 3: {sample_list}')
sample_list.clear()
print(f'Clear list to empty it: {sample_list}')
