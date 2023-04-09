n = int(input('Enter a six-digit number: '))

while n < 100000 or n > 999999:
    n = int(input('Enter a six-digit number: '))
print(n)

sum1 = 0
sum2 = 0
while n != 0:
    if n > 999:
        sum1 += n % 10
    else:
        sum2 += n % 10
    n //= 10

if sum1 == sum2:
    print(f'{sum1} = {sum2} - Happy!')
else:
    print(f'{sum1} != {sum2} - Not happy.')
