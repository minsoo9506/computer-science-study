def main():
    print("Hello world")

    score1, score2 = input("Enter two score : ").split()
    average = (int(score1) + int(score2)) / 2

    print("The average is : ", average)


main()

# class 이용


class HelloWorld:
    def __init__(self):
        print("Hello world")


def main():
    world = HelloWorld()
    world


main()
