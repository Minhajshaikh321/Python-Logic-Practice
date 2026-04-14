#Lower Level Design Question: Design a system to track account balances based on a series of transactions. Each transaction can be a deposit, withdrawal, or transfer between accounts. The system should be able to process a list of transactions and return the final balance for each account.
class AccountBalanceTracker:
  def __init__(self):
    self.balances={}

  def processTransactions(self, transactions):
    print(transactions)
    for txn in transactions:
      parts=txn.split()
      action=parts[0]
      if action == 'DEPOSIT':
        user,amount=parts[1],int(parts[2])
        self.balances[user]=self.balances.get(user,0)+amount

      elif action == 'WITHDRAW':
        user,amount=parts[1],int(parts[2])
        if self.balances.get(user,0)>=amount:
          self.balances[user]-=amount

      elif action == 'TRANSFER':
        snd,dst,amount=parts[1],parts[2],int(parts[3]) #extract source, destination, and amount
        if self.balances.get(snd,0)>=amount:
          self.balances[snd]-=amount
          self.balances[dst]=self.balances.get(dst,0)+amount
  def getUserBalance(self, user):
    return self.balances.get(user,0)

abt = AccountBalanceTracker()
transactions=["DEPOSIT Alice 100","WITHDRAW Alice 30","DEPOSIT Bob 50","TRANSFER Alice Bob 50","WITHDRAW Bob 120"]
abt.processTransactions(transactions)
print(abt.getUserBalance("Alice"))
print(abt.getUserBalance("Bob"))
print(abt.getUserBalance("John"))
