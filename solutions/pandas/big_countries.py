import pandas as pd

data = {
    "country": ["USA", "Canada", "Mexico", "Brazil", "Argentina"],
    "population": [331002651, 37742154, 128932753, 212559417, 45195777],
    "area": [9833520, 9984670, 1964375, 8515767, 2780400],
}

df = pd.DataFrame(data)
df.set_index("country", inplace=True)

# Usando loc para filtrar y seleccionar columnas
filtered_df = df.loc[df["population"] > 100000000, ["population", "area"]]

# Usando iloc para seleccionar filas y columnas por índice
selected_df = df.iloc[:3, [0, 2]]

# Usando loc con condición AND
filtered_df_and = df.loc[
    (df["population"] > 100000000) & (df["area"] > 5000000), ["population", "area"]
]

# Usando loc con condición OR
filtered_df_or = df.loc[
    (df["population"] > 100000000) | (df["area"] > 5000000), ["population", "area"]
]
