# def check_palindrome():
#   num = input("Enter the number to check palindrome or not: ")
#   if num == num[::-1]:
#     return 'PALINDROME'
#   else:
#     return 'NOT PALINDROME'
def check_palindrome():
    num=int(input("Enter a number:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
        