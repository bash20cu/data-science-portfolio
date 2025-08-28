import pandas as pd

#Crear un DataFrame desde un diccionario
data = {
    "Nombre": ["Ana", "Luis", "María", "Pedro"],
    "Edad": [23, 30, 21, 35],
    "Carrera": ["Ingeniería", "Medicina", "Economía", "Derecho"],
    "Nota": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Primeras filas
print(df.head())

# Info general
print(df.info())

# Estadísticas básicas
print(df.describe())