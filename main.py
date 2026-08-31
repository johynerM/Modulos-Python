#Programa para inscripciones del curso, validaciones
from validaciones.validaciones import validar_nombre, validar_edad, validar_horas
from matematicas.calculos import calcular_costo
print("===== MATRICULA DEL CURSO ============")

nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))
horas = int(input("Cuantas horas dura el curso: "))

#Validar el nombre de la persona
if not validar_nombre(nombre):
    print("Error: el nombre NO puede estar vacio")
elif not validar_edad(edad):
    print("No puedes matricularte, ers muy joven o muy oldmoney")
elif validar_horas(horas):
    print("Horas incorretas, revisa nuevamente")
else:
    valor_hora=float(input("Introduce el valor por hora del curso: "))
    horas=int(input("Introduce la cantidad de horas del curso: "))
    costo= calcular_costo(horas,valor_hora)
    if edad > 65:
        costo = costo - (costo*0.1)
    print(f"Bienvenido {nombre}")
    print(f"Costo del curso {costo}")

#validar horas del curso



#crear una funcion para descuento si la persona es mayor a 65 años 10%

