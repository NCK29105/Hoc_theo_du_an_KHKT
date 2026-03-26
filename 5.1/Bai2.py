class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number   
        self.__balance = balance                

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Nạp {amount} thành công.")
        else:
            print("Số tiền không hợp lệ.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Rút {amount} thành công.")
            else:
                print("Không đủ tiền.")
        else:
            print("Số tiền không hợp lệ.")

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("123456789", 1000)

    print("Số tài khoản:", acc.get_account_number())
    print("Số dư ban đầu:", acc.get_balance())

    acc.deposit(500)
    acc.withdraw(300)

    print("Số dư hiện tại:", acc.get_balance())