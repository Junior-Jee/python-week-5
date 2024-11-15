# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Subclass: Jets
class Jets(Vehicle):
    def move(self):
        return "Flying at supersonic speeds ✈️🚀"

# Example usage
vehicles = [Car(), Plane(), Boat(), Jets()]
for vehicle in vehicles:
    print(vehicle.move())
