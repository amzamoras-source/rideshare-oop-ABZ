
from base_ride import Ride


class PremiumRide(Ride):

    def __init__(self, distance_km, snack):
        super().__init__(distance_km)

        self.__premium_base_rate = 15.00
        self.__complimentary_snack = snack

    def calculate_fare(self):
        return self.__premium_base_rate + (self.distance_km * 3.00)

    def start_ride(self):
        print(f"Starting VIP Premium Ride for {self.distance_km} km. Enjoy your snacks!")

    def complete_ride(self):
        fare = self.calculate_fare()
        self.is_completed = True

        print("=== VIP PREMIUM RECEIPT ===")
        print(f"Distance: {self.distance_km} km")
        print(f"Fare: ₱{fare:.2f}")
        print(f"Complimentary Snack: {self.__complimentary_snack}")
        print("Ride completed successfully.")
