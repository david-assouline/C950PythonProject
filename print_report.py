from load_trucks import all_packages


def generate_report(truck_one_total_distance, truck_two_total_distance, truck_three_total_distance, truck_time):
    print("*" * 40)
    print(f"Report Generated at: {truck_time}")
    for i in all_packages.get_keys():
        temp = all_packages.get_item(i)
        print(f"package: {i} has destination: {temp[0]} and status: {temp[-1]}")
    print("*" * 40)
    print(f"truck one total distance traveled: {round(truck_one_total_distance, 2)} miles")
    print(f"truck two total distance traveled: {round(truck_two_total_distance, 2)} miles")
    print(f"truck three total distance traveled: {round(truck_three_total_distance, 2)} miles")
    print("*" * 40)
