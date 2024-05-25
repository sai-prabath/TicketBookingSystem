from dao.EventServiceProviderImpl import EventServiceProviderImpl
from dao.BookingSystemServiceProviderImpl import BookingSystemServiceProviderImpl
from entity.movie import Movie
from entity.concert import Concert
from entity.sports import Sports
from entity.venue import Venue
from entity.customer import Customer
from exceptions.myexceptions import CreatingEventException, EventNotFoundException, BookingTicketsException, CancelBookingException, BookingNotFoundException, FetchingTicketsException, UserCreationException

class MainModule:
    def __init__(self):
        self.event_service_provider = EventServiceProviderImpl()
        self.booking_service_provider = BookingSystemServiceProviderImpl()

    def create_venue(self):
        try:
            print("\n------Creating Venue------\n")
            venue_name = input("Enter venue name: ")
            address = input("Enter venue address: ")
            venue = Venue(None, venue_name, address)
            result = self.event_service_provider.CreateVenue(venue)
            if result:
                print("Venue Created Successfully")
            else:
                raise CreatingEventException("Error Creating Venue")

        except Exception as e:
            print(e)

    def create_user(self):
        try:
            print("\n------Creating User------\n")
            username = input("Enter Name: ")
            email = input("Enter email: ")
            phone = input("Enter Phone Number: ")
            customer = Customer(None, username, email, phone)
            result = self.booking_service_provider.create_user(customer)
            if result:
                print(f"User Created Successfully and Customer id = {result}")
            else:
                raise UserCreationException()
        except Exception as e:
            print(e)
    def create_event(self):
        try:
            print("\n------Creating Event------")
            event_name = input("Enter event name: ")
            event_date = input("Enter Event date (YYYY-MM-DD): ")
            event_time = input("Enter Event time (HH:MM:SS): ")
            venue_id = input("Enter venue ID: ")
            total_seats = int(input("Enter total seats: "))
            available_seats = total_seats
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (movie, concert, sports): ").lower()
            event = None

            if event_type == "movie":
                genre = input("Enter Genre name: ")
                actor_name = input("Enter Actor name: ")
                actress_name = input("Enter Actress name: ")
                event = Movie(None, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, genre, actor_name, actress_name)

            elif event_type == "concert":
                artist_name = input("Enter Artist name: ")
                concert_type = input("Enter Concert type: ")
                event = Concert(None, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, artist_name, concert_type)

            elif event_type == "sports":
                sport_name = input("Enter Sport name: ")
                teams_name = input("Enter teams name: ")
                event = Sports(None, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, sport_name, teams_name)
            else:
                print("Event type error")

            result = self.event_service_provider.create_event(event)

            if result:
                print(f"Event successfully created with event id {result}")
            else:
                raise CreatingEventException()

        except Exception as e:
            print(e)

    def display_events(self):
        try:
            events = self.event_service_provider.getEventDetails()
            if events:
                print("\n------Events------\n")
                for category in events:
                    for event in category:
                        print(event)
                print("-------------------\n")
            else:
                raise EventNotFoundException()
        except Exception as e:
            print(e)

    def get_available_tickets(self):
        try:
            available_tickets = self.event_service_provider.getAvailableNoOfTickets()
            if available_tickets:
                for i in available_tickets:
                    print(f"Available Tickets in {i[0]} = {i[1]}")
            else:
                raise FetchingTicketsException()
        except Exception as e:
            print(e)

    def book_tickets(self):
        try:
            self.display_events()
            event_id = input("Enter event id to book tickets: ")
            customer_id = input("Enter your customer id: ")
            num_tickets = int(input("Enter number of tickets to book: "))

            result = self.booking_service_provider.book_tickets(customer_id, event_id, num_tickets)

            if result:
                print(f"Tickets booked successfully with booking ID: {result}")
            else:
                raise BookingTicketsException()

        except Exception as e:
            print(e)

    def cancel_booking(self):
        try:
            booking_id = int(input("Enter booking ID to cancel: "))
            if self.booking_service_provider.cancel_booking(booking_id):
                print("Booking cancelled successfully.")
            else:
                raise CancelBookingException()
        except Exception as e:
            print(e)

    def get_booking_details(self):
        try:
            booking_id = int(input("Enter booking ID to retrieve details: "))
            booking = self.booking_service_provider.get_booking_details(booking_id)
            if booking:
                print("\n------Booking Details------\n")
                print(booking)
                print("----------------------------")
            else:
                raise BookingNotFoundException()

        except Exception as e:
            print(e)

    def main_menu(self):
        while True:
            print("\n-------- Main Menu --------\n")
            print("1. Create Venue")
            print("2. Create Event")
            print("3. Display Events")
            print("4. Get Available Tickets")
            print("5. Create User")
            print("6. Book Tickets")
            print("7. Cancel Booking")
            print("8. Get Booking Details")
            print("9. Exit")
            print("---------------------------\n")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_venue()
            elif choice == '2':
                self.create_event()
            elif choice == '3':
                self.display_events()
            elif choice == '4':
                self.get_available_tickets()
            elif choice == '5':
                self.create_user()
            elif choice == '6':
                self.book_tickets()
            elif choice == '7':
                self.cancel_booking()
            elif choice == '8':
                self.get_booking_details()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.main_menu()
