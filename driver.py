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