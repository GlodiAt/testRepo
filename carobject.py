class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        
    def accelerate(self, increment):
        self.speed += increment
        
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
            
    def get_speed(self):
        return self.speed

# Usage
my_car = Car("Toyota", "Camry", 2020, "Blue")
print(f"My car is a {my_car.year} {my_car.make} {my_car.model} in {my_car.color} color.")
print("Current speed:", my_car.get_speed())
my_car.accelerate(20)
print("Accelerating... Current speed:", my_car.get_speed())
my_car.brake(10)
print("Braking... Current speed:", my_car.get_speed())
