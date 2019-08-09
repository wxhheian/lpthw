#传参
def optor(x=None,j=None):
    print(x,j)

optor(x='Hello',j='Fine')

options={'x':'Something','j':'Another Thing'}

optor(**options)

def printit(a,b,c,d):
    print(a,b,c,d)

y=[1,2,3,4]
printit(*y)
