import datetime
# class to create package objects
class Package:
    def __init__(self, pid, address, city, state, zip_code, deadline, weight, notes):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.departure_time = None
        self.delivered_time = None
        self.status = "at hub"

    # B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:
    # delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status (i.e., "at the hub", "en route", or "delivered"), including delivery time
    # O(1)
    def lookup_details(self, user_time_input):

        if user_time_input >= self.delivered_time:
            time = self.delivered_time
            status = f"Status: delivered - Delivered Time: {str(time)}"
        elif self.delivered_time > user_time_input > self.departure_time:
            status = "Status: en route"
        else:
            status = "Status: at hub"

        # Handle Wrong Address case
        if self.pid == 9 and user_time_input >= datetime.timedelta(seconds=37200):
            self.address = "410 S State St"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.zip_code = "84111"

        return (f"Package ID: {self.pid}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code} Deadline: {self.deadline}, Weight(kg): {self.weight}, Status: {status}, Notes: {self.notes}")
