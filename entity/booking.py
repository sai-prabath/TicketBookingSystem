class Booking:
    def __init__(self, booking_id=None, customer_id=None, event_id=None, num_tickets=0,total_cost=0,booking_date=None,event=None):
        self.__booking_id = booking_id
        self.__event_id = event_id
        self.__customer_id = customer_id
        self.__num_tickets = num_tickets
        if total_cost == 0 or total_cost == None:
            self.__total_cost = event.getTicketPrice() * num_tickets
        else:
            self.__total_cost = total_cost
        self.__booking_date = booking_date

    def getBookingID(self):
        return self.__booking_id

    def getEvent(self):
        return self.__event_id

    def setEvent(self, event_id):
        self.__event_id = event_id

    def getCustomer(self):
        return self.__customer_id

    def setCustomer(self, customer_id):
        self.__customer_id = customer_id

    def getNumTickets(self):
        return self.__num_tickets

    def setNumTickets(self, num_tickets):
        self.__num_tickets = num_tickets

    def getTotalCost(self):
        return self.__total_cost

    def setTotalCost(self, total_cost):
        self.__total_cost = total_cost

    def getBookingDate(self):
        return self.__booking_date

    def setBookingDate(self, booking_date):
        self.__booking_date = booking_date

    def __str__(self):
        return f"Booking ID: {self.__booking_id}\nCustomer id: {self.__customer_id} Event id: {self.__event_id}\nNumber of Tickets: {self.__num_tickets}, Total Cost: {self.__total_cost}, Date: {self.__booking_date}\n"
