from pandas import read_csv


def calculate_distance(first_loc, second_loc):
    data = read_csv("data/distance_name_data.csv")
    index_one = int(data[data.values == first_loc]["C1"].values)
    index_two = int(data[data.values == second_loc]["C1"].values)

    data = read_csv("data/distance_data.csv")
    if index_one > index_two:
        return data.iloc[index_one, index_two]
    elif index_two > index_one:
        return data.iloc[index_two, index_one]