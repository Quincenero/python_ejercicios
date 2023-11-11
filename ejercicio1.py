'''
Leer tres números que denoten una fecha (día, mes, año) y comprobar que sea una fecha
válida. Si la fecha no es válida escribir un mensaje de error por pantalla. Si la fecha es
válida se debe imprimir la fecha cambiando el número que representa el mes por su
nombre. Por ejemplo: si se introduce 1 2 2006, se deberá imprimir “1 de febrero de 2006”.
'''
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
if mes == 1 and 0 < dia <= 31:
    print("La fecha es: ", dia, " Enero", "del ", anio)
elif mes == 2 and 0 < dia <= 28:
    print("La fecha es: ", dia, " Febrero", "del ", anio)
elif mes == 3 and 0 < dia <= 31:
    print("La fecha es: ", dia, " Marzo", "del ", anio)
elif mes == 4 and 0 < dia <=30:
    print("La fecha es: ", dia, " Abril", "del ", anio)
elif mes == 5 and 0 < dia <= 31:
    print("La fecha es: ", dia, " Mayo", "del ", anio)
elif mes == 6 and 0 < dia <= 30:
    print("La fecha es: ", dia, " Junio", "del ", anio)    
elif mes == 7 and 0 < dia<= 31:
    print("La fecha es: ", dia, " Julio", "del ", anio)
elif mes == 8 and 0 < dia <= 31:
    print("La fecha es: ", dia, " Agosto", "del ", anio)  
elif mes == 9 and 0 < dia <= 30:
    print("La fecha es: ", dia, " Septiembre", "del ", anio) 
elif mes == 10 and 0 < dia <= 31:
    print("La fecha es: ", dia, " Octubre", "del ", anio)
elif mes == 11 and 0 < dia <= 30:
    print("La fecha es: ", dia, " Noviembre", "del ", anio)
elif mes == 12 and 0 < dia <= 31:
    print("La fecha es: ", dia, " Diciembre", "del ", anio)

else:
    print("La fecha ingresada es invalida")
    
'''prueba concluida'''