
# Creates the PassengerAccount class!
class PassengerAccount:

    # Constructor: initializes a passenger's account!
    def __init__(self, name):
        self.name = name  # Stores the passenger's name
        self.__wallet_balance = 0.0  # Private wallet balance, starts at 0.0

    # Method for adding money to the passenger's wallet!
    def top_up_wallet(self, amount):

        # This checks if the top-up amount is negative!
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        # Adds the amount to the existing wallet balance
        self.__wallet_balance += amount

        # Displays the successful top-up and updated balance
        print(f"Successfully added ₱{amount:.2f}!")
        print(f"Current balance: ₱{self.__wallet_balance:.2f}")

    # Method for paying the fare of a ride
    def pay_for_ride(self, fare_amount):

        # Prevents negative ride fares
        if fare_amount < 0:
            raise ValueError("Fare cannot be negative.")

        # Checks if the passenger has enough money
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")

        # Deducts the ride fare from the wallet balance
        self.__wallet_balance -= fare_amount

        # Displays the successful payment and remaining balance
        print("Payment successful!")
        print(f"Remaining balance: ₱{self.__wallet_balance:.2f}")

    # Property that allows the wallet balance to be viewed
    # without directly modifying the private attribute
    @property
    def wallet_balance(self):
        return self.__wallet_balance
