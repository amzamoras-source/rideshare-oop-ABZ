
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
        self.is_completed = True
        print("=== VIP RECEIPT ===")
        print(f"Distance: {self.distance_km} km")
        print(f"Fare: Php {self.calculate_fare():.2f}")
        print(f"Complimentary Snack: {self.__complimentary_snack}")
