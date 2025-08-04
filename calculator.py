import math
def evaluate_value(val):
    val = val.lower().strip()
    try:

        if val.startswith("sqrt"):
            num = float(val.split()[1])
            if num < 0:
                return "Invalid input for square root"
            return math.sqrt(num)

        elif val.startswith("fact"):
            num = int(val.split()[1])
            if num < 0:
                return "Invalid number for factorial"
            return math.factorial(num)

        elif "%" in val and "of" in val:
            percent = float(val.split('%')[0].strip())
            of_value = float(val.split('of')[1].strip())
            return (percent / 100) * of_value

        # Power: "power 2^5"
        elif val.startswith("power"):
            _, base, exponent = val.split()
            return float(base) ** float(exponent)
     
        else:
            allowed_chars = "0123456789+-*/().% "
            for char in val:
                if char not in allowed_chars:
                    return "Invalid characters in expression"
            return eval(val)

    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("\n CALCULATOR ")
    print("  ➤ Basic expressions: (a + b) * c")
    print("  ➤ Square root: sqrt a")
    print("  ➤ Factorial: fact a")
    print("  ➤ Percentage: a% of a")
    print("  ➤ Power: power a b")
    print("Type 'exit' to quit")

    while True:
        val = input("\nEnter expression: ").strip()
        if val.lower() == 'exit':
            print("Exiting Calculator.")
            break
        result = evaluate_value(val)
        print("Result:", result)

if __name__ == "__main__":
    main()