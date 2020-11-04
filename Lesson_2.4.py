print('это высокосный год?')
a=int(input())
d=a%4
c=a%100
if c!=0 and d==0:
    print('YES')
elif d!=0 and c==0:
    print('NO')
else:
    print('NO')


#вместо переменной "а" вводил "х" - почемуто выдает ошибку