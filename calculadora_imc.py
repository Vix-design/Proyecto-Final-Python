# Datos personales

#string: nombre
nombre = input("¿Cuál es tu nombre?").strip().title()

while nombre == "":
    print("El nombre no puede estar vacío.")
    nombre = input("¿Cuál es tu nombre?").strip().title()

# string apellido paterno
apellido_paterno = input("¿Cuál es tu apellido paterno?").strip().title()

while apellido_paterno == "":
    print("El apellido paterno no puede estar vacío")
    apellido_paterno = input("¿Cuál es tu apellido paterno?").strip().title()


# string apellido materno
apellido_materno = input("¿Cuál es tu apellido materno?").strip().title()

while apellido_materno == "":
    print("El apellido materno no puede estar vacío")
    apellido_materno = input("¿Cuál es tu apellido materno?").strip().title()

# int: edad
edad = input("¿Cuál es tu edad?")

while not edad.isdigit():
    print("La edad debe ser número.")
    edad = input("¿Cuál es tu edad?")

edad = int(edad)

# float: peso
while True:
    try:
        peso = float(input("¿Cuál es tu peso?"))
        break
    except ValueError:
        print("El peso debe ser un número")

# float: estatura
while True:
    try:
        estatura = float(input("¿Cuál es tu estatura?"))
        if estatura <= 0:
            print("La estatura debe ser mayor a cero")
        else:
            break
    except ValueError:
        print("La estatura debe ser número")

# Cálculo del IMC
imc = peso / estatura ** 2

# Resultado
print (f"Nombre: {nombre} {apellido_paterno} {apellido_materno} | Edad: {edad} | Peso: {peso} kg | Estatura: {estatura} m | IMC: {imc:.2f}")