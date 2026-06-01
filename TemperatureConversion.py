choice=int(input("Enter the option number:\n1.Celsius to Farenheit\n2.Farenheit to Celsius\n3.Celsius to Kelvin\n4.Kelvin to Celsius\n5.Farenheit to Kelvin\n6.Kelvin to Farenheit\n"))

if choice==1:
    C=float(input("Enter the Celsius value: "))
    F=(C*(9/5))+32
    print("Farenheit:",F)
elif choice==2:
    F=float(input("Enter the Farenheit value: "))
    C=(F-32)*(5/9)
    print("Celsius:",C)
elif choice==3:
    C=float(input("Enter the Celsius value: "))
    K=C+273.15
    print("Kelvin:",K)
elif choice==4:
    K=float(input("Enter the Kelvin value: "))
    C=K-273.15
    print("Celsius:",C)
elif choice==5:
    F=float(input("Enter the Farenheit value: "))
    K=(F-32)*(5/9)+273.15
    print("Kelvin:",K)
elif choice==6:
    K=float(input("Enter the Kelvin value: "))
    F=(K-273.15)*(9/5)+32
    print("Farenheit: ",F)
else:
    print("Invalid choice!!")