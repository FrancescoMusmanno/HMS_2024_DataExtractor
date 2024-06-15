import json
import pandas as pd
from typing import Any


def generate_combinations(config_file: str) -> list[tuple[Any, Any]]:
    with open(config_file, 'r') as f:
        data = json.load(f)

    input_pallets = data['input_pallets']
    pickup_pallets = data['pickup_pallets']

    if len(input_pallets) != len(pickup_pallets):
        raise ValueError("The number of arrays in input_pallet and pickup_pallet should be the same.")

    combinations = []
    for input_pallet in input_pallets:
        if input_pallet[0] > 15 or input_pallet[1] > 60:
            raise ValueError("Invalid input pallets dimensions. The maximum dimensions are 15x60.")
        for pickup_pallet in pickup_pallets:
            if pickup_pallet[0] > 15 or pickup_pallet[1] > 60:
                raise ValueError("Invalid pickup pallets dimensions. The maximum dimensions are 15x60.")
            combinations.append((*input_pallet, *pickup_pallet))
    return combinations


def write_to_csv(results: dict, output_file: str):
    rows = []
    columns = []
    values = []

    for key, value in results.items():
        row_key = f'{key[0]}-{key[1]}'
        col_key = f'{key[2]}-{key[3]}'
        rows.append(row_key)
        columns.append(col_key)
        values.append(value)
    df = pd.DataFrame({'Row': rows, 'Column': columns, 'Value': values})
    pivot_df = df.pivot(index='Row', columns='Column', values='Value')
    pivot_df.to_csv(output_file)
