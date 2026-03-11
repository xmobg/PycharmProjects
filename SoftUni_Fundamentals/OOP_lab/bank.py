class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit_money(self, amount):
        self.__balance += amount

    def withdraw_money(self, amount):
        if amount > self.__balance:
            return "Not enough money"
        self.__balance -= amount
        return f"Withdrew ${amount}"

    def show_balance(self):
        return self.__balance

account_one = Account(100)
print(account_one.show_balance())
account_two = Account(200)
print(account_two.show_balance())
account_one.deposit_money(100)
print(account_one.show_balance())
account_two.deposit_money(200)
print(account_two.show_balance())
account_one.withdraw_money(200)
print(account_one.show_balance())
account_two.withdraw_money(200)
print(account_two.show_balance())