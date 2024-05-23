from entity.event import Event

class Sports(Event):
    def __init__(self, event_id=None, event_name=None, event_date=None, event_time=None, venue_name=None, total_seats=0, available_seats=0, ticket_price=0.0, event_type=None, sport_name=None, teams_name=None):
        super().__init__(event_id, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
        self.__sport_name = sport_name
        self.__teams_name = teams_name

    def getSportName(self):
        return self.__sport_name

    def setSportName(self, sport_name):
        self.__sport_name = sport_name

    def getTeamsName(self):
        return self.__teams_name

    def setTeamsName(self, teams_name):
        self.__teams_name = teams_name

    def __str__(self):
        parent_details = super().__str__()
        child_details = f"Sport Name: {self.__sport_name}, Teams Name: {self.__teams_name}\n"
        return parent_details + child_details
