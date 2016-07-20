from pylab import*
x=linspace(0,2*pi,400)
y=sin(x)
i=3
n=0
while (n<100):
    y=y+(1.0/i)*sin(i*x)
    i += 2
    n += 1
plot(x,y)
show()
