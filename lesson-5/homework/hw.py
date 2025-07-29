1
year = int(input())


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year')
        else:
            print('Not Leap Year')
    else:
        print('Leap Year')
else:
    print('Not Leap Year')


2
n = int(input())

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0:
    if 2 <= n and n <= 5:
        print('Not Weird')
    elif 6 <= n and n <= 20:
        print('Weird')
    else:
        print('Not Weird')


3
1.
try:
  # Get numbers from the user
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))

  # Find the first even number to start from
  if a % 2 == 0:
    start_even = a
  else:
    start_even = a + 1
  
  # Generate the list of even numbers and print it
  result = list(range(start_even, b + 1, 2))
  print(f"\nEven numbers: {result}")

except ValueError:
  print("\nOops! Please enter whole numbers only.")


2.
try:
  # Get numbers from the user
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))

  # Calculate the first even number directly
  # If a is even, a % 2 is 0. If odd, a % 2 is 1.
  start_even = a + (a % 2)
  
  # Generate the list of even numbers and print it
  result = list(range(start_even, b + 1, 2))
  print(f"\nEven numbers: {result}")

except ValueError:
  print("\nOops! Please enter whole numbers only.")
