# import math

# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def subtract(self,a,b):
#         return a-b
#     def multiply(self,a,b):
#         return a*b
#     def divide(self,a,b):
#         if b==0:
#             return "division by zero is not possible "
#         else:
#             return a/b
#     def modulus(self,a,b):
#         return a%b
   
#     def power(self,a,b):
#         return a**b
    
#     def squareroot(self,a):
#         if (a<0):
#             return "NO. is not valid for square root"
#         else:
#             return math.sqrt(a)
    
#     def factorial(self, a):
#         if a<0:
#             return"Entered no. is not valid "
#         elif a==0 or a==1:
#             return 1
#         else:
#             f= 1
#             for i in range(1,a+1):
#                 f *= i
#             return f

# def show_menu():
#     print("  full calculator  ".upper())
#     print("1. addition")
#     print("2. subtraction")
#     print("3. multiplication")
#     print("4. division")
#     print("5. power")
#     print("6. square Root")
#     print("7. factorial")
#     print("8. modulus")
#     print("9. exit")
    
# calc = Calculator()

# while True:
#     show_menu()
#     choice = input("Enter your choice (1-9): ")
    
#     if choice =='9':
#         print("exiting the calculator ")
#         break
#     elif choice not in [str(i) for i in range(1,10)]:
#         print("invalid choice, try agian")
#         continue
#     elif choice in ['1','2','3','4','5','8']:
#         a=float(input("enter the first number: "))
#         b=float(input("enter the second number: "))
        
#         if choice =='1':
#             print(f"result:{calc.add(a,b)}")
#         elif choice =='2':
#             print(f"result:{calc.subtract(a,b)}")
#         elif choice =='3':
#             print(f"result:{calc.multiply(a,b)}")
#         elif choice =='4':
#             print(f"result:{calc.divide(a,b)}")
#         elif choice =='5':
#             print(f"result:{calc.power(a,b)}")
#         elif choice =='8':
#             print(f"result:{calc.modulus(a,b)}")
        
#     elif choice in ['6','7']:
#         a=float(input("enter the number: "))
#         if choice =='6':
#             print(f"result:{calc.squareroot(a)}")
#         elif choice =='7':
#             print(f"result:{calc.factorial(a)}")



import math

class Calculator:
    
    def add(self, *args):
        return sum(args)

    def subtract(self, *args):
        if not args:
            return "No numbers entered"
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, *args):
        if not args:
            return "No numbers entered"
        result = args[0]
        try:
            for num in args[1:]:
                if num == 0:
                    return "Division by zero is not possible"
                result /= num
            return result
        except Exception as e:
            return str(e)

    def modulus(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

    def squareroot(self, a):
        if a < 0:
            return "Number is not valid for square root"
        else:
            return math.sqrt(a)

    def factorial(self, a):
        if a < 0:
            return "Entered number is not valid"
        elif a == 0 or a == 1:
            return 1
        else:
            f = 1
            for i in range(1, a + 1):
                f *= i
            return f

def show_menu():
    print("  FULL CALCULATOR  ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Modulus")
    print("9. Exit")

calc = Calculator()

while True:
    show_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == '9':
        print("Exiting the calculator.")
        break

    elif choice not in [str(i) for i in range(1, 10)]:
        print("Invalid choice, try again.")
        continue

   
    elif choice in ['1', '2', '3', '4']:
        numbers = input("Enter numbers separated by space: ")
        args = list(map(float, numbers.split()))
        if choice == '1':
            print(f"Result: {calc.add(*args)}")
        elif choice == '2':
            print(f"Result: {calc.subtract(*args)}")
        elif choice == '3':
            print(f"Result: {calc.multiply(*args)}")
        elif choice == '4':
            print(f"Result: {calc.divide(*args)}")

    elif choice == '5':
        a = float(input("Enter the base number: "))
        b = float(input("Enter the exponent: "))
        print(f"Result: {calc.power(a, b)}")

    elif choice == '8':
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"Result: {calc.modulus(a, b)}")

    elif choice == '6':
        a = float(input("Enter the number: "))
        print(f"Result: {calc.squareroot(a)}")

    elif choice == '7':
        a = int(input("Enter the number: "))
        print(f"Result: {calc.factorial(a)}")
