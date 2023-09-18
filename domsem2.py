#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть
x = int(input())

s_orel = 0
s_resh = 0

for i in range(x):
    side = int(input())
    if side == 1:
        s_resh+=1
    else:
        s_orel+=1
print(min(s_orel,s_resh))
      
#Задача 12: Найти два числа до 1000,
# где s-сумма чисел а p-произведение

#s = int(input())
#p = int(input())
#find = False
#for x in range(1000):
#    for y in range(1000):
#        if x+y == s and x*y == p:
#            print(x,y)
#            find = True
#            break
#    if find:
#        break
#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#не превосходящие числа N.

#n = int(input())
#res = 1
#while res < n:
#    print(res, end =" ")
#    res *= 2