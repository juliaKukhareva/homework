#1 task 
def my_func():
    pass


#2 task
def multiplikation(x):
    total = x * 2
    return total

print (multiplikation(235))

#3 task 
def characteristic (y):
    if y % 2 == 0:
        print ('yes') 
    else:
        print ('no')    

characteristic (77)

#4 task
def func (d=6,c=9):
    if d > 10:
        print ('yes')
    else:
        print ('no')
func (11,6)

#5 task
g = lambda s,v: s%v
print (g (2,6))

#6 task
def decorator(func):
    def wrapper():
        print(";)))")
        func()
        print(":))")
    return wrapper

def say():
    print("Ура!")

say = decorator(say)
say ()

#7 task 
num = [625,225,81]

def square_root (x):
    return x **(1/2)

num = list (map(square_root, num))

print (num)

num = [625,225,81]
def check (x):
    return x ** (1/2) >20
num = list (filter (check, num))
print (num)
 
 
 #8 task 

def pure_function (e,t):
    sum = e+t
    return sum
   
print (pure_function(5,6))    

 

 #9 task 

result = min (2,-23,100,5)
print ('The minimum number is ', result)
result = max (2,-23,100,5)
print ('The maximum number is ', result)

#10 task 
year = int (input ('Введите год: '))

if year % 4 != 0:
    print('Год не високосный.')
else:
    print('Год високосный.')

import calendar
year = int(input('Введите год: '))

if calendar.isleap(year):
    print('Год високосный.')
else:
    print('Год не високосный.')

#11 task

def season (a):
   
    if a == 1 or a == 2 or a == 12:
        return 'Winter'
    elif a == 3 or a== 4 or a== 5:
        return 'Sping'
    elif a == 6 or a== 7 or a==8:
        return 'Summer'
    elif a == 9 or a == 10 or a == 11:
        return 'Autumn'
    else:
        return 'Error'

S = season (int(input('Введите номер месяца: ')))
print (S)

#12 task
from datetime import date
 
def data (y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False
 
print(data (2020,12,12))
print(data (2020,12,32))

#13 task
spisok = [16,-17,2,78.7,False,False,{'True': True},555,12,23,42,'DD']
foo = list(filter(lambda num: type(num) is int or type (num) is float, spisok))
print (sorted (foo))
