# 🎮 Welcome to the Interactive Fun Calculator! 🎮
# Choose your operation and let's get calculating like pros! 🧮😎

# Step 1: Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Present a menu of operations to the user
print("\nSelect an operation:")
print("1 ➕ Addition")
print("2 ➖ Subtraction")
print("3 ✖️ Multiplication")
print("4 ➗ Division")

# Step 3: Get user's choice
choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

# Step 4: Perform the selected operation
if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\n🚫 Error: You can't divide by zero!")
else:
    print("\n😕 Invalid choice. Please enter 1, 2, 3, or 4.")

# 🎉 Thanks for using the Fun Calculator! 🎉