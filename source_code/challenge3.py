class Swapping_Numbers:

    def swapping(self):

        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        num1 = num1 + num2
        num2 = num1 - num2
        num1 = num1 - num2

        print(f"The value of Number1 is: {num1} & The Value of Number2 is: {num2}")


swap = Swapping_Numbers()
swap.swapping()
