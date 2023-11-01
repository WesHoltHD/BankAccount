# Create a BankAccount class with the attributes interest rate and balance 
# Add a deposit method to the BankAccount class 
# Add a withdraw method to the BankAccount class 
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class
# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
        
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit : ${amount}")
        print(f"New Current Balance : ${self.balance}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #& Merely For Clear Seperation In Terminal
        # return self
        
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f"Withdraw: ${amount}")
            print(f"New Balance : ${self.balance}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #& Merely For Clear Seperation In Terminal
        else:
            print("Insufficient Funds: Charging A $5 Overdraft Fee")
            self.balance -= 5
            print(f"New Negative Balance: ${self.balance}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #& Merely For Clear Seperation In Terminal
        # return self
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #& Merely For Clear Seperation In Terminal
        # return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        print(f"Interest + Balance : ${self.balance}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #& Merely For Clear Seperation In Terminal
        # return self
        
    @classmethod
    def printAllAccounts(cls):
        for account in cls.accounts:
            account.display_account_info()
    
#* NOTE: Remember When Creating An Instance (Accounts) Since the __Init__ functions are asking for 2 different arguments
savings_account = BankAccount(.05,1000) 
checking_account = BankAccount(.02,5000)

savings_account.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()

print("+++++++++++++") #& Merely For Clear Seperation In Terminal

checking_account.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

#? NOTE : Following Operations Above NEED A RETURN OF SELF!!!
#^ - REQUIRED For The Chaining Methods (PERSONALLY NOT PREFERED)





#* NOTE : Following Operations Below DO NOT Need A RETURN OF SELF!!!
#& - NOT Required IF NOT Chaining Methods (PERSONALLY PREFERED)


# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 
savings_account.deposit(10)
savings_account.deposit(20)
savings_account.deposit(40)
savings_account.withdraw(600)
savings_account.yield_interest()
savings_account.display_account_info()

print("+++++++++++++") #& Merely For Clear Seperation In Terminal

checking_account.deposit(100)
checking_account.deposit(200)
checking_account.deposit(400)
checking_account.withdraw(60)
checking_account.yield_interest()
checking_account.display_account_info()

print("+++++++++++++") #& Merely For Clear Seperation In Terminal 

BankAccount.printAllAccounts()