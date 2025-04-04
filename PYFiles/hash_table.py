#A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:
#delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status (i.e., at the hub, en route, or delivered), including the delivery time

#Hash Table was created from zybooks
#This hash table is based on the zybooks material for Hash tables...
#C 949: Data Structures and Algorithms I home > 15.10: Python: Hash tables
#Figure 15.10.2: ChainingHashTableItem and ChainingHashTable classes.
class HashTable:

    #Initialize the hash table with a capacity that covers what's needed in terms of the amount of packages.
    def __init__(self, init_cap=45):

        self.table = []
        for i in range(init_cap):
            self.table.append([])

    #Inserts key value pairs into the hash table
    def insert(self, key, item):

        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        for keyValue in bucket_list:

            if keyValue[0] == key:
                keyValue[1] = item
                return True

        new_key = [key, item]
        bucket_list.append(new_key)
        return True
    
    #Deletes values by Key from the hash table
    def delete(self, key):

        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        if key in bucket_list:
            bucket_list.remove(key)

    #Searches values by Key from the hash table
    def search(self, key):

        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        for keyValue in bucket_list:
            if keyValue[0] == key:
                return keyValue[1]
        return None