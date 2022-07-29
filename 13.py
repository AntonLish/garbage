class Shape():
    def what_am_i(self):
        print("я - фігура")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w
        
    def calculate_perimeter(self):
        a = (self.len+self.width)*2
        print("периметр дорівнює: {}".format(a))
        
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def  change_size2(self, size):
        self.side += size
        
    def calculate_perimeter(self):
        b = (self.side)*4
        print("периметр дорівнює: {}".format(b))
        
rectangle = Rectangle(10, 20)
square = Square(10)

#rectangle.calculate_perimeter()

#square.change_size2(-5)
#square.calculate_perimeter()

#rectangle.what_am_i()
#square.what_am_i()

class Horse():
    def __init__(self, name):
        self.name = name

class Rider ():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse
        
h1 = Horse("кобила")

the_rider = Rider("John", h1)


print(the_rider.horse.name)
