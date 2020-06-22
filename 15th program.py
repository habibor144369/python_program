# golobal and local variable with function....
def myfnc(x):
    print('inside myfnc', x)
    x = 10
    print('inside mufnc', x)
x = 30
myfnc(x)
print(x)

# global variable with function....
def myFunction(y):
    print('inside myFunction', y)
    print('inside myFunction', z)

z = 100
myFunction(z)
