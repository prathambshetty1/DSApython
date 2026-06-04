try:
    num=int(input("Enter a number: "))
    res=100/num
    print("Result: ",res)
except ZeroDivisionError:
    print("Error CAnnot divide by zero")
except Exception as e:
    print("Something went wrong",e)
finally:
    print("Done")