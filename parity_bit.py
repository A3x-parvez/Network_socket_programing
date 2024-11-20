def getparity(n):
    parity = 0
    while n:
        parity =~ parity
        n=n&(n-1)
    return parity
        
n=int(input("Enter n :"))
print("Odd parity"if getparity(n) else "Even parity")