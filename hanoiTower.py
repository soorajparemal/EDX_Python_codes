def move(fr,to):
	print('Move from ' + str(fr) + 'to' + str(to))
def Towers(n,fr,to,spare):
	if n==1:
	   move(fr,to)
	else:
	   Tower(n-1,fr,spare,to)
	   Tower(1,fr,to,spare)
	   Tower(n-1,spare,to,fr)

