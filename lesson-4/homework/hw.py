# 1
fruit_prices = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 7}
ascending = dict(sorted(fruit_prices.items(), key=lambda item: item[1]))
print("Ascending:", ascending)
descending = dict(sorted(fruit_prices.items(), key=lambda item: item[1], reverse=True))
print("Descending:", descending)

# 2
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)

# 3
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
merged_dict = dict_a | dict_b | dict_c
print(merged_dict)

# 4
n = int(input())
number_squares = {x: x * x for x in range(1, n + 1)}
print(number_squares)

# 5
squares_1_to_15 = {x: x * x for x in range(1, 16)}
print(squares_1_to_15)

# 6
numbers_set = {1, 2, 3, 4, 5}
print('Set:', numbers_set)

# 7
values_set = {10, 20, 30, 40}
for value in values_set:
    print(value)

# 8
update_set = {1, 2, 3, 4}
update_set.add(5)
print(update_set)

# 9
removal_set = {1, 2, 3, 4}
removal_set.remove(1)
print(removal_set)

# 10
conditional_removal_set = {1, 2, 3, 4}
element_to_remove = 1
if element_to_remove in conditional_removal_set:
    conditional_removal_set.remove(element_to_remove)
    print(conditional_removal_set)
else:
    print('There is no such element:', element_to_remove)
