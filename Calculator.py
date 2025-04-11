print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. **")
print("6. //")
action = input("Eter your desired action: ")
print("----------------------------------------------------------------------")

if action == "1":
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))
    print(num1 + num2)

if action == "2":
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))
    print(num1 - num2)


if action == "3":
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))
    print(num1 * num2)

if action == "4":
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))
    print(num1 / num2)

if action == "5":
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))
    print(num1 ** num2)

if action == "6":
    num1 = float(input("Enter the first digit: "))
    num2 = float(input("Enter the second digit: "))
    print(num1 // num2)
