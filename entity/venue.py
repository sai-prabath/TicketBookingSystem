class Venue:
    def __init__(self, venue_id=None, venue_name=None, address=None):
        self.__venue_id = venue_id
        self.__venue_name = venue_name
        self.__address = address

    # Getters and Setters
    def getVenueID(self):
        return self.__venue_id

    def getVenueName(self):
        return self.__venue_name

    def setVenueName(self, venue_name):
        self.__venue_name = venue_name

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def __str__(self):
        return f"Venue ID: {self.__venue_id}\nVenue Name: {self.__venue_name}, Address: {self.__address}\n"

