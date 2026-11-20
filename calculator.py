def calculator(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        total = args[0]
        for i in args[1:]:
            total -= i
        return total
    elif operator == "/":
        if 0 in args[1:]:
            return "cannot divide by zero"
        total = args[0]
        for i in args[1:]:
            total /= i
        return total
        
    elif operator == "*":
        total = 1
        for i in args:
            total*= i
        return total
    else:
            return ("invalid input")
while True:
    
    operators = input("Enter operator (+, -, *, /) or q for quit: ")
    if operators == "q":
        print("Good bye buddy👋")
        break 
    numbers = input("Enter numbers: ").split()
    if not numbers:
        print("Please enter at least one number!")
        continue
    if len(numbers) < 2:
        print("Please enter at least two number!")
        continue
    try:
       numbers = [float(i) for i in numbers]
    except ValueError:
        print("Please enter valid numbers!")
        continue
    
    result = calculator(operators, *numbers)

    print(result)