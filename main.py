from abc import ABC, abstractmethod


class Ride(ABC):

    def __init__(self, distance_km: float):
        self.distance_km = distance_km
        self.is_completed = False

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def start_ride(self):
        pass

    @abstractmethod
    def complete_ride(self):
        pass

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

class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0 
        self.__total_trips = 0

    def add_rating(self, new_rating):
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Rating must be between 1.0 and 5.0")
        
        self.__rating = (self.__rating * self.__total_trips + new_rating) / (self.__total_trips + 1)
        self.__total_trips += 1

    @property
    def rating(self):
        return round(self.__rating, 2)

    @property
    def total_trips(self):
        return self.__total_trips

    def print_rating_info(self):
        print(f"Driver: {self.name}, Average Rating: {self.__rating:.2f}, Total Trips: {self.__total_trips}")
