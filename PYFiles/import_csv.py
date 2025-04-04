import csv
from PYFiles.packages import *
from PYFiles.hash_table import *

hash_table = HashTable()
distance_data = []
address_data = []


# parses the packages from the packages CSV file
def import_packages(filename):

    with open(filename, "r", encoding="utf-8-sig") as packages_csv_file:
        packages_reader = csv.reader(packages_csv_file, delimiter=",")

        # loops through each row in the CSV file in O(n) time
        for row in packages_reader:

            # storing values into variables to pass into insert function and package object
            pid = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = int(row[6])
            notes = row[7]

            # inserts the package ID as the key and the package object with the variables above as the value making a key, value pair for the hash table
            hash_table.insert(pid, Package(pid, address, city, state, zip_code, deadline, weight, notes))


# parses the distance csv file
def import_distances(filename):
    
    with open(filename, "r", encoding="utf-8-sig") as distances_csv_file:
        distances_reader = csv.reader(distances_csv_file, delimiter=",")

        # stores each row from the distances csv file into the distance_data list in O(n) time
        for row in distances_reader:
            distance_data.append(row)   


# parses the address csv file
def import_addresses(filename):

    with open(filename, "r", encoding="utf-8-sig") as addresses_csv_file:
        addresses_reader = csv.reader(addresses_csv_file, delimiter=",")

        # loops through each row in the csv file in O(n) time
        for row in addresses_reader:

            # appends only the addresses in the 3rd column from the addresses csv to the list
            address_data.append(row[2])
