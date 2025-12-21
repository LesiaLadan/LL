print('1. Квадрат числа.')
print()
x = float(input('Enter a number to square: '))
print()

result = x ** 2

if result.is_integer():
    print(int(x), 'squared equals', int(result))
else:
    print(( x, 'squared equals', result))
print()


print('2. Середнє трьох чисел.')
print()
x = float(input('To calculate the average of three numbers, enter the first number: '))
print()
y = float(input('Enter second number: '))
print()
z = float(input('Enter third number: '))
print()

result = (x + y + z) / 3

x = int(x) if x.is_integer() else x
y = int(y) if y.is_integer() else y
z = int(z) if z.is_integer() else z
result = int(result) if result.is_integer() else result

print('The average of', x,',', y, 'and', z, 'equals', result)
print()


print('3. Перетворення хвилин у години')
print()
minutes_total = int(input('Enter the number of minutes: '))
print()

hours, minutes = divmod(minutes_total, 60)

print(minutes_total, 'minutes equals', hours,'h and', minutes,'min')
print()


print('4. Розрахунок знижки')
print()
price = float(input("To calculate the total with discount, enter the original price: "))
print()
discount = float(input("Enter the discount percentage (%): " ))
print()

final_price = price - price * discount / 100

print ('Total with discount ', round(final_price, 2))
print()

print('5. Остання цифра числа')
print()
number = int(input('Enter the number: '))
print()

left, right = divmod((abs(number)), 10)

print('The last digit of', number, 'is', right)
print()


print('6. Периметр прямокутника')
print()
lenght = float(input('Enter the length of the rectangle: '))
print()
width = float(input('Enter the width of the rectangle: '))
print()

perimeter = (lenght + width) * 2
if perimeter.is_integer():
    print('The perimeter of the rectangle is', int(perimeter))
else:
    print('The perimeter of the rectangle is', (perimeter))
print()


print('7. Виведення числа в стовпчик')
print()

number = int(input('Enter the 4-digit number: '))
a, left = divmod(number, 1000)
b, left = divmod(left,100)
c, d = divmod(left,10)
digits = [a, b, c, d]
for digit in digits:
    print(digit)


