def main():
  print("Hello learners!")

if __name__=="__main__":
  main()

# Adding multiple numbers
def addmultiplenumbers(numbers):
  return sum(numbers)

# Multiplying multiple numbers
def multiplymultiplenumbers(numbers):
  result = 1
  for num in numbers:
    result *= num
  return result
  
  # Checking for even numbers
def isiteven(number):
  if isinstance(number, int) and number % 2 == 0:
    return True
  else:
    return False
  
  #Checking for integers
def isitaninteger(number):
  if isinstance(number, int):
    return True
  else:
    return False

  
  



