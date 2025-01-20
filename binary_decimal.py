binary_no=input("Enter Binary number: ")
length=len(binary_no)
dec=0
for i in range(length):
    dec+=int(binary_no[length-i-1])*int(2**i)
print(dec)