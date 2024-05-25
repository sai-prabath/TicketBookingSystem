class Event:
    def __init__(self, event_id=None, event_name=None, event_date=None, event_time=None, venue_id=None, total_seats=0,
                 available_seats=0, ticket_price=0.0, event_type=None):
        self.__event_id = event_id
        self.__event_name = event_name
        self.__event_date = event_date
        self.__event_time = event_time
        self.__venue_id = venue_id
        self.__total_seats = total_seats
        self.__available_seats = available_seats
        self.__ticket_price = ticket_price
        self.__event_type = event_type

    # Getters and Setters
    def getEventID(self):
        return self.__event_id

    def getEventName(self):
        return self.__event_name

    def setEventName(self, event_name):
        self.__event_name = event_name

    def getEventDate(self):
        return self.__event_date

    def setEventDate(self, event_date):
        self.__event_date = event_date

    def getEventTime(self):
        return self.__event_time

    def setEventTime(self, event_time):
        self.__event_time = event_time

    def getVenueID(self):
        return self.__venue_id

    def setVenueID(self, venue_id):
        self.__venue_id = venue_id

    def getTotalSeats(self):
        return self.__total_seats

    def setTotalSeats(self, total_seats):
        self.__total_seats = total_seats

    def getAvailableSeats(self):
        return self.__available_seats

    def setAvailableSeats(self, available_seats):
        self.__available_seats = available_seats

    def getTicketPrice(self):
        return self.__ticket_price

    def setTicketPrice(self, ticket_price):
        self.__ticket_price = ticket_price

    def getEventType(self):
        return self.__event_type

    def setEventType(self, event_type):
        self.__event_type = event_type

    # Methods
    def calculate_total_revenue(self):
        return (self.__total_seats - self.__available_seats) * self.__ticket_price

    def getBookedNoOfTickets(self):
        return self.__total_seats - self.__available_seats

    def book_tickets(self, num_tickets):
        self.__available_seats -= num_tickets

    def cancel_booking(self, num_tickets):
        self.__available_seats += num_tickets


    def __str__(self):
        return f"Event ID: {self.__event_id}\nEvent Name: {self.__event_name}, Event Date: {self.__event_date}, Event Time: {self.__event_time}\nVenue Name: {self.__venue_id}, Total Seats: {self.__total_seats}, Available Seats: {self.__available_seats}\nTicket Price: {self.__ticket_price}, Event Type: {self.__event_type}\n"

