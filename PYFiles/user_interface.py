from PYFiles.transport import *

# function that converts a users string time input into a datetime object. Takes O(1) time
def convert_time(user_time):
    
    (h, m, s) = user_time.split(":")
    h = int(h)
    m = int(m)
    s = int(s)
    return datetime.timedelta(hours=h, minutes=m, seconds=s)


def start():

    # prints the total distance traveled for all trucks
    total_distance = truck2.miles_traveled + truck2.miles_traveled + truck3.miles_traveled
    rounded_total_distance = round(total_distance, 1)
    print(f"Sum of all distances traveled for all the trucks: {rounded_total_distance} miles\n")

    print(f"Package numbers on {truck1.truck_id}: {truck1.delivered}\n")
    print(f"Package numbers on {truck2.truck_id}: {truck2.delivered}\n")
    print(f"Package numbers on {truck3.truck_id}: {truck3.delivered}\n")
    print("choose from the following options")

    is_running = True
    while is_running:
        print("(1) get status details of a single package at a specific time")
        print("(2) get all package status details at a specific time")
        print("(3) Exit program")

        try:
            option = int(input("Choose from the folowing above\n Prompt: "))
            if option == 3:
                try:
                    print("Quitting program")
                    is_running = False
                except:
                    print("Invalid input, please pick 1, 2, or 3")

            elif option == 1:
                try:
                    # takes the user input for a chosen time in HH:MM:SS format, else sends an error message
                    user_time_input = input("enter desired time in the following format, HH:MM:SS: ")

                    # converts the input string from user_time_input to a datetime object
                    converted_time = convert_time(user_time_input)

                    # takes the user input for package ID
                    lookup_id = int(input("enter desired package ID: "))

                    # searches the hash table for the package object
                    package = hash_table.search(lookup_id)

                    # prints details to the screen
                    print(f"Package numbers on {truck1.truck_id}: {truck1.delivered}\n")
                    print(f"Package numbers on {truck2.truck_id}: {truck2.delivered}\n")
                    print(f"Package numbers on {truck3.truck_id}: {truck3.delivered}\n")
                    print(package.lookup_details(converted_time))

                except:
                    print("Invalid input, try again")

            elif option == 2:

                try:
                    user_time_input = input("enter time with the following format, HH:MM:SS: ")
                    converted_time = convert_time(user_time_input)

                    # loops through all the packages in the hash table
                    print(f"Package numbers on {truck1.truck_id}: {truck1.delivered}\n")
                    print(f"Package numbers on {truck2.truck_id}: {truck2.delivered}\n")
                    print(f"Package numbers on {truck3.truck_id}: {truck3.delivered}\n")
                    for element in range(1, 44):
                        package = hash_table.search(element)
                        print(package.lookup_details(converted_time))

                except:
                    print("Invalid input, try again")
            else:
                print("invalid input, try again")
        except:
            print("invalid input, try again")