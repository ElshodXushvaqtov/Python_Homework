import datetime
import random
import string

# 1. Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"{name}, you are {age} years old.\n")

# 2. Extract Car Names (1st string)
txt1 = 'LMaasleitbtui'
car1 = txt1[1::2]
print("Extracted car name from first text:", car1)

# 3. Extract Car Names (2nd string)
txt2 = 'MsaatmiazD'
car2 = txt2[::2]
print("Extracted car name from second text:", car2)

# 4. Extract Residence Area
txt3 = "I'am John. I am from London"
residence = txt3.split("from")[-1].strip()
print("Residence area extracted:", residence)

# 5. Reverse String
user_input = input("\nEnter a string to reverse: ")
reversed_str = user_input[::-1]
print("Reversed string:", reversed_str)

# 6. Count Vowels
vowel_input = input("\nEnter a string to count vowels: ")
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in vowel_input if char in vowels)
print("Number of vowels:", vowel_count)

# 7. Find Maximum Value
num_list = list(map(int, input("\nEnter a list of numbers separated by spaces: ").split()))
max_value = max(num_list)
print("Maximum value:", max_value)

# 8. Check Palindrome
word = input("\nEnter a word to check if it is a palindrome: ")
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# 9. Extract Email Domain
email = input("\nEnter your email address: ")
domain = email.split('@')[-1]
print("Email domain:", domain)

# 10. Generate Random Password
length = int(input("\nEnter desired password length: "))
all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for _ in range(length))
print("Generated password:", password)
