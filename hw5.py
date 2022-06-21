from typing import Union, Any,List


#1 task 

def my_func():
    pass



def multiplikation(x: complex) -> complex:
    total = x * 2
    return total

print (multiplikation(20))

 
def characteristic (y: complex) -> None:
    if y % 2 == 0:
        print ('yes') 
    else:
        print ('no')    

characteristic (77)


def func (d : int =6,c: int =9) -> None:
    if d > 10:
        print ('yes')
    else:
        print ('no')
func (11,6)



g: int = lambda s,v: s%v
print (g (2,6))



def decorator(func): 
    def wrapper():
        print(";)))")
        func ()
        print(":))")
    return wrapper

def say():
    print("Ура!")

say = decorator(say)
say ()


num: List [int] = [625,225,81]

def square_root (x: int) -> int:
    return x **(1/2)

num : List = list (map(square_root, num))

print (num)

num: List [int] = [625,225,81]
def check (x: int) -> int:
    return x ** (1/2) >20
num: List = list (filter (check, num))
print (num)
 
 
 

def pure_function (e: int,t: int) -> int:
    sum = e+t
    return sum
   
print (pure_function(5,6))    

 

 

result: int = min (2,-23,100,5)
print ('The minimum number is ', result)
result:int = max (2,-23,100,5)
print ('The maximum number is ', result)

 
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



def season (a:int) -> int:
   
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


from datetime import date
 
def data (y:Any, m:Any, d:Any) -> bool:
    try:
        date(y, m, d)
        return True
    except:
        return False
 
print(data (2020,12,12))
print(data (2020,12,32))


spisok: List = [16,-17,2,78.7,False,False,{'True': True},555,12,23,42,'DD']
foo: List = list(filter(lambda num: type(num) is int or type (num) is float, spisok))
print (sorted (foo))

#  2 task

def something (x:int,n:int,a:str) -> Any:
    v: Any = f"{x}, {n}, {a}"
    return v
  
print (something (2,3,'Hello'))

# 3 task

def some (x: str) -> int:
    s = x*2 
    return s


print (some (50))


#4

def mydecor(func):
    def wrap(n,i):
        return func(n,i)**2

    return wrap
 
@mydecor
def value (x,i):
    return x+i

print(value(3,9))

#6
def generator_function():
    for i in range(5):
        yield i
gen = generator_function()
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))

