import os

from printerror import *


def input_file_path():
    file_path = input('\nInput the file path: ')
    return file_path


def input_region():
    region = input('Input the region: ')
    return region


def input_column_id():
    column_id = input('\nInput the id of column: ')
    return column_id


def check_file(file_path):
    if not file_path.endswith('.csv'):
        print_error(ERROR_WITH_FILE_EXTENSION)
        return False
    elif os.path.getsize(file_path) == 0:
        print_error(ERROR_WITH_FILE_SIZE)
        return False
    elif not os.path.exists(file_path):
        print_error(ERROR_WITH_FILE_EXISTS)
        return False
    return True


def check_region(data, chosen_region):
    for i in data:
        if i['region'] == chosen_region:
            return True
    print_error(ERROR_WITH_REGION)
    return False


def check_column_id(data, column_id):
    if column_id.isalpha() or '.' in column_id:
        print_error_with_entered_column_number()
        return False
    number_of_columns = len(data[0].keys())
    column_number = int(column_id)
    if column_number < 0 or column_number >= number_of_columns:
        print_error_with_range_of_id_column()
        return False
    return True


def print_statistics(max_value, min_value, mean_value, median_value, sum_of_squared_difference):
    print(f'\nMax value is: {max_value}')
    print(f'Min value is: {min_value}')
    print(f'Mean value is: {mean_value}')
    print(f'Median value is: {median_value}')
    print(f'(Additional task) Sum of squared difference is: {sum_of_squared_difference}\n')


def print_percentiles(percentile_number, percentile_value):
    print(f'{str(percentile_number).rjust(3)}% {round(percentile_value, 2)}')


def print_modified_table():
    print('\nModified table:')


def print_table_percentiles():
    print('Table of percentiles:')