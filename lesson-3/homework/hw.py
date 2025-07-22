# 1
fruits = ['Apple', 'Pineapple', 'Orange', 'Pear', 'Strawberry']
print(fruits[2])

# 2
numbers_list1 = [1, 2, 3, 4]
numbers_list2 = [5, 6, 7, 8]
combined_list = numbers_list1 + numbers_list2
print(combined_list)

# 3
nums = [1, 2, 3, 4, 5, 6, 7]
extracted = [nums[0], nums[len(nums)//2], nums[-1]]
print(extracted)

# 4
favorite_movies = ['Interstellar', 'Schindlers List', 'X-Men', 'Inception', 'Avatar']
movies_tuple = tuple(favorite_movies)
print(movies_tuple)

# 5
cities = ['Paris', 'Moscow', 'Tashkent']
print('Paris' in cities)

# 6
original_numbers = [1, 2, 3]
copied_numbers = original_numbers.copy()
print(copied_numbers)

# 7
swappable_list = [1, 2, 3, 4]
swappable_list[0], swappable_list[-1] = swappable_list[-1], swappable_list[0]
print(swappable_list)

# 8
ten_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_tuple = ten_numbers[2:7]
print(sliced_tuple)

# 9
colors = ['red', 'blue', 'yellow', 'green', 'blue']
blue_count = colors.count('blue')
print(blue_count)

# 10
animals = ('cat', 'bear', 'lion', 'dog')
lion_index = animals.index('lion')
print(lion_index)

# 11
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
merged_tuple = tuple_a + tuple_b
print(merged_tuple)

# 12
sample_tuple = (1, 2, 3, 4)
sample_list = [1, 2, 3, 4, 5, 6]
print('Length of tuple:', len(sample_tuple))
print('Length of list:', len(sample_list))

# 13
tuple_numbers = (1, 2, 3, 4, 5)
converted_list = list(tuple_numbers)
print(converted_list)

# 14
range_tuple = (1, 2, 3, 4)
print('Minimum value:', min(range_tuple))
print('Maximum value:', max(range_tuple))

# 15
word_tuple = ('bad', 'good', 'fast', 'slow')
reversed_words = word_tuple[::-1]
print(reversed_words) 
