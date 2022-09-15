#выведите все элементы а , в которых есть b
a=[0,1,2,3,4,5]
b=[3,4,5,8]
c=[]
for element in a : 
    if element in b: 
        c.append(element)
print(c)        

print([el for el in a if el in b])

print('Hell0')

#создайте новый массив с уникальными значениями a = [0, 2, 1, 0, 1, 2]
a=[0,2,1,0,1,2]
print(list(set(a)))

b = []
for item in a:
    if item not in b:
        b.append(item)
print(b)    

# создайте новый массив с четными элементами
# исходный массив
a = [0, 1, 2, 3, 4, 5]
b=[]
for el in a: 
    if el % 2 ==0 :
        b.append(el)
print(b)    

print([el for el in a if not el % 2])

print([el for el in a if el % 2==0])

# comprehension 

a = [0, 1, 2, 3, 4, 5]
b = [k for k in a]
b = [f'number: {k}' for k in a]
print(b)

# создайте словарь из списка, где ключ - индекс этого элемента
# исходный массив
a = ['foo', 'bar', 'baz']
b=[]
for ind, val in enumerate(a):
    b.update({ind: val})
print(b)

print({i:j for (i,j) in enumerate(a)})

# распечатайте приветствия
a = [
   'John', 'Allison', 'Brian',
    'Claire', 'Andrew'
]
for element in a:
    print(f'Hi, {element}')
    print('Hi, %s' %(element))
    print('Hi, {a}'.format(a=element))

#'%s%s' % (параметр1, параметр2)
#'{}'.format(параметр1,параметр2)
#f'{выражение}'








#Странно:
#dict((f, s) for f, s in enumerate(a))
#Это работает
#dict(enumerate(a))
#Это не работает
# результат

 напечатайте все элементы из a, которые отсутствуют в b
a = ['foo', 'bar', 'baz', 'egg']
b = ['bar', 'baz']
c=[]
d=[]
for i in a: 
    if i not in b:
        c.append(i)
    else:
        d.append(i)
print(f'отсутствуют:{k}' for k in c)   

c=[el for el in a if el not in b ]
f=’,‘.join(c)
print('отсутствуют {a}'.format(a-f))
print(f'отсутствуют: {", ".join(с)}')

#set - уникальность

# склейте 2 массива. результат - отсортированный массив
a = [0, 1, 2, 6, 7, 8]
b = [3, 4, 5]
с=[el for ]

# создайте новый словарь из a с отсортированными ключами в обратном порядке
a = {0: 'foo', 1: 'bar', 2: 'baz'}
y=reversed(a)

# добыть данные из внешнего API (https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0) и вывести скорость и направление ветра по всем точкам

'направление: NW, скорость: 2'
'направление: NW, скорость: 3'
'направление: W,  скорость: 5'

pip install requests 

import requests
response = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&u
nit=metric&output=json&tzshift=0')
print(response.text)
json.dumps(json_formatted_text), indent=4


pip install <название пакета>
pip install -r requirements.txt
python -m pip install <название пакета>













