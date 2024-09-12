from abc import ABC, abstractmethod

# Interface untuk menghitung luas bangun datar
class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Interface untuk menghitung keliling bangun datar
class Perimeter(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

# Persegi mengimplementasikan kedua antarmuka (luas dan keliling)
class Square(Area, Perimeter):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side

# Lingkaran hanya mengimplementasikan antarmuka luas, karena kita tidak butuh keliling dalam kasus ini
class Circle(Area):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Penggunaan
square = Square(4)
circle = Circle(5)

print("Square Area:", square.calculate_area())
print("Square Perimeter:", square.calculate_perimeter())  # Relevant

print("Circle Area:", circle.calculate_area())
# circle.calculate_perimeter() tidak ada karena lingkaran tidak mengimplementasikan Perimeter
