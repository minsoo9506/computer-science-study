# class
class Home:
    colorRoof = 'red'

    def paintRoof(self, color):
        self.colorRoof = color

    def printRoof(self):
        print(self.colorRoof)


home1 = Home()
home2 = Home()
home1.printRoof()
home2.paintRoof('blue')
home2.printRoof()

# Important Methods in class
# - constructor, destructor


class Home:
    colorRoof = 'red'

    def paintRoof(self, color):
        self.colorRoof = color

    def printRoof(self):
        print(self.colorRoof)

    def __init__(self, strAddress):  # constructor
        print('Address:', strAddress)

    def __del__(self):  # Deconstructor
        print('BAMM')


myHome = Home('Seoul')
myHome.printRoof()
del myHome  # BAMM 나온다
