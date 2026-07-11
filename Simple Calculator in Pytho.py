# Simple Menu-Driven Calculator in Python

def calculator():
    print("=" * 40)
    print(" SIMPLE CALCULATOR")
    print("=" * 40)
    
    while True: 
        
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        
        if choice == '6':
            print("Exiting Calculator. Goodbye!")
            break
        
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice! Please enter a number between 1 to 6.")
            continue
        
        # Get numbers from user
        numbers = []
        print("Enter numbers. Type 'done' when finished.")
        while True:
            num = input("Enter number: ")
            if num.lower() == 'done':
                break
            try:
                numbers.append(float(num))
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        if len(numbers) < 2:
            print("Please enter at least 2 numbers.")
            continue
            
        result = numbers[0]
        
        
        if choice == '1': 
            for num in numbers[1:]:
                result += num
            print(f"Result: {' + '.join(map(str, numbers))} = {result}")
                
        elif choice == '2': 
            for num in numbers[1:]:
                result -= num
            print(f"Result: {' - '.join(map(str, numbers))} = {result}")
                
        elif choice == '3': # Multiplication
            for num in numbers[1:]:
                result *= num
            print(f"Result: {' * '.join(map(str, numbers))} = {result}")
                
        elif choice == '4': # Division
            for num in numbers[1:]:
                if num == 0:
                    print("Error: Division by zero is not allowed!")
                    result = None
                    break
                result /= num
            if result is not None:
                print(f"Result: {' / '.join(map(str, numbers))} = {result}")
                
        elif choice == '5': # Modulus
            for num in numbers[1:]:
                if num == 0:
                    print("Error: Modulus by zero is not allowed!")
                    result = None
                    break
                result %= num
            if result is not None:
                print(f"Result: {' % '.join(map(str, numbers))} = {result}")


calculator()