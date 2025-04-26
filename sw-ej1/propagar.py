def calcular_patrones(distancia):
    combinaciones = []

    
    def backtracking(patron_actual, suma_actual):
        if suma_actual == distancia:
            combinaciones.append(patron_actual)
            return

        if suma_actual > distancia:
            return

        backtracking(patron_actual + "A", suma_actual + 1)
        backtracking(patron_actual + "B", suma_actual + 2)

    backtracking("", 0)
    return combinaciones


    

distancia = 10
patrones = calcular_patrones(distancia)
# print(f"Patrones para distancia {distancia}: {patrones}")
print(f"Cantidad de patrones: {len(patrones)}")
    
    

    



