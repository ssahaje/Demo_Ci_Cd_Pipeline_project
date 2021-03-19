numbers = [3,5,4,3,5,7,8,9,4,3,2,1]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'The largest number in the list is: {max}')