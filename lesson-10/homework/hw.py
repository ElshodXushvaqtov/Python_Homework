1.
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {'Completed' if self.status else 'Incomplete'}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        
    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None

    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = True
                return True
        return False

    def display_tasks(self, filter_status=None):
        tasks = self.tasks
        if filter_status is not None:
            tasks = [task for task in tasks if task.status == filter_status]
        
        if not tasks:
            if filter_status is False:
                print("\nNo incomplete tasks!")
            elif filter_status is True:
                print("\nNo completed tasks!")
            else:
                print("\nNo tasks available!")
        else:
            print("\nTasks:")
            for task in tasks:
                print(task)


class ToDoCLI:
    def __init__(self):
        self.todo_list = ToDoList()

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Display Incomplete Tasks")
            print("4. Display All Tasks")
            print("5. Exit")

            try:
                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    title = input("Enter task title: ").strip()
                    description = input("Enter task description: ").strip()
                    due_date = input("Enter due date: ").strip()
                    
                    if not title or not description or not due_date:
                        print("\nError: Title, description, and due date cannot be empty!")
                    else:
                        self.todo_list.add_task(Task(title, description, due_date))
                        print("\nTask added successfully!")
                        
                elif choice == "2":
                    if not self.todo_list.tasks:
                        print("\nNo tasks available to mark as completed!")
                    else:
                        title = input("Enter task title: ").strip()
                        if not title:
                            print("\nTask title cannot be empty!")
                        else:
                            if self.todo_list.mark_task_as_completed(title):
                                print(f"\nTask '{title}' marked as completed!")
                            else:
                                print(f"\nTask '{title}' not found.")
                                
                elif choice == "3":
                    self.todo_list.display_tasks(filter_status=False)
                    
                elif choice == "4":
                    self.todo_list.display_tasks()
                    
                elif choice == "5":
                    print("\nGoodbye!")
                    break
                    
                else:
                    print("\nInvalid choice! Please choose a number between 1-5.")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
                print("Please try again.")


cli = ToDoCLI()
cli.run()





