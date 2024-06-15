import json
from typing import Any


def extract_data(data_file: str, combinations: list[tuple[Any, Any]]) -> Any:
    with open(data_file, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    results = {}
    for combination in combinations:
        result = data['Times'][combination[0]][str(combination[1])][str(int(combination[0] + 1))][str(combination[2])][
            str(combination[3])]
        results[combination] = result
    return results
