string = input("Enter the String to be Encrypted: ")
key = int(input("Enter the Key: "))
encrypt = ""
for char in string:
    ascvalue = ord(char)
    codevalue = ascvalue + key
    if codevalue > ord('z'): 
        codevalue = ord('a') + (codevalue - ord('z') - 1)
    encrypt += chr(codevalue)
print("Encrypted String:", encrypt)

string = input("Enter the String to be Decrypted: ")
key = int(input("Enter the Key: "))
decrypt = ""
for char in string:
    ascdvalue = ord(char)
    codevalue = ascdvalue - key
    if codevalue < ord('a'): 
        codevalue = ord('z') - (ord('a') - codevalue - 1)
    decrypt += chr(codevalue)
print("Decrypted String:", decrypt)
