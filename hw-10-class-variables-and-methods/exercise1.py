class BankAccount:
  interest_rate = 0.01
  accounts = []
  
  def __init__(self):
    self.balance = 0
    __class__.accounts.append(self) #Simply append the current instance of BankAccount to Accounts

  def deposit(self, deposit_amount):
    self.balance += deposit_amount
  
  def withdraw(self, withdraw_amount):
    if withdraw_amount >= self.balance:
      return f'No sufficient fund, your balance is {self.balance}'
    else:
      self.balance -= withdraw_amount
  
  @classmethod
  def total_funds(cls): #For every account in list of accounts, add its balance
    total_amt = 0  #should not simply return cls.accounts as it does not make any sense
    for acc in cls.accounts: #You can either use cls or __class__, both seem to work.
      total_amt += acc.balance 
    return total_amt
   
  @classmethod
  def add_interest(cls):
    for acc in cls.accounts:
      acc.balance += (acc.balance * cls.interest_rate)
  
def main():
  my_account = BankAccount()
  your_account = BankAccount()
  print(my_account.balance) #--> 0
  print(BankAccount.total_funds()) #--> 0
  my_account.deposit(200)
  your_account.deposit(1000)
  print(my_account.balance) #--> 200
  print(your_account.balance) #--> 1000
  print(BankAccount.total_funds()) #--> 1200
  BankAccount.add_interest()
  print(my_account.balance) #--> 202.0
  print(your_account.balance) #--> 1010.0
  print(BankAccount.total_funds()) #--> 1212.0
  my_account.withdraw(50)
  print(my_account.balance) #--> 152.0
  print(BankAccount.total_funds()) #--> 1162.0

main()
