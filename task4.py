# 2x+y = S
# 4x = y
# 6x = S
# x = S/6
# y = 4S/6

s = int(input('Enter S: '))
if s % 6 == 0:
    x = s//6
    y = 4*x
    print(f'Petya = {x}, Serega = {x}, Katya = {y}')
else:
    print('No answer in integer numbers.')
