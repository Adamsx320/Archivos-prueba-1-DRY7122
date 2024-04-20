
seccion_valida = "DRY7122-003V"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
codigo_sección = input("Ingrese su código de sección: ")
sede = input("Ingrese su sede: ")

if codigo_seccion == seccion_valida:
    print("Información: ")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Código-sección:", codigo_seccion)
    print("Sede:", sede)

else:
    print("Usted no pertenece a esta sección.")
