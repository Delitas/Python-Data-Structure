"""
Data : 2020-12-18
dev : Python 3.8
Auth : Delitas
"""
print('Ver 1.1')
print('Convert to Decimal(Non int() function)')
print('Author : Delitas')
print('='*20)
numbers = int(input('Input number : '))
base = int(input("Input number's base (1<base<11) : "))

base_temp = 1
covert_num = 0

while(1):
    num_temp = numbers % 10
    if num_temp >= base:
        print('Base Number Error')
        break
    covert_num += num_temp * base_temp
    base_temp *= base
    numbers //= 10
    if numbers == 0:
        print(covert_num)
        break

