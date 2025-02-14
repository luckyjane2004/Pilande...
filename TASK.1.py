class Car:
    def __init__(self, brand, model, year):
        self.brand = brand   # Attribute for the car's brand name
        self.model = model    # Attribute for the car's model
        self.year = year      # Attribute for the car's year

    def display_info(self):
        # Method to display car information
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Creating an object (instance) of the Car class
my_car1 = Car("Porsche", "718 Cayman", 2024)

my_car2 = Car("BMW", "Z4", 2025)
# Accessing attributes and calling a method
my_car1.display_info()
my_car2.display_info()