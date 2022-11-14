import csv

def calculate_distance(first_loc, second_loc):
    index_one = get_index(first_loc)
    index_two = get_index(second_loc)

    input_file = csv.DictReader(open("distance_data.csv"))
    if int(index_one) < int(index_two):
        param1 = int(index_two)
        param2 = int(index_one) + 1
    else:
        param1 = int(index_one)
        param2 = int(index_two) + 1
    for index, row in enumerate(input_file):
        if index == param1:
            return row[str(param2)]

def get_index(location):
    input_file = csv.DictReader(open("distance_name_data.csv"))
    for row in input_file:
        if row["C3"] == location:
            return row["C1"]


print(calculate_distance("1488 4800 S","4001 South 700 East"))