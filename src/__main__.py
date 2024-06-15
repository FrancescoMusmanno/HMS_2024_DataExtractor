import os
import datetime

from data_extractor import extract_data
from io_manager import generate_combinations, write_to_csv


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(base_dir, 'config\\config.json')
    data_file = os.path.join(base_dir, 'data\\data.json')

    timestamp = datetime.datetime.now().strftime('%d-%m-%Y-%H.%M.%S')
    output_file = os.path.join(base_dir, f'output\\{timestamp}.csv')

    combinations = generate_combinations(config_file)
    results = extract_data(data_file, combinations)
    write_to_csv(results, output_file)


if __name__ == "__main__":
    main()
