def check_fibonaci():
    n = int(input("Enter number for fibanoci series: "))
    a = 0
    b = 1
    sum = 0
    count = 1
    print("Fibonacci Series: ", end = " ")
    while(count <= n):
        print(sum, end = " ")
        count += 1
        a = b
        b = sum
        sum = a + b
        

