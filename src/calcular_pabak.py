import numpy as np
import pandas as pd
import argparse

# Establecer la opción para el comportamiento futuro
pd.set_option('future.no_silent_downcasting', True)

# Función para calcular el acuerdo observado considerando varias categorías (-1, 0, 1)
def calculate_observed_agreement_full(data):
    total_items = data.shape[0] # Número de textos anotados
    total_ratings = data.shape[1]  # Número de anotadores
    agreements = 0
    print(f"textos: {total_items} , anotadores:  {total_ratings}")

    for row in data:
        # Contar las frecuencias de cada categoría en la fila
        counts = np.bincount(row.astype(int) + 1)  # Shift de [-1,0,1] a [0,1,2]
        agreements += np.sum(counts * (counts - 1)) / 2  # Acuerdos por pares

    # Proporción de acuerdos observados
    Pa = agreements / (total_items * total_ratings * (total_ratings - 1) / 2)
    return Pa

def main(file_path):
    # Cargar el archivo Excel
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

    # Eliminar la fila 0 que contiene descripciones
    df = df.drop(index=0).reset_index(drop=True)

    # Filtrar solo las columnas que contienen '#1_' en su nombre
    filtered_columns = [col for col in df.columns if '#1_' in col]
    df_filtered = df[filtered_columns]

    # Mapeo de anotaciones a valores: "+ Virtud" = 1, "- Vicio" = -1, y NaN = 0
    mapping = {"+ Virtud": 1, "- Vicio": -1}
    df_filtered = df_filtered.replace(mapping).fillna(0)

    # Convertir el DataFrame a matriz numpy
    data_matrix = df_filtered.values

    # Transponer para que cada fila sea una tarea y cada columna un anotador
    data_matrix_transposed = np.transpose(data_matrix)

    # Calcular el acuerdo observado (Pa)
    observed_agreement_full = calculate_observed_agreement_full(data_matrix_transposed)

    # Calcular PABAK
    PABAK_full = 2 * observed_agreement_full - 1

    # Mostrar resultado
    print("PABAK:", PABAK_full)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calcular PABAK a partir de un archivo Excel.')
    parser.add_argument('file', type=str, help='Ruta al archivo Excel')
    args = parser.parse_args()
    main(args.file)

