#option 1
list = ['Roma','Pasha','Sveta','Oleg','Alesia']
print (list[2::2])


#option 2
list = ('Roma','Pasha','Sveta','Oleg','Alesia',)
print (list [2], list [-1])

#option 3 is the most labor-consuming :))
list = ['Roma','Pasha','Sveta','Oleg','Alesia']
list.remove('Roma')
list.remove('Pasha')
list.remove('Oleg')
print (list)

#

number_list = [x for x in range(10) if x % 2 != 0] 
print(number_list)

number_list = [1,3,99,52,66]
a = [num for num in number_list if num %2 !=0]
print (a)

