class Figure:
    unit = "cm"
    def __init__(self):
        pass
    
    def calculate_area(self):
        pass
    
    def info(self):
        pass
    
class Square(Figure):
    
    def __init__(self, side_length):
        super().__init__
        self.__side_length = side_length
        
    def calculate_area(self):
        if type(self.__side_length) == int and self.__side_length > 0:  
            return f"Area of square: {self.__side_length ** 2}{Figure.unit}"
        else:
            return ValueError("Invalid type ot invalid input")
    
    def info(self):
        return f"Square side length: {self.__side_length}{Figure.unit}, area: {self.__side_length ** 2}{Figure.unit}."
    
class Rectangle(Figure):
    
    def __init__(self, length, width):
        super().__init__
        self.__length = length
        self.__width = width
        
    def calculate_area(self):
        if type(self.__side_length) == int and self.__side_length > 0:  
            return f"Area of rectangle: {self.__length * self.__width}{Figure.unit}"
        else:
            return ValueError("Invalid type ot invalid input")
    
    def info(self):
        return f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit},  area: {self.__length * self.__width}{Figure.unit}"
    
    
figures_array = [
    Square(20),
    Square(15),
    Rectangle(10, 5),
    Rectangle(20, 8),
    Rectangle(3, 2)
]

for figure in figures_array:
    print(figure.info())