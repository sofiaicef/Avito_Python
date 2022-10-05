import csv

def read(needed_file:str)->list:
    with open(needed_file,'r', newline='') as file:
        data=csv.reader(file,delimiter=';')
        data1=list(data)
        return data1

read('Corp_summary.csv')

def choose(needed_file:str):
    print('Что пожелаете:\ n')
    print('Иерархию',1,'\n')
    print('Отчет департаментов', 2, '\n')
    print('Отчет департаментов в scv ', 3, '\n')
    res=input()
    if res=='1':
        hierarchy(data)
    elif res=='2':
        report(data)
    elif res=='3':
        reportcsv(data)

 def hierarchy(data:list):
     departaments=[]
     for row in data:
        departaments.append(row['Департамент'])
    departaments = set(departaments)
    depart_otdel = {x: [] for x in departaments}
    return

def report(data:list):
    return 

def reportcsv(data:list):
    return        
