a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
mod_sum=((a%c)+(b%c))%c
mod_sub=((a%c)-(b%c)+c)%c
mod_mul=((a%c)*(b%c))%c
print("Modular Addition: ",mod_sum)
print("Modular Sutraction: ",mod_sub)
print("Modular Multiplication: ",mod_mul)