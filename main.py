from Programs import armstrong,palindrome,prime,fibonaci

one_dict = {1:armstrong.check_armstrong,
    2:palindrome.check_palindrome,
    3:prime.check_prime_number,
    4:fibonaci.check_fibonaci}
print("1:Armstrong Number, 2:Palindrome Number, 3:Prime Number ,4:Fibonaci Series")
select = int(input("Enter your choice from above: "))
logic = one_dict.get(select)
print(logic())
