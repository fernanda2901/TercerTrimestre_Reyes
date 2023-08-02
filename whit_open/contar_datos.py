
def contar_caracteres():
    archivo = open("datos.txt", "r")
    datos_texto = archivo.read()
    archivo.close()

    numero_caracteres = len(datos_texto)
    numero_lineas = datos_texto.count("\n") +1

    return numero_caracteres, numero_lineas


caracteres, lineas = contar_caracteres()

print(f"Los numeros de caracteres  fueron: {caracteres}")
print(f"El numero de lineas fue: {lineas}")

