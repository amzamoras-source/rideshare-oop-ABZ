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
