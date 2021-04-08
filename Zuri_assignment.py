class Budget:

    def __init__(self, budget_category, total_amount=0):
        self.budget_categeory = budget_category
        self.total_amount = total_amount

    def deposit(self, amount):
        # Method to deposit funds to budget
        self.total_amount = self.total_amount + amount

    def withdraw(self, amount):
        # Method to withdraw funds from budget
        self.total_amount = self.total_amount - amount
    
    def balance(self):
        # Method to return budget balance
        return self.total_amount

    def transfer_balance(self, budget_object):
        # Method to transfer balance to another budget class
        transfer_amount = self.balance()
        budget_object.total_amount = transfer_amount
        self.total_amount = transfer_amount - self.total_amount

budget1 = Budget('food')
budget2 = Budget('cloth')
budget2.deposit(20000)
budget2.withdraw(10000)
print(budget2.balance())
budget2.transfer(budget1)
print(budget2.balance())
print(budget1.balance())