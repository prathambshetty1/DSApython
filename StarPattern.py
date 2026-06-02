def half_pyramid(rows):
    for i in range(1,rows+1):
        print("* "*i)
def full_pyramid(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i)+"* "*i)
def diamond(rows):
    #upper half
    for i in range(1,rows+1):
        print(" "*(rows-i)+"* "*i)
    #lower half
    for i in range(rows-1,0,-1):
        print(" "*(rows-i)+"* "*i)
rows=int(input("Enter the number of rows: "))
half_pyramid(rows)
full_pyramid(rows)
diamond(rows)