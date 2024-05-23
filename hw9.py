class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)

    def show(self):
        print(f"좌측 상단 꼭지점이 {self.lt.get()}이고 우측 하단 꼭지점이 {self.rb.get()}인 사각형입니다.")

    def getWidth(self):
        return self.rb.x - self.lt.x

    def getHeight(self):
        return self.rb.y - self.lt.y

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

r1 = Rectangle(5, 5, 20, 10) 
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"넓이는 {a}, 둘레는 {p}")
