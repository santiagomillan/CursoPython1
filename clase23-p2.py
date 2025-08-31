class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Account is inactive. Cannot deposit.")
        
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"the account has been deactivated")

    def activate_account(self):
        self.is_active = True
        print(f"the account has been activated")

account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

#Llamada a los metodos
account1.deposit(200)
account2.deposit(100)
account1.deactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)