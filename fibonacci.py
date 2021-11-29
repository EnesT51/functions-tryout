def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        e = a + b
        a = b
        b = e
        print(e)    
fib(11)