"""
Este módulo contiene una función para filtrar y ordenar las vistas de artículos donde el autor es también el espectador.
"""

import pandas as pd


def article_views_df(views: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra las vistas de artículos donde el autor es también el espectador y las ordena por 'id' en orden ascendente.

    Args:
        views (pd.DataFrame): DataFrame que contiene las vistas de artículos con columnas 'author_id' y 'viewer_id'.

    Returns:
        pd.DataFrame: DataFrame filtrado y ordenado con una sola columna 'id'.
    """
    df_author_is_viewer = views[views["author_id"] == views["viewer_id"]]
    df_author_is_viewer = df_author_is_viewer.rename(columns={"author_id": "id"})
    return df_author_is_viewer[["id"]].sort_values("id", ascending=True)


def article_views_array(views: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra las vistas de artículos donde el autor es también el espectador y devuelve los IDs únicos en orden ascendente.

    Args:
        views (pd.DataFrame): DataFrame que contiene las vistas de artículos con columnas 'author_id' y 'viewer_id'.

    Returns:
        pd.DataFrame: DataFrame con una sola columna 'id' que contiene los IDs únicos en orden ascendente.
    """
    authors_viewed_own_articles = views[views["author_id"] == views["viewer_id"]]
    unique_authors = authors_viewed_own_articles["author_id"].unique()
    unique_authors = sorted(unique_authors)
    result_df = pd.DataFrame({"id": unique_authors})
    return result_df


if __name__ == "__main__":
    data = {"author_id": [1, 2, 3, 4, 5], "viewer_id": [1, 5, 8, 9, 10]}
    views = pd.DataFrame(data)

    result_df = article_views_df(views)
    result_array = article_views_array(views)

    expected_data_df = {"id": [1]}
    expected_df = pd.DataFrame(expected_data_df)

    expected_data_array = {"id": [1]}
    expected_array = pd.DataFrame(expected_data_array)

    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)
    pd.testing.assert_frame_equal(result_array.reset_index(drop=True), expected_array)
