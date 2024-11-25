"""
Simplicidad y eficiencia para contar ocurrencias -> value_counts().
Flexibilidad o múltiples agregaciones -> groupby().
"""

import pandas as pd


def get_classes_with_min_students(df: pd.DataFrame, min_students: int) -> pd.Index:
    """
    Obtiene los nombres de las clases que tienen al menos una cantidad mínima de estudiantes.

    Parameters:
    df (pd.DataFrame): DataFrame que contiene los datos de las clases.
    min_students (int): Número mínimo de estudiantes para filtrar las clases.

    Returns:
    pd.Index: Índice con los nombres de las clases que tienen al menos min_students estudiantes.
    """
    value_counts = df["class_name"].value_counts()
    return value_counts[value_counts >= min_students].index


def find_classes_with_min_students_value_counts(
    df: pd.DataFrame, min_students: int = 5
) -> pd.DataFrame:
    """
    Encuentra las clases que tienen al menos una cantidad mínima de estudiantes
    utilizando el método value_counts().

    Parameters:
    df (pd.DataFrame): DataFrame que contiene los datos de las clases.
    min_students (int): Número mínimo de estudiantes para filtrar las clases.

    Returns:
    pd.DataFrame: DataFrame con las clases que tienen al menos min_students estudiantes.
    """
    filtered_classes = get_classes_with_min_students(df, min_students)
    return pd.DataFrame(filtered_classes, columns=["class_name"])


def find_classes_with_min_students_group_by(
    df: pd.DataFrame, min_students: int = 5
) -> pd.DataFrame:
    """
    Encuentra las clases que tienen al menos una cantidad mínima de estudiantes
    utilizando el método groupby() y count().

    Parameters:
    df (pd.DataFrame): DataFrame que contiene los datos de las clases.
    min_students (int): Número mínimo de estudiantes para filtrar las clases.

    Returns:
    pd.DataFrame: DataFrame con las clases que tienen al menos min_students estudiantes.
    """
    class_counts = df.groupby("class_name")["student_id"].count().reset_index()
    classes_with_min_students = class_counts[
        class_counts["student_id"] >= min_students
    ][["class_name"]]
    return classes_with_min_students


# Ejemplo de uso
data = {
    "class_name": ["Math", "Science", "Math", "History", "Math", "Science", "Art"],
    "student_id": [30, 25, 30, 20, 30, 25, 15],
}

df_courses = pd.DataFrame(data)

# Obtener resultados de ambas funciones
classes_value_counts = find_classes_with_min_students_value_counts(
    df_courses, min_students=2
)
classes_group_by = find_classes_with_min_students_group_by(df_courses, min_students=2)

# Verificar que los resultados son iguales
assert classes_value_counts.equals(classes_group_by), "Los resultados no son iguales"
print("Ambas funciones entregan el mismo resultado")

