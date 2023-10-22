# /Users/daria/Documents/Бауманка предметы/2 курс/3 семестр/ЯПП/Python/laba_1/tests/russian_demography.csv
# /Users/daria/Documents/Бауманка предметы/2 курс/3 семестр/ЯПП/Python/laba_1/tests/russian_demography_broken.csv
# /Users/daria/Documents/Бауманка предметы/2 курс/3 семестр/ЯПП/Python/laba_1/tests/russian_demography_one_column.csv
# /Users/daria/Documents/Бауманка предметы/2 курс/3 семестр/ЯПП/Python/laba_1/tests/demography_empty.csv

from calculatestatistics import *
from workwithtable import *


if __name__ == '__main__':
    file_name = input_file_path()
    if check_file(file_name):
        with open(file_name, 'r') as file:
            data_from_file = parse_table(file)
        region_name = input_region()
        if check_region(data_from_file, region_name):
            new_data_from_file = filter_by_region(data_from_file, region_name)
            print_modified_table()
            format_table(new_data_from_file)
            column_number = input_column_id()
            if check_column_id(new_data_from_file, column_number):
                column_number = int(column_number)
                list_of_statistics = get_values_by_column(new_data_from_file, column_number)
                if list_of_statistics:
                    show_statistics(list_of_statistics)
                    show_percentile(sorted(list_of_statistics))
                else:
                    print_error(ERROR_WITH_CALCULATE_STATISTICS)



