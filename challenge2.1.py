class BankAccount:

  def __init__ (self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      #self.__account_balance = self.__account_balance+amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount, 
                                                     self.__account_balance))
    else:
      print("Invalid desposit amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      
      print("Withdraw ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
      self.__account_holder_name, self.__account_number,
      self.__account_balance))

#create an instance of the Bannkaccont class
account = BankAccount(account_number="152405020104",
                     account_holder_name= "Arshidha",
                     initial_balance=10000.0)
#Test deposit and withdrawalfunctionality
account.display_balance()
account.deposit(1000.0)
account.withdraw(700.0)
account.display_balance()