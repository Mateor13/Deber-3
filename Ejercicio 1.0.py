print("Ejercicio de réplica 01")
lista = [1, 3, 2, 7, 9, 8, 6]
print("Respesta:", 4 in lista, "\n") 


print("Ejercicio de réplica 02")
x=4
y=2
lista = [1, 5]
print("Respuesta 1:", x is lista) 
print("Respuesta 2:", x is 4,"\n") 



print("Ejercicio de réplica 03")
print("Hola","\n")
"Ejemplo de comentario "
"""Hola esto
es un 
comentario
de varias líneas"""

print("Ejercicio de réplica 04")
a= -1 
b= a + 2 
print(b)
suma=1.1+2.2
print (suma,"\n")


print("Ejercicio de réplica 05")
real = 1.1+2.2 
print (real) 
print(f'{real:.2f}')
un_real= 1.1 
print(un_real)
otro_real= 1/2 
print(otro_real)
not_cient = 1.23E3 
print(not_cient,"\n")


print("Ejercicio de réplica 06")
complejo = 1+2j
print (complejo.real)
print (complejo.imag,"\n")


print ("Ejercicio de réplica 07")
print(bool(0)) 
print(bool(len("")),"\n")


print("Ejercicio de réplica 08")
print(bool(0.0))
print(bool(0j))
print(bool(''))
print(bool())
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(range(0)),"\n")


print("Ejercicio de réplica 09")
caracter_a='a'
print(caracter_a)
hola = 'Hola "Fythonista"'
hola_2 = 'Hola \'Fythonista\''
hola_3 = "Hola 'Fythonista'"
print(hola)
print(hola_2)
print(hola_3,"\n")


print("Ejercicio de réplica 10")
lista = [1, 2, 3, 8, 9]
tupla = (1, 4, 8, 0, 5)
conjunto = set({1, 3, 1, 4})
diccionario = {'a': 1, 'b':3, 'z':8}
print(lista)
print(tupla)
print(conjunto)
print(diccionario,"\n")


print("Ejercicio de réplica 11")
type(3)
type(2.78)
type('Hola')
isinstance (3,float)
isinstance (3,int)
isinstance (3,bool)
isinstance (False, bool)
print("\n")


print("Ejercicio de réplica 12")
numero = 15
print(numero, type(numero))
numero_flotante=15.5
print (numero_flotante, type(numero_flotante))
numero_complejo=5+6j
print(numero_complejo, type(numero_complejo))
nombre="Ernesto"
print(nombre, type(nombre))
verdadero_falso=3==3
print(verdadero_falso, type(verdadero_falso),"\n")


print("Ejercicio de réplica 13")
edad0= '25'
conversión = int(edad0) + 10  
print(conversión)
edad1=35
print (str(edad1))
num1 = '18.66'
float(num1)
print (num1,"\n")


print("Ejercicio de réplica 14")
mensaje = input("Introduce tu nombre: ")
numeroEntero = int(input("Introduce número entero: "))
numeroFlotante = float(input("Introduce número flotante: "))
numeroComplejo = complex(input("Introduce número complejo: "))
print("Bienvenido:", mensaje)
print("En número entero introducido es:", numeroEntero)
print("En número flotante introducido es:", numeroFlotante)
print("En número complejo introducido es:", numeroComplejo,"\nMateo Torres")