'''
Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
forma:
1
22
333
4444
55555
666666
'''

for i in range(7):
    for j in range(i):
        print(i, end = " ")
    print(" ")