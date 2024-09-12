# Antarmuka yang memaksa setiap bangun datar untuk memiliki metode luas dan keliling
class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

# Persegi mengimplementasikan kedua metode
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side

# Lingkaran dipaksa untuk mengimplementasikan keliling meskipun mungkin tidak selalu dibutuhkan
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# Penggunaan
square = Square(4)
circle = Circle(5)

print("Square Area:", square.calculate_area())
print("Square Perimeter:", square.calculate_perimeter())

print("Circle Area:", circle.calculate_area())
print("Circle Perimeter:", circle.calculate_perimeter())  # Tidak selalu dibutuhkan
