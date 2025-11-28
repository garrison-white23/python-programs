class BankAccount:
    def __init__(self, owner):
        self.name = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw (self, amount):
        self.balance -= amount
    def show_balance(self):
        print(f"\nCurrent balance: ${self.balance}")
        

def main():
    owner = BankAccount(input("Enter your name: "))
    menu(owner)
    print("Goodbye!")
    
    
def menu(owner):
    while True:
        option = input("\nChoose an option:\n[1]Deposit\n[2]Withdraw\n[3]View Balance\n[4]Quit\n>")
        if option in ["1", "2", "3", "4"]:
            if option == "4":
                break
            if option == "3":
                owner.show_balance()

            if option == "1":
                deposit_money(owner)
            if option == "2":
                withdraw_money(owner)
            if option == "3":
                owner.show_balance()
        else:
            print("Invalid input. Try again.")
            
            
def deposit_money(owner):
    amount = float(input("\nEnter amount to deposit: $"))
    owner.deposit(amount)
    print("Deposit successful!")
    
    
def withdraw_money(owner):
    while True:
        try:
        amount = float(input(f"\nEnter amount to withdraw (Current balance: ${owner.balance}): $"))
        if amount <= owner.balance:
            break
        else:
            print(f"Can't exceed current balance (${owner.balance}). Try again.")
    
    owner.withdraw(amount)
    print("Withdrawl successful.")
    
            
if __name__ == "__main__":
    main()
