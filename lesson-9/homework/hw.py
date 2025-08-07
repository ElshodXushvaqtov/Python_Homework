import math
from datetime import datetime

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(20)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())


# 2. Person Class
class Person:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )
        return f"{self.name} is from {self.country} and {age} years old"

p1 = Person('John', 'USA', '2005-09-09')
print(p1.age())


# 3. Calculator Class
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2

calc = Calculator(20, 8)
print("Add:", calc.add())
print("Subtract:", calc.subtract())
print("Multiply:", calc.multiply())
print("Divide:", calc.divide())


# 4. Shape Inheritance
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c, height=None):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        if self.height:
            return 0.5 * self.a * self.height
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return 4 * self.a

shapes = [
    Circle(5),
    Triangle(3, 4, 5),
    Triangle(4, 5, 6, height=3),
    Square(4)
]

for shape in shapes:
    print(f"Area: {round(shape.area(), 2)}, Perimeter: {round(shape.perimeter(), 2)}")


# 5. Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            current = current.left if value < current.value else current.right
        return False

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(5))
print(bst.search(12))


# 6. Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.items:
            print(f"Popped: {self.items[-1]}")
            return self.items.pop()
        print("Stack is empty!")
        return None

    def is_empty(self):
        return not self.items

    def display(self):
        print("Stack:", self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.display()
stack.pop()
stack.display()


# 7. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted: {data}")

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Deleted: {data}")
                return
            prev = current
            current = current.next
        print(f"{data} not found in list.")

    def display(self):
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.display()
ll.delete(10)
ll.display()


# 8. Shopping Cart
class Cart:
    def __init__(self):
        self.cart = []

    def add(self, name, price):
        self.cart.append((name, price))

    def remove(self, name):
        for i, (item_name, _) in enumerate(self.cart):
            if item_name == name:
                del self.cart[i]
                break

    def calculate_total(self):
        return sum(price for _, price in self.cart)

my_cart = Cart()
my_cart.add("Apple", 1.5)
my_cart.add("Banana", 0.8)
my_cart.add("Apple", 1.5)
print("Total:", my_cart.calculate_total())

print("Removing 'Apple'...")
my_cart.remove("Apple")
print("Total:", my_cart.calculate_total())


# 10. Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        return self.items[0] if self.items else "Queue is empty"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

q = Queue()
q.enqueue("Apple")
q.enqueue("Banana")
q.enqueue("Cherry")
print("Queue:", q.display())
print("Dequeued:", q.dequeue())
print("Queue Now:", q.display())


# 11. Bank Class
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into {self.customer_name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.customer_name}'s account.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.customer_name} - Account #{self.account_number} - Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account with this number already exists.")
        else:
            account = BankAccount(account_number, customer_name, initial_deposit)
            self.accounts[account_number] = account
            print(f"Account created for {customer_name} with account number {account_number}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def show_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

bank = Bank()
bank.create_account("123456", "Alice", 1000)
bank.deposit_to_account("123456", 500)
bank.withdraw_from_account("123456", 200)
bank.show_account_info("123456")