2.
class Post:

    def __init__(self,title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\n{'-'*30}"

class Blog:

    def __init__(self):
        self.posts = []
    
    def questions(self):
        print('\nMenu:')
        print('\n1. Edit title')
        print('2. Edit content')
        print('3. Edit author')
        print('4. Exit')

    def addPost(self,post):
        self.posts.append(post)
    
    def listPosts(self):
        for i in self.posts:
            print(i)
    
    def listByAuthor(self, author):
        found = False
        for i in self.posts:
            if i.author == author:
                print(i)
                found = True
        if not found:
            print(f"No posts found by author '{author}'")
    
    def deletePost(self, title):
        status = False
        for i in self.posts:
            if i.title == title:
                self.posts.remove(i)
                print(f'{title} removed')
                status = True
                break
        if status == False:
            print(f'{title} is not found')


    def displayLatest(self):
        if self.posts:
            print(self.posts[-1])
        else:
            print("No posts available")
    
    def editPost(self,title):
        found = False
        for i in self.posts:
            if title == i.title:
                found = True
                self.questions()
                try:
                    choice = int(input())
                    if choice == 1:
                        print('Enter new title: \n')
                        new_title = input().strip()
                        if new_title:
                            i.title = new_title
                            print('Title updated successfully!')
                        else:
                            print('Title cannot be empty!')
                    elif choice == 2:
                        print('Enter new content: \n')
                        new_content = input().strip()
                        if new_content:
                            i.content = new_content
                            print('Content updated successfully!')
                        else:
                            print('Content cannot be empty!')
                    elif choice == 3:
                        print('Enter new author: \n')
                        new_author = input().strip()
                        if new_author:
                            i.author = new_author
                            print('Author updated successfully!')
                        else:
                            print('Author cannot be empty!')
                    elif choice == 4:
                        break
                    else:
                        print('Invalid number! Please choose 1-4.')
                except ValueError:
                    print('Please enter a valid number!')
                break
        if not found:
            print(f"Post with title '{title}' not found!")


class BlogCLI:
    def __init__(self):
        self.blog = Blog()

    def run(self):
        while True:
            print('\nMenu:')
            print('\n1. Add Post')
            print('2. List Posts')
            print('3. List Posts by Author')
            print('4. Delete Post')
            print('5. Display Latest Post')
            print('6. Edit Post')
            print('7. Exit')

            try:
                choice = int(input('Enter your choice: '))

                if choice == 1:
                    title = input('Enter title: \n').strip()
                    content = input('Enter content: \n').strip()
                    author = input('Enter author: \n').strip()
                    
                    if not title or not content or not author:
                        print('Error: Title, content, and author cannot be empty!')
                    else:
                        self.blog.addPost(Post(title, content, author))
                        print('Post added successfully!')
                        
                elif choice == 2:
                    if not self.blog.posts:
                        print('No posts available!')
                    else:
                        self.blog.listPosts()
                        
                elif choice == 3:
                    if not self.blog.posts:
                        print('No posts available!')
                    else:
                        author = input('Enter author: \n').strip()
                        if not author:
                            print('Author name cannot be empty!')
                        else:
                            self.blog.listByAuthor(author)
                            
                elif choice == 4:
                    if not self.blog.posts:
                        print('No posts available to delete!')
                    else:
                        title = input('Enter title: \n').strip()
                        if not title:
                            print('Title cannot be empty!')
                        else:
                            self.blog.deletePost(title)
                            
                elif choice == 5:
                    self.blog.displayLatest()
                    
                elif choice == 6:
                    if not self.blog.posts:
                        print('No posts available to edit!')
                    else:
                        title = input('Enter title: \n').strip()
                        if not title:
                            print('Title cannot be empty!')
                        else:
                            self.blog.editPost(title)
                            
                elif choice == 7:
                    print('Goodbye!')
                    break
                else:
                    print('Invalid choice! Please choose a number between 1-7.')
                    
            except ValueError:
                print('Please enter a valid number!')
            except KeyboardInterrupt:
                print('\nGoodbye!')
                break



cli = BlogCLI()
cli.run()



3.
class Account:
    """Represents a bank account with basic information and balance."""
    
    def __init__(self, acc_number, acc_name):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.acc_balance = 0
    
    def __str__(self):
        return f"Account({self.acc_number}, {self.acc_name}, ${self.acc_balance})"


class Bank:
    """Manages multiple bank accounts and provides banking operations."""
    
    def __init__(self):
        self.accounts = []
    
    def find_account(self, acc_number):
        """Find and return account by account number."""
        for account in self.accounts:
            if account.acc_number == acc_number:
                return account
        return None
        
    def add_acc(self,acc):
        self.accounts.append(acc)
    
    def check_balance(self, acc_number):
        """Display the balance for the specified account."""
        account = self.find_account(acc_number)
        if account:
            print(f"Balance: ${account.acc_balance}")
        else:
            print('Account not found!')
    
    def deposit_money(self, amount, acc_number):
        """Deposit money into the specified account."""
        account = self.find_account(acc_number)
        if account:
            account.acc_balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${account.acc_balance}")
        else:
            print('Account not found!')            

    
    def withdraw_money(self, amount, acc_number):
        """Withdraw money from the specified account."""
        account = self.find_account(acc_number)
        if not account:
            print('Account not found!')
            return
            
        if account.acc_balance >= amount:
            account.acc_balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${account.acc_balance}")
        else:
            print('Insufficient funds!')
    
    def transfer_money(self, sender, receiver, amount):
        sender_acc = None
        receiver_acc = None
        
        for acc in self.accounts:
            if acc.acc_number == sender:
                sender_acc = acc
            if acc.acc_number == receiver:
                receiver_acc = acc
        
        if not sender_acc:
            print('Sender account not found!')
            return
        if not receiver_acc:
            print('Receiver account not found!')
            return
        if sender_acc.acc_balance < amount:
            print('Insufficient funds in sender account!')
            return
            

        sender_acc.acc_balance -= amount
        receiver_acc.acc_balance += amount
        print(f'Successfully transferred ${amount} from {sender} to {receiver}')  
  

    def display_details(self, acc_name):
        """Display detailed information for accounts matching the holder name."""
        found_accounts = [acc for acc in self.accounts if acc.acc_name == acc_name]
        
        if found_accounts:
            for acc in found_accounts:
                print(f'Account Number: {acc.acc_number}')
                print(f'Account Holder: {acc.acc_name}')
                print(f'Balance: ${acc.acc_balance}')
                print('-' * 30)
        else:
            print('No accounts found for that name!')


class BankCLI:
    """Command Line Interface for the Banking System."""
    
    def __init__(self):
        self.bank = Bank()
    
    def get_valid_input(self, prompt, input_type=str, validator=None):
        """Get and validate user input."""
        while True:
            try:
                value = input_type(input(prompt).strip())
                if validator and not validator(value):
                    print("Invalid input. Please try again.")
                    continue
                return value
            except ValueError:
                print(f"Please enter a valid {input_type.__name__}.")
    
    def check_accounts_exist(self):
        """Check if any accounts exist in the bank."""
        if not self.bank.accounts:
            print('No accounts exist yet!')
            return False
        return True
    

    def run(self):
        while True:
            print('\nMenu:')
            print('1. Add account')
            print('2. Check Balance')
            print('3. Deposit Money')
            print('4. Withdraw Money')
            print('5. Transfer Money')
            print('6. Display Details')
            print('7. Exit')

            try:
                choice = int(input('Enter your choice: '))

                if choice == 1:
                    acc_name = input('Enter account holder name: \n').strip()
                    acc_number = input('Enter account number: \n').strip()

                    if not acc_name or not acc_number:
                        print('Error, all fields must be filled!')
                    else:
                        self.bank.add_acc(Account(acc_number, acc_name))
                        print('Account created successfully!')
            
                elif choice == 2:
                    acc_number = input('Enter account number: ')
                    if not self.bank.accounts:
                        print('There are not any accounts!')
                    elif not acc_number:
                        print('Account number must be filled!')
                    else:
                        self.bank.check_balance(acc_number)
            

                elif choice == 3:
                    amount = int(input('Enter amount: '))
                    acc_number = input('Enter account number: ')
                    if not self.bank.accounts:
                        print('There are not any accounts!')
                    elif not acc_number or not amount:
                        print('All fields must be filled!')
                    else:
                        self.bank.deposit_money(amount,acc_number)
            

                elif choice == 4:
                    amount = int(input('Enter amount: '))
                    acc_number = input('Enter account number: ')
                    if not self.bank.accounts:
                        print('There are not any accounts!')
                    elif not acc_number or not amount:
                        print('All fields must be filled!')
                    else:
                        self.bank.withdraw_money(amount,acc_number)


                elif choice == 5:
                    amount = int(input('Enter amount: '))
                    sender = input('Enter sender account number: ')
                    receiver = input('Enter receiver account number: ')
                    if not self.bank.accounts:
                        print('There are no accounts!')
                    elif not amount or not receiver or not sender:
                        print('All fields must be filled!')
                    else:
                        self.bank.transfer_money(sender, receiver, amount)
            

                elif choice == 6:
                    if self.check_accounts_exist():
                        acc_name = self.get_valid_input('Enter account holder name: ', 
                                                       validator=lambda x: len(x) > 0)
                        self.bank.display_details(acc_name)

                elif choice == 7:
                    print('Goodbye!')
                    break

                else:
                    print('Invalid choice! Please choose a number between 1-7.')
            
            except ValueError:
                print('Please enter a valid number!')
            except KeyboardInterrupt:
                print('\nGoodbye!')
                break

cli = BankCLI()
cli.run()
