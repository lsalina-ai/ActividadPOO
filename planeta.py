from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"


class Planeta:

    def __init__(self, nombre, cantidad_satelites,
                 masa, volumen, diametro,
                 distancia_sol, tipo,
                 es_observable,
                 periodo_orbital,
                 periodo_rotacion):

        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self):

        print("\n========== DATOS DEL PLANETA ==========")
        print("Nombre:", self.nombre)
        print("Cantidad de satélites:", self.cantidad_satelites)
        print("Masa:", self.masa, "kg")
        print("Volumen:", self.volumen, "km³")
        print("Diámetro:", self.diametro, "km")
        print("Distancia al Sol:", self.distancia_sol, "km")
        print("Tipo de planeta:", self.tipo.value)
        print("Observable:", self.es_observable)
        print("Periodo orbital:", self.periodo_orbital, "años")
        print("Periodo de rotación:", self.periodo_rotacion, "días")

    def calcular_densidad(self):

        return self.masa / self.volumen

    def es_planeta_exterior(self):

        limite = 149597870 * 3.4

        if self.distancia_sol > limite:
            return True
        else:
            return False



print("======================================")
print("       REGISTRO DE PLANETAS")
print("======================================")

print("\nPLANETA 1")

nombre1 = input("Nombre del planeta: ")
satelites1 = int(input("Cantidad de satélites: "))
masa1 = float(input("Masa del planeta: "))
volumen1 = float(input("Volumen del planeta: "))
diametro1 = int(input("Diámetro del planeta: "))
distancia1 = int(input("Distancia al Sol: "))

print("\nTipos disponibles:")
print("1. GASEOSO")
print("2. TERRESTRE")
print("3. ENANO")

opcion1 = int(input("Seleccione el tipo de planeta: "))

if opcion1 == 1:
    tipo1 = TipoPlaneta.GASEOSO
elif opcion1 == 2:
    tipo1 = TipoPlaneta.TERRESTRE
else:
    tipo1 = TipoPlaneta.ENANO

observable1 = input("¿Es observable? (si/no): ").lower() == "si"

orbital1 = float(input("Periodo orbital (años): "))
rotacion1 = float(input("Periodo de rotación (días): "))


planeta1 = Planeta(
    nombre1,
    satelites1,
    masa1,
    volumen1,
    diametro1,
    distancia1,
    tipo1,
    observable1,
    orbital1,
    rotacion1
)


print("\nPLANETA 2")

nombre2 = input("Nombre del planeta: ")
satelites2 = int(input("Cantidad de satélites: "))
masa2 = float(input("Masa del planeta: "))
volumen2 = float(input("Volumen del planeta: "))
diametro2 = int(input("Diámetro del planeta: "))
distancia2 = int(input("Distancia al Sol: "))

print("\nTipos disponibles:")
print("1. GASEOSO")
print("2. TERRESTRE")
print("3. ENANO")

opcion2 = int(input("Seleccione el tipo de planeta: "))

if opcion2 == 1:
    tipo2 = TipoPlaneta.GASEOSO
elif opcion2 == 2:
    tipo2 = TipoPlaneta.TERRESTRE
else:
    tipo2 = TipoPlaneta.ENANO

observable2 = input("¿Es observable? (si/no): ").lower() == "si"

orbital2 = float(input("Periodo orbital (años): "))
rotacion2 = float(input("Periodo de rotación (días): "))


planeta2 = Planeta(
    nombre2,
    satelites2,
    masa2,
    volumen2,
    diametro2,
    distancia2,
    tipo2,
    observable2,
    orbital2,
    rotacion2
)


planeta1.imprimir()

print("Densidad:", planeta1.calcular_densidad())
print("¿Es planeta exterior?:", planeta1.es_planeta_exterior())

planeta2.imprimir()

print("Densidad:", planeta2.calcular_densidad())
print("¿Es planeta exterior?:", planeta2.es_planeta_exterior())