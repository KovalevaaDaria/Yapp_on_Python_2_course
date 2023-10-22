ERROR_WITH_FILE_EXTENSION = 1
ERROR_WITH_FILE_SIZE = 2
ERROR_WITH_FILE_EXISTS = 3
ERROR_VALUE = 4
ERROR_WITH_ENTERED_COLUMN_NUMBER = 5
ERROR_WITH_RANGE_OF_ID_COLUMN = 6
ERROR_WITH_REGION = 7
ERROR_WITH_CALCULATE_STATISTICS = 8


def print_error_with_file_extension():
    print('\nThe file has a different extension (not ".csv")!')


def print_error_size():
    print('\nThere is no data in file it is empty!')


def print_error_exists():
    print('\nThe file does not exist!')


def print_error_value():
    print('\nThe value should be a number, not a letter/word!')


def print_error_with_entered_column_number():
    print('\nThe column number is entered incorrectly!')


def print_error_with_range_of_id_column():
    print(f'\nIncorrect range of the entered value!')


def print_error_region():
    print('\nThere is no such region in table!')


def print_error_with_calculate_statistics():
    print('It is impossible to calculate statistics!')


def print_error(error):
    if error == ERROR_WITH_FILE_EXTENSION:
        print_error_with_file_extension()
    elif error == ERROR_WITH_FILE_SIZE:
        print_error_size()
    elif error == ERROR_WITH_FILE_EXISTS:
        print_error_exists()
    elif error == ERROR_VALUE:
        print_error_value()
    elif error == ERROR_WITH_ENTERED_COLUMN_NUMBER:
        print_error_with_entered_column_number()
    elif error == ERROR_WITH_RANGE_OF_ID_COLUMN:
        print_error_with_range_of_id_column()
    elif error == ERROR_WITH_REGION:
        print_error_region()
    elif error == ERROR_WITH_CALCULATE_STATISTICS:
        print_error_with_calculate_statistics()