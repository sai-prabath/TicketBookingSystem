from entity.event import Event

class Movie(Event):
    def __init__(self, event_id=None, event_name=None, event_date=None, event_time=None, venue_name=None, total_seats=0, available_seats=0, ticket_price=0.0, event_type=None, genre=None, actor_name=None, actress_name=None):
        super().__init__(event_id, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
        self.__genre = genre
        self.__actor_name = actor_name
        self.__actress_name = actress_name

    def getGenre(self):
        return self.__genre

    def setGenre(self, genre):
        self.__genre = genre

    def getActorName(self):
        return self.__actor_name

    def setActorName(self, actor_name):
        self.__actor_name = actor_name

    def getActressName(self):
        return self.__actress_name

    def setActressName(self, actress_name):
        self.__actress_name = actress_name

    def __str__(self):
        parent_details = super().__str__()
        child_details = f"Genre: {self.__genre}, Actor Name: {self.__actor_name}, Actress Name: {self.__actress_name}\n"
        return parent_details + child_details

