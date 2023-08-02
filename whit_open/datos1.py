
def datos_personales():

    nombre= input("Ingrese su nombre y apellido:")
    edad= input("Ingrse su edad:")
    telefono= int(input("Ingreses su numero de celular:"))

    archivo= open("datos.txt", "w")
    archivo.write(F"Su nombre, apellido y edad son: {nombre}, {edad}\nSu numero de telefono es: {telefono}.")
    archivo.close()

    print("Datos guardados")

datos_personales()