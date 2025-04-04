# Name: Jorge De La Garza
# Student ID: 011066647

from PYFiles.user_interface import *

class Main:
    print("------WGU Parcel Service Program------\n")

    # imports package objects into hash_table
    import_packages("csv files/packages.csv")

    # imports addresses into array
    import_addresses("csv files/addresses.csv")

    # imports distances to all addresses into an array
    import_distances("csv files/distances.csv")

    # calls transport function for each truck from transport.py
    transport(truck1)
    transport(truck2)
    transport(truck3)

# starts the program where the user can see the inputs
start()
