number = 1
while number <= 1000:
    if number % 15 == 0:
        print("Fizzbuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    number += 1

