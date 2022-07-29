#12.1
class Apple():
    def __init__(self, sort, color, price, number):
        self.sort = sort
        self.color = color
        self.price = price
        self.number = number
antonivka = Apple("Антонівка", "білий", "1$", "100")
print(antonivka.color)
#12.2
import math
class Circle():
    def __init__(self, rad):
        self.rad = rad
        
    def area(self):
        return (self.rad**2)*math.pi
    
crl1 = Circle(5)
crl2 = Circle(232)
crl3 = Circle(2.2)
print(crl1.area())
print(crl2.area())
print(crl3.area())

#12.3
class Triangle():
    def __init__(self, kat1, kat2, ang1):
        self.kat1 = kat1
        self.kat2 = kat2
        self.ang1 = ang1
    def area_t(self):
        return (self.kat1 * self.kat2 * math.sin(self.ang1))/2
triangle1 = Triangle(5, 5, 1.57)
print(triangle1.area_t())

#12.4

class Hexagon():
    def __init__(self, side):
        self.side = side
    def calculate_perimeter(self):
        return self.side * 6
    
hexagon_test = Hexagon(10)

print(hexagon_test.calculate_perimeter())
