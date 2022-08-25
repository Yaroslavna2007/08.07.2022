k = int(input('введите число от 1 до 10'))
x = k//2
y = k - x -1
m = 45 * k + x * 5 + y * 15
v = m // 60
c = 9 + v
print(c, ':', m - (60 * v))