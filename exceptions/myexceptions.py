class CreatingEventException(Exception):
    def __init__(self, message="Error Creating Event"):
        self.message = message
        super().__init__(self.message)

class EventNotFoundException(Exception):
    def __init__(self, message="No Events Found"):
        self.message = message
        super().__init__(self.message)

class BookingTicketsException(Exception):
    def __init__(self, message="Error booking tickets"):
        self.message = message
        super().__init__(self.message)

class CancelBookingException(Exception):
    def __init__(self, message="Error cancelling booking"):
        self.message = message
        super().__init__(self.message)

class BookingNotFoundException(Exception):
    def __init__(self, message="No Bookings Found"):
        self.message = message
        super().__init__(self.message)

class FetchingTicketsException(Exception):
    def __init__(self, message="Error retrieving available tickets"):
        self.message = message
        super().__init__(self.message)

class UserCreationException(Exception):
    def __init__(self, message="Error Creating User"):
        self.message = message
        super().__init__(self.message)