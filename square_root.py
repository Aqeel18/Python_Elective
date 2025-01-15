n = float(input("Enter a number: "))
if n < 0:
    print("square root of a negative number cannot be found.")
else:
    if n == 0:
        result = 0
    else:
        val = n / 2
        while True:
            nextval = (val + n / val) / 2
            if abs(nextval - val) < 10**-7:
                result = nextval
                break
            val = nextval
    print("The square root of", n, "is", result)
