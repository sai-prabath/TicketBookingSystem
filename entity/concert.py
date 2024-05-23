from entity.event import Event

class Concert(Event):
    def __init__(self, event_id=None, event_name=None, event_date=None, event_time=None, venue_name=None, total_seats=0, available_seats=0, ticket_price=0.0, event_type=None, artist=None, concert_type=None):
        super().__init__(event_id, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
        self.__artist = artist
        self.__concert_type = concert_type

    def getArtist(self):
        return self.__artist

    def setArtist(self, artist):
        self.__artist = artist

    def getConcertType(self):
        return self.__concert_type

    def setConcertType(self, concert_type):
        self.__concert_type = concert_type

    def __str__(self):
        parent_details = super().__str__()
        child_details = f"Artist: {self.__artist}, Concert Type: {self.__concert_type}\n"
        return parent_details + child_details
