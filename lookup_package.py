import datetime
from time import strptime

from load_trucks import truck_one, truck_two, truck_three, all_packages


def lookup_package(package_number, package_datetime: datetime.datetime):
    if package_number in truck_one.get_keys():
        ref_time = datetime.datetime(2022, 11, 11, 8, 0, 0)
        if package_datetime < ref_time:
            print(f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was at the hub")
            return
        elif package_datetime < all_packages.get_item(package_number)[-2]:
            print(f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was en route to {all_packages.get_item(package_number)[0]}")
        else:
            print(f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} had already been"
                  f" delivered to {all_packages.get_item(package_number)[0]} at {all_packages.get_item(package_number)[-2]}")

    elif package_number in truck_two.get_keys() or package_number in truck_three.get_keys():
        ref_time = datetime.datetime(2022, 11, 11, 8, 30, 0)
        if package_number == '9':
            if package_datetime < ref_time:
                print(f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was at the hub")
                return
            elif package_datetime < datetime.datetime(2022, 11, 11, 10, 20, 0):
                print(
                    f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was awaiting its updated destination")
            elif package_datetime > datetime.datetime(2022, 11, 11, 10, 20, 0) and package_datetime < all_packages.get_item(package_number)[-2]:
                print(
                    f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was en route to {all_packages.get_item(package_number)[0]}")
            else:
                print(
                    f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} had already been"
                    f" delivered to {all_packages.get_item(package_number)[0]} at {all_packages.get_item(package_number)[-2]}")
        elif package_datetime < ref_time:
            print(f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was at the hub")
            return
        elif package_datetime < all_packages.get_item(package_number)[-2]:
            print(
                f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} was en route to {all_packages.get_item(package_number)[0]}")
        else:
            print(f"At {package_datetime.hour}:{package_datetime.minute}, Package #{package_number} had already been"
                  f" delivered to {all_packages.get_item(package_number)[0]} at {all_packages.get_item(package_number)[-2]}")
