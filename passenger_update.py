
class PassengerAccount:

    def __init__(self, name):
        self.name = name  
        self.__wallet_balance = 0.0  

    def top_up_wallet(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        self.__wallet_balance += amount

        print(f"Successfully added ₱{amount:.2f}!")
        print(f"Current balance: ₱{self.__wallet_balance:.2f}")

    def pay_for_ride(self, fare_amount):
        if fare_amount < 0:
            raise ValueError("Fare cannot be negative.")

        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")

        self.__wallet_balance -= fare_amount

        print("Payment successful!")
        print(f"Remaining balance: ₱{self.__wallet_balance:.2f}")

    @property
    def wallet_balance(self):
        return self.__wallet_balance
