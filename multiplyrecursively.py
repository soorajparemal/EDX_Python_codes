x=int(input("Enter the first number : "))
y=int(input("Enter the number to be multiplied with : "))
def fun(a,b):
	if b==1:
	   return a
	else:
	   return a + fun(a,b-1)
print fun(x,y)
