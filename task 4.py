class Hexagon:
    def __init__(self,s):
        self.side = s
    
    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self,s):
        self.__side = s
        return 
    def calArea(self):
        return 1.5*1.732*self.side
    def calcPeri(self):
        return 6*self.side
    def calAngleSum(self):
        return 6*120
    def display(self):
        return f'Area of Hexagon is: {self.calArea()}\n'+f'Perimeter of Hexagon is: {self.calcPeri()}\n'+f'Sum of angles of Hexagon is: {self.calAngleSum()}'
    

class Square:
    def __init__(self,s):
        self.side = s
    
    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self,s):
        self.__side = s
        return 
    def calAreaSquare(self):
        return self.side*self.side
    def calcPeriSquare(self):
        return 4*self.side
    def display(self):
        return f'Area of Square is: {self.calAreaSquare()}\n'+f'Perimeter of Square is: {self.calcPeriSquare()}\n'
    
def main():
    n = int(input('Enter 1 to compute area, perimeter and sum of all angles of Hexagon\nEnter 2 to compute area and perimeter of square\nPress anyother key to exit.'))
    if n == 1:
        hex = Hexagon(8)
        print(hex.display())
    if n == 2:
        sq = Square(9)
        print(sq.display())
main()    