import math
from inputandoutput import *


def show_statistics(list_of_values):
    max_value = calculate_max_value(list_of_values)
    min_value = calculate_min_value(list_of_values)
    mean_value = calculate_mean_value(list_of_values)
    median_value = calculate_median_value(list_of_values)
    sum_of_squared_differences = calculate_sum_of_squared_differences(list_of_values)
    print_statistics(max_value, min_value, mean_value, median_value, sum_of_squared_differences)


def calculate_sum_of_squared_differences(lst):
    sum_of_squared_differences = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            difference = lst[i] - lst[j]
            squared_difference = difference ** 2
            sum_of_squared_differences += squared_difference
    return round(sum_of_squared_differences, 2)


def calculate_max_value(list_of_values):
    return max(list_of_values)


def calculate_min_value(list_of_values):
    return min(list_of_values)


def calculate_mean_value(list_of_values):
    return round(sum(list_of_values) / len(list_of_values), 2)


def calculate_median_value(list_of_values):
    new_list_of_values = sorted(list_of_values)
    middle_index = len(new_list_of_values) // 2

    if len(new_list_of_values) % 2 != 0:
        median_value = round(new_list_of_values[middle_index], 2)
    else:
        median_value = round((new_list_of_values[middle_index - 1] + new_list_of_values[middle_index]) / 2, 2)

    return median_value


def calculate_percentile(values, percentile):
    values_count = len(values)
    rank = percentile / 100 * (values_count - 1)
    rank_floor = math.floor(rank)
    rank_fraction = rank - rank_floor

    if rank_floor == values_count - 1:
        result = values[-1]
    else:
        result = values[rank_floor] + (values[rank_floor + 1] - values[rank_floor]) * rank_fraction
    return result


def show_percentile(sorted_stats):
    print_table_percentiles()
    current_percentile = 0
    max_percentile = 100
    percentile_step = 5
    while current_percentile <= max_percentile:
        percentile_value = calculate_percentile(sorted_stats, current_percentile)
        print_percentiles(current_percentile, percentile_value)
        current_percentile += percentile_step