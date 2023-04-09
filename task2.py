n = abs(int(input('Enter a three-digit number: ')))

while n < 100 or n > 999:
    n = abs(int(input('Enter a three-digit number: ')))
print(n)

sum = 0
while n != 0:
    sum += n % 10
    n //= 10
print(sum)
