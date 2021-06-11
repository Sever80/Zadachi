# С клавиатуры вводится 5 значное число.
# Если четных цифр в нем больше, чем нечетных,
# то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 и 5 цифры.
import math
# number=[2,2,3,4,5]
a=input('Введите пятизначное число:')
b=[]
for i in a:
    b.append(int(i))
print(b)

cht=0
ncht=0

for i in b:
    if i%2==0:
        cht+=1
    else:
        ncht+=1
print('Кол-во чётных:', cht)
print('Кол-во нечётных:',ncht)
s=0

if cht>ncht:
    for i in b:
        s+=i
    print('Сумма чисел:',s)
elif cht<ncht:
    pr=b[0]*b[4]
    print('Произведене 1 и 5 цифры:', pr)