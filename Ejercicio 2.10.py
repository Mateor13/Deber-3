nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota de ingles: "))
if nota>=9 and nota<=10:
    print("Felicitaciones", nombre, "su nota es",nota, "equivalente a excelente", "\nMateo Torres")
elif nota>7 and nota<=8:
     print("Siga adelante", nombre,"su nota es", nota,"equivalente a muy buena", "\nMateo Torres")
elif nota>5 and nota<=6:
    print("Debe esforzarse más", nombre,"su nota es", nota,"equivalente a buena", "\nMateo Torres")
elif nota>0 and nota<=4:
    print("Usted", nombre,"puede reprobar ya que su nota es", nota,"equivalente a regula", "\nMateo Torres")
else:
    print("Valor invalido", "\nMateo Torres")