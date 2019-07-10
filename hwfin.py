'''
Create a banking program that represents the process of banking and utilizes two classes: The Bank class and the customer class
The classes will have (but are not limited to) the following attributes and methods. Feel free to add more if you'd like
The bank class has the following attributes:
  Name, Current Balance in bank, minimum amount of currency needed to have an account, number of customers, and list of customers
The bank class has the following functions:
  Constructor (see above),
  ///////Loan money #gives out some of balance to a customer
  ///////UpdateBalance #returns balance after some exchange
  ///////UpdateCustomers #returns the number of customers at the bank
  AccountCheck #checks if a given customer has enough money in their account. If it is below this number, the customer is removed from the system and the remaining balance goes back to the customer's personal fund. If it is at or above the given number, a customer ///////may have or may continue to have an account.
The customer class has the following attributes:
  Name, Personal Fund, Bank Account, and a boolean value: MemberStatus
  -The bank account is always 0 unless MemberStatus is true
The customer class has the following functions:
  Startaccount(bank) #attempts to create an account with a bank. If successful, bank account will begin with the bank's minimum required balance, taken from the personal fund to the bank account
  Transfer_from_personal(x)#transfers x amount of money from personal to bank account
  Transfer_from_bank (x) #transfers x amount of money from bank to personal (don't forget AccountCheck)
  Change_Banks(name1,name2): transfers from one bank to another; bank account remains the same but still requires a new AccountCheck. Customer is removed from original bank (name1)'s list and added to the new bank (name2)'s
'''

class Bank:
  def __init__(self, balance, minMoney, numCustomers):
    self.balance = balance
    self.minMoney = minMoney
    self.numCustomers = numCustomers
  def loanMoney(self, cus, moneyAmt):
    self.balance = self.balance - moneyAmt
    cus.account = cus.account + moneyAmt
  def updateBalance(self, amt):
    self.balance = self.balance + amt
    return self.balance
  def updateNumCustomers(self):
    return self.numCustomers
  def accountCheck(self, cus):
    if(cus.account < self.minMoney):
      cus.memberStatus = False
      cus.pFund = cus.pFund + cus.account
      cus.account = 0

class Customer:
  def __init__(self, pFund, account, memberStatus):
    self.pFund = pFund
    if(memberStatus):
      self.account = account
    else:
      self.account = 0
    self.memberStatus = memberStatus
  def startAccount(self, b):
    if(b.minMoney<=self.pFund):
      self.memberStatus = True
      self.account = self.account + b.minMoney
      self.pFund = self.pFund - b.minMoney
      b.numCustomers = b.numCustomers + 1
    else:
      print("not enough money")
  def transferFromPersonal(self, x):
    if(self.pFund>=x):
      self.account = self.account + x
      self.pFund = self.pFund - x
    else:
      print("not enough money")
  def transferFromBank(self, x):
    if(self.account>=x):
      self.pFund = self.pFund + x
      self.account = self.account - x
    else:
      print("not enough money")
  def switchBanks(self, b1, b2):
    b1.numCustomers = b1.numCustomers - 1
    b2.numCustomers = b2.numCustomers + 1
    b2.accountCheck(b2, self)
aa = Bank(5000, 100, 5)
print(aa.minMoney)
