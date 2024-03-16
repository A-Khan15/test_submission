print("""
      This program allows you to divide two numbers, please enter 0 as the second number to exit the loop.
      """)
while True:

    Value1 = float(input("Please enter number 1: "))
    Value2 = float(input("Please enter number 2: "))

    if Value2 == 0:
        print("Divisor can't be 0, program closing.")
        break

    def division(a,b):
        return f"{a/b:.2f}"

    print(division(Value1,Value2))