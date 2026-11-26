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

from base_ride import Ride


class StandardRide(Ride):
    def __init__(self, distance_km):
        super().__init__(distance_km)
        self.__base_rate = 5.00

    def calculate_fare(self):
        return self.__base_rate + (self.distance_km * 1.50)

    def start_ride(self):
        print(f"Starting a standard ride for {self.distance_km} km.")

    def complete_ride(self):
        print(f"===STANDARD RECEIPT===\nFare: Php{self.calculate_fare():.2f}")
from ride import Ride

class PremiumRide(Ride):

    def __init__(self, distance_km, snack):
        super().__init__(distance_km)

        self.__premium_base_rate = 15.00
        self.__complimentary_snack = snack

    def calculate_fare(self):
        return self.__premium_base_rate + (self.distance_km * 3.00)

    def start_ride(self):
        print("Starting VIP Premium Ride. Enjoy your snacks!")

    def complete_ride(self):
        print("=== VIP RECEIPT ===")
        print(f"Distance: {self.distance_km} km")
        print(f"Fare: Php {self.calculate_fare():.2f}")
        print(f"Complimentary Snack: {self.__complimentary_snack}")

from premium_ride import PremiumRide

vip = PremiumRide(10, "Chocolate Bar")

vip.start_ride()

# Complete the ride
vip.complete_ride()


class RideDispatcher:
    def process_ride_request(self, ride_list):
        print("--- Dispatching Ride Queue ---")

        total_revenue = 0.0

        for ride in ride_list:
            ride.start_ride()
            total_revenue += ride.calculate_fare()
            ride.complete_ride()

        print(f"Total Revenue for this batch: php{total_revenue:.2f}")
        return total_revenue

