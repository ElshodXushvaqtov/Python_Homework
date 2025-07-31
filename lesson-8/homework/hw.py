# 1. ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 2. ValueError
try:
    val = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Not an integer.")

# 3. FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

# 4. TypeError
try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    if not x.replace('.', '', 1).isdigit() or not y.replace('.', '', 1).isdigit():
        raise TypeError("Inputs must be numbers.")
    print(float(x) + float(y))
except TypeError as e:
    print(e)

# 5. PermissionError
try:
    with open("/root/secret.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Permission denied.")

# 6. IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range.")

# 7. KeyboardInterrupt
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# 8. ArithmeticError
try:
    a = 10
    b = 0
    print(a / b)
except ArithmeticError:
    print("Arithmetic error occurred.")

# 9. UnicodeDecodeError
try:
    with open("file.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Encoding issue with file.")

# 10. AttributeError
try:
    lst = [1, 2, 3]
    lst.upper()
except AttributeError:
    print("Attribute does not exist.")

# File Input/Output Exercises

# 1. Read entire file
with open("sample.txt", "r") as f:
    print(f.read())

# 2. Read first n lines
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 3. Append text to file and display
with open("sample.txt", "a") as f:
    f.write("\nAppended line.")
with open("sample.txt", "r") as f:
    print(f.read())

# 4. Read last n lines
n = 3
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# 5. Line by line into list
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
    print(lines)

# 6. Line by line into variable
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# 7. Line by line into array
with open("sample.txt", "r") as f:
    array = f.readlines()
    print(array)

# 8. Longest word
with open("sample.txt", "r") as f:
    words = f.read().split()
    print(max(words, key=len))

# 9. Count lines
with open("sample.txt", "r") as f:
    print(len(f.readlines()))

# 10. Word frequency
from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().replace(',', ' ').split()
    print(Counter(words))

# 11. File size
import os
print(os.path.getsize("sample.txt"))

# 12. Write list to file
lst = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")

# 13. Copy contents to another file
with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# 14. Combine each line from 2 files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

# 15. Random line from file
import random
with open("sample.txt", "r") as f:
    print(random.choice(f.readlines()).strip())

# 16. Check if file is closed
f = open("sample.txt", "r")
print(f.closed)
f.close()
print(f.closed)

# 17. Remove newlines
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
    print("".join(lines))

# 18. Count words in file
with open("sample.txt", "r") as f:
    text = f.read().replace(",", " ")
    print(len(text.split()))

# 19. Extract characters to list
files = ["sample.txt", "copy.txt"]
chars = []
for file in files:
    with open(file, "r") as f:
        chars.extend(list(f.read()))
print(chars)

# 20. Generate A.txt to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")

# 21. Letter
per_line = 5
letters = string.ascii_lowercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), per_line):
        f.write("".join(letters[i:i+per_line]) + "\n")
