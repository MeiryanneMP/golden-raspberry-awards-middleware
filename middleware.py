import pandas as pd
import json
import os


def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    df = pd.read_csv(file_path, delimiter=";")
    print("Colunas encontradas:", df.columns.tolist())
    return df


def process_csv_data(df):
    data = []

    column_mapping = {
        'col1': [''],
        'col2': [''],
        'col3': ['']
    }

    def map_column(column):
        for col in column_mapping[column]:
            if col in df.columns:
                return col
        return None

    col_1 = map_column('')
    col_2 = map_column('')
    col_3 = map_column('')

    map_value_col1 = {
        '': ['']
    }

    def map_value_col1(value):
        for val in map_value_col1[value]:
            if val in df.values:
                return val
        return None

    col1_value = map_value_col1('')


def main():
    file_path = ''

    try:
        df = read_csv(file_path)
        data = process_csv_data(df)
        print(json.dumps(data, indent=2))

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    except FileNotFoundError as e:
        print(str(e))


if __name__ == "__main__":
    main()
