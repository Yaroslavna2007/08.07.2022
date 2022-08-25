n = int(input('длинна меньшего борта'))
m = int(input('длина большего борта'))
y = int(input('расстояние до меньшего борта'))
x = int(input('расстояние до большего борта'))
z = m - y
v = n - x
if y < z and y < x and y < v:
    print(y)
elif v < y and v < z and v < x:
    print(v)
elif x < y and x < z and x < v:
    print(x)
elif z < x and z < y and z < v:
    print(z)