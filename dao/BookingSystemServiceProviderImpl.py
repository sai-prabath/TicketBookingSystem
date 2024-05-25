from dao.BookingSystemServiceProvider import BookingSystemServiceProvider
from dao.EventServiceProviderImpl import EventServiceProviderImpl
import mysql.connector
from entity.event import Event
from entity.booking import Booking

class BookingSystemServiceProviderImpl(EventServiceProviderImpl, BookingSystemServiceProvider):
    def __init__(self):
        super().__init__()

    def create_user(self, customer):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO customer (customer_name, email, phone_number) VALUES (%s, %s, %s)"
            values = (customer.getCustomerName(), customer.getEmail(), customer.getPhoneNumber())
            cursor.execute(query, values)
            self.conn.commit()

            cursor.execute("SELECT MAX(customer_id) from customer")
            customer_id = cursor.fetchone()[0]
            self.conn.commit()
            cursor.close()
            return customer_id
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def book_tickets(self, customer_id, event_id, num_tickets):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Event WHERE event_id = %s"
            cursor.execute(query, (event_id,))
            event_data = cursor.fetchone()

            if event_data:
                event = Event(*event_data)
                if num_tickets <= event.getAvailableSeats():
                    event.book_tickets(num_tickets)
                    update_query = "UPDATE Event SET available_seats = %s WHERE event_id = %s"
                    cursor.execute(update_query, (event.getAvailableSeats(), event.getEventID()))
                    self.conn.commit()

                    booking = Booking(None, customer_id, event_id, num_tickets,0,None,event)
                    booking_query = "INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost, booking_date) VALUES (%s, %s, %s, %s, now())"
                    cursor.execute(booking_query, (customer_id, event_id, num_tickets,booking.getTotalCost()))
                    self.conn.commit()

                    cursor.execute("SELECT MAX(booking_id) FROM booking")
                    booking_id = cursor.fetchone()[0]
                    self.conn.commit()
                    cursor.close()
                    return booking_id
                else:
                    print("Not enough available seats.")
                    return False
            else:
                print("Event not found.")
                return False

        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def cancel_booking(self, booking_id):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Booking WHERE booking_id=%s"
            cursor.execute(query, (booking_id,))
            booking_data = cursor.fetchone()
            booking = Booking(*booking_data)

            event_query = "SELECT * FROM Event WHERE event_id=%s"
            cursor.execute(event_query, (booking.getEvent(),))
            event_data = cursor.fetchone()
            event = Event(*event_data)

            event.cancel_booking(booking.getNumTickets())

            update_query = "UPDATE Event SET available_seats=%s WHERE event_id=%s"
            cursor.execute(update_query, (event.getAvailableSeats(), event.getEventID()))
            self.conn.commit()

            delete_booking_query = "DELETE FROM Booking WHERE booking_id=%s"
            cursor.execute(delete_booking_query, (booking_id,))
            self.conn.commit()

            cursor.close()
            return True

        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def get_booking_details(self, booking_id):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Booking WHERE booking_id=%s"
            cursor.execute(query, (booking_id,))
            booking_data = cursor.fetchone()
            cursor.close()

            booking = Booking(*booking_data)
            return booking

        except mysql.connector.Error as err:
            print("Error:", err)
            return False
