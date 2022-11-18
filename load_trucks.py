import csv

from hash_map import HashTable

truck_one = HashTable(12)
truck_one_destinations = []
truck_two = HashTable(8)
truck_two_destinations = []
truck_three = HashTable(20)
truck_three_destinations = []
all_packages = HashTable(40)


def load_trucks():
    truck_one.set_item("1", "195 W Oakland Ave")
    truck_one.set_item("13", "2010 W 500 S")
    truck_one.set_item("14", "4300 S 1300 E")
    truck_one.set_item("15", "4580 S 2300 E")
    truck_one.set_item("16", "4580 S 2300 E")
    truck_one.set_item("34", "4580 S 2300 E")
    truck_one.set_item("20", "3595 Main St")
    truck_one.set_item("29", "1330 2100 S")
    truck_one.set_item("30", "300 State St")
    truck_one.set_item("31", "3365 S 900 W")
    truck_one.set_item("37", "410 S State St")
    truck_one.set_item("40", "380 W 2880 S")

    for i in truck_one.get_keys():
        truck_one_destinations.append(truck_one.get_item(i))

    truck_two.set_item("3", "233 Canyon Rd")
    truck_two.set_item("6", "3060 Lester St")
    truck_two.set_item("18", "1488 4800 S")
    truck_two.set_item("25", "5383 South 900 East #104")
    truck_two.set_item("28", "2835 Main St")
    truck_two.set_item("32", "3365 S 900 W")
    truck_two.set_item("36", "2300 Parkway Blvd")
    truck_two.set_item("38", "410 S State St")

    for i in truck_two.get_keys():
        truck_two_destinations.append(truck_two.get_item(i))

    truck_three.set_item("2", "2530 S 500 E")
    truck_three.set_item("4", "380 W 2880 S")
    truck_three.set_item("5", "410 S State St")
    truck_three.set_item("7", "1330 2100 S")
    truck_three.set_item("8", "300 State St")
    truck_three.set_item("9", "300 State St")
    truck_three.set_item("10", "600 E 900 South")
    truck_three.set_item("11", "2600 Taylorsville Blvd")
    truck_three.set_item("12", "3575 W Valley Central Station bus Loop")
    truck_three.set_item("17", "3148 S 1100 W")
    truck_three.set_item("19", "177 W Price Ave")
    truck_three.set_item("21", "3595 Main St")
    truck_three.set_item("22", "6351 South 900 East")
    truck_three.set_item("23", "5100 South 2700 West")
    truck_three.set_item("24", "5025 State St")
    truck_three.set_item("26", "5383 South 900 East #104")
    truck_three.set_item("27", "1060 Dalton Ave S")
    truck_three.set_item("33", "2530 S 500 E")
    truck_three.set_item("35", "1060 Dalton Ave S")
    truck_three.set_item("39", "2010 W 500 S")

    for i in truck_three.get_keys():
        truck_three_destinations.append(truck_three.get_item(i))

    input_file = csv.DictReader(open("input_data.csv"))
    for row in input_file:
        all_packages.set_item(row["1"], [row["2"], row["3"], row["4"], row["5"], row["6"], row["7"], row["8"], -1, "At The Hub"])

