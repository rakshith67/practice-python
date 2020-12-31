import pytz
import datetime


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.transaction_list = []
        if balance > 0:
            self.transaction_list.append((Account._current_time(), balance))
        print("Account created for" + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than 0 and less than your account balance")

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction_list(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time is {})".format(amount, trans_type, date, date.astimezone()))


if __name__ == "__main__":
    rakshith = Account("Rakshith", 0)
    rakshith.show_balance()
    rakshith.deposit(1000)
    rakshith.withdraw(500)
    rakshith.withdraw(1000)
    rakshith.show_transaction_list()

    rakshith2 = Account("Rakshith", 5000)
    rakshith2.deposit(1000)
    rakshith2.withdraw(500)
    rakshith2.__balance = 40  # name mingling doesn't occurs if variable name ends with 2 underscores
    rakshith2.show_transaction_list()
    rakshith2.show_balance()
