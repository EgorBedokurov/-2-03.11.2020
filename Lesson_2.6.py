z=int(input('введите число кратное "10" '))
x=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
if abs(z) in x:
    print('yes')
else:
    print('no')