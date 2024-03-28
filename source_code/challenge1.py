class Patterns:

    def right_half_pyramid(self):
        # Right Half  Pyramid
        print("*\n* *\n* * *\n* * * *\n* * * * *")
        print()

    def reverse_half_pyramid(self):
        # Reverse Right Half pyramid
        print("* * * * *\n* * * * \n* * *\n* *\n*")

    def left_half_pyramid(self):
        # Left Half Pyramid
        print("        *\n      * *\n    * * *\n  * * * *\n* * * * *")


patterns = Patterns()
f"{patterns.right_half_pyramid()} {patterns.reverse_half_pyramid()} {patterns.left_half_pyramid()}"