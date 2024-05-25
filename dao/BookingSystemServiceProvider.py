from abc import ABC, abstractmethod

class BookingSystemServiceProvider(ABC):

    @abstractmethod
    def book_tickets(self, customer_id, event_id, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id):
        pass

    @abstractmethod
    def create_user(self, booking_id):
        pass