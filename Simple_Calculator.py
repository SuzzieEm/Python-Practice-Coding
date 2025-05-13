# Taking two numbers, adding them together and printing the results
Num1 = float (input("input first number"))
Num2 = float (input("input second number"))
operation = ("+")
result = (Num1 + Num2)
print(result)

# Subtracting first number from second number
result_sub = (Num1 -Num2)
print(result_sub)

#Multiplying two numbers
result_mul = (Num1*Num2)
print(result_mul)

# Multiplying two numbers
result_div = (Num1/Num2)
print(result_div)

#Performing a modulus operation with two numbers
result_mod = (Num1 % Num2 == 0)
print(result_mod)

# Allowing users to choose which operation they want to perform on two numbers
Num1 = float (input("input first number"))
Num2 = float (input("input second number"))
operation = input ("choose an operation (+, -, *, / )")
if operation == "+":
    result1 = Num1 + Num2
    print(result1)
elif operation == "-":
    result2 = Num1 - Num2
    print(result2)
elif operation == "*":
    result3 = Num1 * Num2
    print(result3)
elif operation == "/":
    if Num2 != 0:
        result4 = (Num1 / Num2)
        print(result4)
    else:
        print("Cannot be divided by zero")
else:
    print("Syntax Error")





