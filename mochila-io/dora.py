import random
import math

class Recluta: 
    def __init__(self, nombre, salario, habilidades, sector):
        self.nombre = nombre
        self.habilidades = habilidades
        self.sector = sector
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Habilidades: {self.habilidades}, Salario: {self.salario}"

    def habilidad_por_perfil(self, perfil):
        return self.habilidades[perfil]

class Equipo:
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.reclutas = []    

    def agregar_recluta(self, recluta, fraccion):
        self.reclutas.append(recluta, fraccion)

    def calcular_habilidades(self, perfil):
        return sum(recluta.habilidad_por_perfil(perfil) * fraccion for recluta, fraccion in self.reclutas)

    def calcular_coste(self):
        return sum(recluta.salario * fraccion for recluta, fraccion in self.reclutas)
    

class SA:
    def __init__(self, perfil, reclutas, presupuesto):
        self.reclutas = reclutas
        self.perfil = perfil
        self.presupuesto = presupuesto
        self.temperatura_inicial = 200
        self.temperatura_final = 5
        self.alfa = 0.9

    def funcion_objetivo(self, equipo):
        coste = equipo.calcular_coste()
        if coste > self.presupuesto:
            equipo.reclutas = [recluta for recluta, fraccion in equipo.reclutas if recluta.salario * fraccion <= self.presupuesto]
            equipo.presupuesto = self.presupuesto

        return equipo.calcular_habilidades(self.perfil)
    
    def generar_vecino(self, equipo):
        nuevo_equipo = Equipo(self.presupuesto)

        for recluta, fraccion in equipo.reclutas:
            random_fraccion = fraccion * random.uniform(0, 1)
            nuevo_equipo.agregar_recluta(recluta, random_fraccion)
        return nuevo_equipo

    def probabilidad_aceptacion(self, delta, temperatura):
        return math.exp(delta / temperatura) > random.uniform(0, 1)
    
    def ejecutar(self):
        solActual = Equipo(self, self.presupuesto)
        temperatura = self.temperatura_inicial

        for recluta in self.reclutas:
            solActual.agregar_recluta(recluta, random.uniform(0, 1))

        costeActual = solActual.calcular_coste()
        solMejor = Equipo(self, self.presupuesto)
        mejorCoste = solMejor.calcular_coste()
        mejorValor = solMejor.funcion_objetivo(solMejor)

        exito = -1
        while self.temperatura_inicial > self.temperatura_final and exito != 0:
            exito = 0
            equipoVecino = self.generar_vecino(solActual)
            costeVecino = equipoVecino.calcular_coste()
            valorVecino = equipoVecino.funcion_objetivo(equipoVecino)
            valorActual = solActual.funcion_objetivo(solActual)
            delta = valorVecino - valorActual

            if delta > 0 or self.probabilidad_aceptacion(delta, temperatura) > random.uniform(0, 1):
                exito += 1
                solActual = equipoVecino
                valorActual = valorVecino
                if(valorActual > mejorValor):
                    mejorValor = valorActual
                    solMejor = solActual

            temperatura *= self.alfa

        return solMejor
                
class Archivo: 
    def __init__(self, ruta):
        self.ruta = ruta

    def leer_datos(self):
        datos = []

        with open(self.ruta) as file:
            lineas = file.readlines()

            i = 0
            while i < len(lineas):
                if lineas[i].strip() == "":
                    i += 1
                    continue

                n = int(lineas[i].strip())
                i += 1

                reclutas = []
                

