# polymorphism
# - different behavior with similar signture
# - signature = method name + parameter list
# method overriding : 부모 method가 아닌 자식 method가 덮어쓰는
# method overloading : 동일한 이름의 method가 여러가지 일을 한다(input argsㅏ 다르다)

# Abstract Class
# - abstract method : method with signature but with no implementation


class Room:
    def opendoor(self):
        pass


class BedRoom(Room):
    def opendoor(self):
        print("opendoor")


bedroom = BedRoom()
bedroom.opendoor()

# 위의 Room 처럼 상속 받는게 없어도 자동으로 object라는 class 상속
# objecr는 hidden methods가 많다 : __init__, __del__, __eq__, __add__ ...
