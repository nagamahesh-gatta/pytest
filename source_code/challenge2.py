class User_Input:

    def greet(self):
        name:str = input("Please Enter Your Name: ").strip()
        print(f"Welcome {name.upper()} to KG Coding")

    def add_two_num(self):

        num1 = float(input("Enter Your First Number: "))
        num2 = float(input("Enter Your Second Number: "))

        print("Sum of your number is: ",num1 + num2)


user_input = User_Input()
user_input.greet()
user_input.add_two_num()