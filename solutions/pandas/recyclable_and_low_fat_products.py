import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Encuentra los productos que son bajos en grasa y reciclables.

    Parameters:
    products (pd.DataFrame): DataFrame que contiene los datos de los productos.

    Returns:
    pd.DataFrame: DataFrame con los IDs de los productos que son bajos en grasa y reciclables.
    """
    return products[
        (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    ].loc[:, ["product_id"]]


# Caso de ejemplo
data = {
    "product_id": [1, 2, 3, 4, 5],
    "low_fats": ["Y", "N", "Y", "Y", "N"],
    "recyclable": ["Y", "Y", "N", "Y", "Y"],
}

df_products = pd.DataFrame(data)

# Llamar a la función con el caso de ejemplo
result = find_products(df_products)
print(result)
