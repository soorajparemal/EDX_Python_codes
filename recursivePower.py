x=int(input("Enter the Base number : "))
y=int(input("Enter the exponent number : "))
def recurPower(base,exp):
    if exp == 0:
       return 1
    elif exp==1:
       return base
    else:
       return base*recurPower(base,exp-1)
print recurPower(x,y)
