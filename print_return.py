print("Please insert a number of meters")

def print_meter_to_cm(meters):
    print(100 * int(meters))
def return_meters_to_cm(meters):
    return 100 * int(meters)
def main():
    meters = input()
    print(str(print_meter_to_cm(meters)) + ("cm"))
    return_meters_to_cm(meters)
    print(str((return_meters_to_cm(meters))) + str("cm"))
if __name__ == "__main__":
    main()