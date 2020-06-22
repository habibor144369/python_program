def function(x, z, y = 10):
    print('x =', x, 'y =', y, 'z =', z)

function(x = 1, y = 2 , z = 5)
a = 5
b = 6
function(x = a, z = b)
a = 1
b = 2
c = 3
function(y = a, z = b, x = c)
