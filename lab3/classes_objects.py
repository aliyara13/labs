class My_shape:
    def __init__(self, color="red", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0


class Rectangle(My_shape):
    def __init__(self, color="blue", is_filled=False, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle - {self.color}, Filled: {self.is_filled}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}"


class Circle(My_shape):
    def __init__(self, color="green", is_filled=True, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return 3.14159 * self.radius ** 2  

    def __str__(self):
        return f"Circle - {self.color}, Filled: {self.is_filled}, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}"



color = input("Enter the color of the rectangle: ")
is_filled = input("Is the rectangle filled? (True/False): ")
x_top_left = int(input("Enter the x-coordinate of the top-left corner: "))
y_top_left = int(input("Enter the y-coordinate of the top-left corner: "))
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))


rectangle = Rectangle(color, is_filled, x_top_left, y_top_left, length, width)


print("Rectangle Details:")
print(rectangle)