import datetime

from PYFiles.trucks import *
from PYFiles.import_csv import *

# manually loading trucks and inputting departure times
truck1 = Truck([13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40],  datetime.timedelta(hours=8, minutes=0, seconds=0), "Truck 1")
truck2 = Truck([3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39], datetime.timedelta(hours=9, minutes=5, seconds=0),  "Truck 2")
truck3 = Truck([9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],  datetime.timedelta(hours=10, minutes=20, seconds=0), "Truck 3")


# function to return the index of an address from the address table in O(1) time
def address_lookup(address):

    return address_data.index(address)


# function to return the distance between two addresses based on the distance table in O(1) time
def distance_in_between(address1, address2):

    distance_value = distance_data[address_lookup(address1)][address_lookup(address2)]
    
    if distance_value == '':
        # Handle the case where distance is empty in the distance table
        distance_value = distance_data[address_lookup(address2)][address_lookup(address1)]
    

    distance = float(distance_value)
    
    return distance

    
# function to return the minimum distance value in the distances array in O(n) time
def find_minimum_distance(truck):

    distances = []

    # loops through truck's array of packages that are not yet delivered
    for i in truck.not_delivered:

        # find the distance between the truck's current address and every other address in the array that matches the index
        dist = distance_in_between(truck.current_address, hash_table.search(i).address)

        # adds the distance in miles to the distances array
        distances.append(float(dist))

    # finds the minimum value in the array of distances
    minimum_distance = min(distances)

    # finds the index of the next closest address
    index_of_minimum = distances.index(minimum_distance)
    return index_of_minimum, minimum_distance


# algorithm used for transporting the packages ***Nearest Neighbor algorithm***
def transport(truck):

    # set packages in truck as en route in O(n) time
    for i in truck.not_delivered:
        hash_table.search(i).status = "en route"
        hash_table.search(i).departure_time = truck.depart_time
        truck.current_time = truck.depart_time

    # loops through every package that is on the truck in the not_delivered array in O(n) time
    while len(truck.not_delivered) > 0:

        # find the shortest distance from the current address of the truck to any package in the array from the min_distance function
        index_of_nearest, shortest_distance = find_minimum_distance(truck)
        truck.current_address = hash_table.search(truck.not_delivered[index_of_nearest]).address
        
        # add the miles traveled to the package to the truck's total miles
        truck.miles_traveled += shortest_distance

        # updated the current time for each package that is delivered ***divided by 18 to get it out of 24 hour time***
        truck.current_time += datetime.timedelta(hours=shortest_distance / 18)

        # marks the package as delivered
        hash_table.search(truck.not_delivered[index_of_nearest]).status = "delivered"
        hash_table.search(truck.not_delivered[index_of_nearest]).delivered_time = truck.current_time

        # moves the package to the delivered array and then removes from the not delivered array
        truck.delivered.append(truck.not_delivered[index_of_nearest])
        truck.not_delivered.remove(truck.not_delivered[index_of_nearest])

    # adds the mileage from the last package address on the truck back to the hub address
    dist_back_to_hub = distance_in_between(hash_table.search(truck.delivered[len(truck.delivered) - 1]).address, truck.end_address)
    truck.miles_traveled += dist_back_to_hub
    truck.miles_traveled = round(truck.miles_traveled, 1)
    truck.current_time += datetime.timedelta(hours=dist_back_to_hub / 18)
    print("________________________________________")
    print(f"{truck.truck_id} Left the hub at: {str(truck.depart_time)}")
    print(f"{truck.truck_id} returned to the hub at: {str(truck.current_time)}")
    print(f"{truck.truck_id} traveled {str(truck.miles_traveled)} miles in total")
    print("________________________________________\n")

