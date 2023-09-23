from printerror import *


def parse_table(data_file):
    keys = data_file.readline().strip().split(',')
    parsed_data = []
    for line in data_file:
        values = line.strip().split(',')
        parsed_dict = dict(zip(keys, values))
        parsed_data.append(parsed_dict)
    return parsed_data


def calculate_max_column_widths(data):
    column_widths = {key: len(key) for key in data[0].keys()}
    for row in data:
        for key, value in row.items():
            column_widths[key] = max(column_widths[key], len(str(value)))
    return column_widths


def format_row(row, width):
    return row.rjust(width)


def format_table(data):
    column_widths = calculate_max_column_widths(data)

    headers_line = data[0].keys()
    for key in headers_line:
        print(format_row(key, column_widths[key]), end='     ')
    print()

    for row in data:
        for key in row.keys():
            print(format_row(row[key], column_widths[key]), end='     ')
        print()


def filter_by_region(data, chosen_region):
    filtered_data = []
    for i in data:
        if i['region'] == chosen_region:
            filtered_data.append(i)
    return filtered_data


def get_values_by_column(data, chosen_column):
    column_keys = list(data[0].keys())
    column_value = column_keys[chosen_column]
    list_of_statistics = []
    for i in data:
        value = i[column_value].replace(" ", "")
        if value != "" and value.isalpha() == False:
            list_of_statistics.append(float(value))
        else:
            print_error(ERROR_VALUE)
            list_of_statistics.clear()
            break
    return list_of_statistics