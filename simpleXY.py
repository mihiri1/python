x = 5
y = 2

z = x
x = y
y = z

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

x, y = y, x
print(x)
print(y)