### 1

### to-do list application

class Task:
    def __init__(self, t_title, t_desc, t_date, t_st=False):
        self.t_title = t_title 
        self.t_desc = t_desc
        self.t_date = t_date
        self.t_st = t_st # false - undone, true - done.


class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_t(self, obj):
        self.tasks.append(obj)
        print("the task has been successfully added to your list.")

    def mark_compl(self, obj):
        for i in self.tasks:
            if i.t_title == obj or i == obj:
                i.t_st = True
                break
        
        print(f'you marked the task "{i.t_title}" as completed.')

    def list_tasks(self):
        for i in self.tasks:
            print(i.t_title)

    def list_incompl(self):
        for i in self.tasks:
            if i.t_st == False:
                print(i.t_title)



task1 = Task("abc", "abc", "20:00", False)
task2 = Task("bca", "abc", "20:00", False)
task3 = Task("qwerty", "abc", "20:00", False)
manager = ToDoList()

manager.add_t(task1)
# manager.list_tasks()
manager.add_t(task2)
manager.mark_compl(task2)
manager.list_incompl()
print("")
manager.list_tasks()

def menu():
    print("")
    print("1. Add a task.")
    print("2. Mark a task as completed.")
    print("3. List all tasks.")
    print("4. List incompleted tasks.")
    print("5. Exit.")
    print("")



def main():
    while 1:

        menu()

        user_inp = int(input("What would you like to do?(number): "))

        
        if user_inp == 1:

            manager.add_t()

        elif user_inp == 2:
            manager.mark_compl()

        elif user_inp == 3:
            manager.list_tasks()
        
        elif user_inp == 4:
            manager.list_incompl()
        
        elif user_inp == 5:
            return 
        
        else:
            print("try again, please.")



main()
### 2

class Post:
    def __init__(self, title, content, author):
        p_title = title
        p_content = content
        p_author = author


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, obj):
        self.posts.append(obj)
        print("the post has been published.")
        return 
    
    def list_posts(self):
        for val in self.posts:
            print(val.p_content)

        return 
    
    def display_posts_by(self, author):
        print(f"here're all the posts published by {author}.")
        for p in self.posts:
            if p.p_author == author:
                print(p.p_content)

    def delete_post(self, title, content):
        for p in self.posts:
            if p.p_title == title and p.p_content == content:
                self.posts.remove(p)
        

    def edit_post(self, curr_p, new_p):
        for p in self.posts:
            if curr_p == p.p_content:
                p.p_content = new_p
        

    def latest_posts(self, n_of_posts):
        num = n_of_posts
        print(f"the last {num} posts:")

        for p in self.posts[::-1]:
            print(p.p_content)

            if num == 0:
                break
    
            num -= 1

m = Blog()

def menu():
    print("")
    print("1. Publish a post.")
    print("2. Display posts by a specific author.")
    print("3. List all posts.")
    print("4. Edit a post.")
    print("5. Show latest posts.")
    print("6. Delete a post.")
    print("7. Exit.")
    print("")


while 1:

    menu()

    user_inp = int(input("What would you like to do?(number): "))

    
    if user_inp == 1:
        m.add_post()

    elif user_inp == 2:
        author = input("enter the author's name: ")
        m.display_posts_by(author)

    elif user_inp == 3:
        m.list_posts()
    
    elif user_inp == 4:
        curr_p = input("enter current post's content: ")
        new_p = input("enter new post's content: ")
        m.edit_post(curr_p, new_p)
    
    elif user_inp == 5:
        m.latest_posts(int(input("enter a number: ")))
    
    elif user_inp == 6:
        m.delete_post(input("title of the post: "), input("content: "))
    
    elif user_inp == 7:
        break
    
    else:
        print("try again, please.")




### 3

class Account:
    def __init__(self, acc_num, holder, balance=0):
        self.acc_num = acc_num
        self.holder = holder
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)
        print("Account created.")

    def find(self, acc_num):
        for a in self.accounts:
            if a.acc_num == acc_num:
                return a
        return None

    def check_balance(self, acc_num):
        acc = self.find(acc_num)
        if acc:
            print(f"Balance: {acc.balance}")
        else:
            print("Account not found.")

    def deposit(self, acc_num, amount):
        acc = self.find(acc_num)
        if acc:
            acc.balance += amount
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, acc_num, amount):
        acc = self.find(acc_num)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        a = self.find(from_acc)
        b = self.find(to_acc)
        if not a or not b:
            print("Invalid account number.")
            return
        if a.balance < amount:
            print("Insufficient funds.")
            return
        a.balance -= amount
        b.balance += amount
        print("Transfer complete.")

    def show_details(self, acc_num):
        acc = self.find(acc_num)
        if acc:
            print(f"Account: {acc.acc_num}, Holder: {acc.holder}, Balance: {acc.balance}")
        else:
            print("Account not found.")


bank = Bank()


def menu():
    print("")
    print("1. Add account")
    print("2. Check balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Show account details")
    print("7. Exit")
    print("")


while True:
    menu()
    x = int(input("Choose: "))

    if x == 1:
        num = input("Account number: ")
        name = input("Holder name: ")
        bal = int(input("Initial balance: "))
        bank.add_account(Account(num, name, bal))

    elif x == 2:
        bank.check_balance(input("Account number: "))

    elif x == 3:
        bank.deposit(input("Account number: "), int(input("Amount: ")))

    elif x == 4:
        bank.withdraw(input("Account number: "), int(input("Amount: ")))

    elif x == 5:
        a = input("From account: ")
        b = input("To account: ")
        amt = int(input("Amount: "))
        bank.transfer(a, b, amt)

    elif x == 6:
        bank.show_details(input("Account number: "))

    elif x == 7:
        break

    else:
        print("Try again.")
