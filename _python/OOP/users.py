class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_deposit(self, amount):
        self.balance -= amount
    def make_withdrawl(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"{self.name}: ${self.balance}")
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

ryan = User("Ryan Ivers", 1000)
jake = User("Jake Rosene", 1000)
riley = User("Riley Ramirez", 2000)

ryan.make_deposit(40)
ryan.make_deposit(40)
ryan.make_deposit(40)
jake.make_deposit(50)
jake.make_deposit(50)
riley.make_deposit(20)
ryan.make_withdrawl(10)
jake.make_withdrawl(20)
jake.make_withdrawl(20)
riley.make_withdrawl(25)
riley.make_withdrawl(25)
riley.make_withdrawl(25)
ryan.transfer_money(jake, 50)


ryan.display_user_balance()
jake.display_user_balance()
riley.display_user_balance()

