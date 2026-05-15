
class Persona:

    
    def __init__(self, nombre, apellidos,
                 numero_documento,
                 anio_nacimiento,
                 pais_nacimiento,
                 genero):

        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    
    def imprimir(self):

        print("\n----- DATOS DE LA PERSONA -----")
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Número de documento:", self.numero_documento)
        print("Año de nacimiento:", self.anio_nacimiento)
        print("País de nacimiento:", self.pais_nacimiento)
        print("Género:", self.genero)



print("================================")
print("     REGISTRO DE PERSONAS")
print("================================")


print("\nPERSONA 1")

nombre1 = input("Ingrese el nombre: ")
apellidos1 = input("Ingrese los apellidos: ")
documento1 = input("Ingrese el número de documento: ")
anio1 = int(input("Ingrese el año de nacimiento: "))
pais1 = input("Ingrese el país de nacimiento: ")
genero1 = input("Ingrese el género (H/M): ")


print("\nPERSONA 2")

nombre2 = input("Ingrese el nombre: ")
apellidos2 = input("Ingrese los apellidos: ")
documento2 = input("Ingrese el número de documento: ")
anio2 = int(input("Ingrese el año de nacimiento: "))
pais2 = input("Ingrese el país de nacimiento: ")
genero2 = input("Ingrese el género (H/M): ")

persona1 = Persona(
    nombre1,
    apellidos1,
    documento1,
    anio1,
    pais1,
    genero1
)

persona2 = Persona(
    nombre2,
    apellidos2,
    documento2,
    anio2,
    pais2,
    genero2
)

persona1.imprimir()
persona2.imprimir()