import pandas as pd

def analizar_datos(archivo_densidad, archivo_sexo, ciudades_filtro):
    """
    Analiza los datos de densidad de población y personas por sexo para descubrir un mensaje secreto.

    Args:
        archivo_densidad (str): Ruta al archivo con la densidad de población.
        archivo_sexo (str): Ruta al archivo con el número de personas por sexo.
        ciudades_filtro (list): Lista de nombres de ciudades a filtrar.

    Returns:
        str: Mensaje secreto formado por las primeras letras de las ciudades filtradas.
    """
    # Leer los archivos
    df_densidad = pd.read_excel(archivo_densidad, header=1)
    df_sexo = pd.read_excel(archivo_sexo, header=4)

    # Imprimir las columnas para depuración
    print("Columnas del archivo de densidad:", df_densidad.columns.tolist())
    print("Columnas del archivo de sexo:", df_sexo.columns.tolist())

    # Renombrar columnas para que coincidan con los nombres esperados
    df_densidad.rename(columns={
        "Territorio": "nombre",
        "Extensión superficial": "superficie"
    }, inplace=True)

    df_sexo.rename(columns={
        "Territorio": "nombre",
        "Hombres": "hombres",
        "Mujeres": "mujeres",
        "Ambos sexos": "poblacion"
    }, inplace=True)

    # Verificar que las columnas necesarias existan
    columnas_densidad = {"nombre", "superficie"}
    columnas_sexo = {"nombre", "hombres", "mujeres", "poblacion"}
    if not columnas_densidad.issubset(df_densidad.columns):
        raise ValueError(f"El archivo de densidad debe contener las columnas: {', '.join(columnas_densidad)}.")
    if not columnas_sexo.issubset(df_sexo.columns):
        raise ValueError(f"El archivo de personas por sexo debe contener las columnas: {', '.join(columnas_sexo)}.")

    # Calcular la densidad poblacional
    df_densidad = pd.merge(df_densidad, df_sexo[["nombre", "poblacion"]], on="nombre")
    df_densidad["densidad"] = df_densidad["poblacion"] / df_densidad["superficie"]

    # Ordenar las ciudades por densidad poblacional de mayor a menor
    df_ordenado = df_densidad.sort_values(by="densidad", ascending=False)

    # Filtrar las ciudades específicas
    ciudades_filtradas = df_ordenado[df_ordenado["nombre"].isin(ciudades_filtro)]["nombre"]

    # Extraer la primera letra de cada ciudad filtrada
    mensaje_secreto = "".join([ciudad[0] for ciudad in ciudades_filtradas])

    return mensaje_secreto


# Rutas a los archivos
archivo_densidad = "C:\\Users\\eguij\\OneDrive\\Escritorio\\Projects\\Python\\OGATHON\\SudokuOgathon\\ia-ej2\\ciudades\\ieca_export_area.xlsx"
archivo_sexo = "C:\\Users\\eguij\\OneDrive\\Escritorio\\Projects\\Python\\OGATHON\\SudokuOgathon\\ia-ej2\\ciudades\\ieca_export_poblacion.xlsx"

# Lista de ciudades a filtrar
ciudades_filtro = [
    "Ayamonte",
    "Villanueva del Ariscal",
    "Gualchos",
    "Isla Cristina",
    "Trebujena",
    "Linares",
    "El Cuervo de Sevilla",
    "Ojén",
    "Niebla",
    "Alfacar",
    "Valderrubio",
    "Olula del Río",
    "Humilladero"
]

# Analizar los datos y descubrir el mensaje secreto
mensaje_secreto = analizar_datos(archivo_densidad, archivo_sexo, ciudades_filtro)

# Guardar el mensaje secreto en un archivo de salida
with open("mensaje_secreto.txt", "w") as archivo_salida:
    archivo_salida.write(mensaje_secreto)

print(f"Mensaje secreto: {mensaje_secreto}")