#Задание 1
b = input('Введите строку: ')
b = b.lower() #Делаем нижний регистр
b = b.replace(' ','') #Убираем лишние пробелы
if b == b[::-1]: #сравниваем с перевернутым словом
    print('Да')
else:
    print('Нет')

#Задание 2
m = [] #создаем список
s = ['end'] #ключ стопер
while True:
    n = input().split() #вводим через сплит
    k = min(n) #ищем минимальное
    if n == s:
        break
    m.append(k) #вносим в массив
for i in m: #выводим красиво
    print(i)

#Задание 3
m = [] #список
d = {} #словарь
n = str(input())
m.append([str(s.lower()) for s in n.split()])
li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j] #конкретное число в массиве
        if p in d:
            d[p]+=1 #выполняем поставленное условние
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)

#Задание 4
import pymysql

connect = pymysql.connect( #конектимся к MySQL
    host='localhost',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cur = connect.cursor() #описываем курсор
year= int(input('Введите год: ')) #вводим год (обязательно int)
s = year
cur.execute(' select first_name,last_name,date_of_birth from user where year(date_of_birth) = %s',s)
for rec in cur: #вывод результата
    print(rec[0],rec[1],rec[2]) #rec0 = first name и тд.