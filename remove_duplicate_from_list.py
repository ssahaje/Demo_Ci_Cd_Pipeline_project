numbers = [3,5,5,7,8,9,0,3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
