def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a=int(input("Enter the a value: "))
b=int(input("Enter the b value: "))
print("GCD: ",gcd(a,b))