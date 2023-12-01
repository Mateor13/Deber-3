import re

cadena = input("Ingrese una cadena: ")
patron = r"[A-Z]"

if re.search(patron, cadena):
    print("La cadena es una letra mayúscula.", "\nMateo Torres")
else:
    print("La cadena no es una letra mayúscula.", "\nMateo Torres")