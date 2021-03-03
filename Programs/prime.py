def check_prime_number():
  num = int(input("Enter the number to check prime or not: "))
  if (num == 1):
    return "1 is neither prime nor composite"
  elif (num <= 0):
    return "Enter valid number"
  else:
    for number in range(2, num):
      if(num % number == 0):
        return "Number is not prime"
        break
    else:
      return "Number is prime"



