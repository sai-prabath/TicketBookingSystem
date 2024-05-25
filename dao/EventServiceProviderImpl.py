from dao.EventServiceProvider import EventServiceProvider
from util.dbutil import DBUtil
from entity.event import Event
from entity.movie import Movie
from entity.concert import Concert
from entity.sports import Sports
import mysql.connector

class EventServiceProviderImpl(EventServiceProvider):
    def __init__(self):
        self.conn = DBUtil.getDBConn()



    def create_event(self, event):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO Event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (event.getEventName(), event.getEventDate(), event.getEventTime(), event.getVenueID(), event.getTotalSeats(), event.getAvailableSeats(), event.getTicketPrice(), event.getEventType())
            cursor.execute(query, values)
            self.conn.commit()
            cursor.execute("SELECT MAX(event_id) FROM event")
            event_id = cursor.fetchone()[0]
            self.conn.commit()

            if event.getEventType() == "movie":
                movie = event
                movie_query = "INSERT INTO Movie (event_id, genre, actor_name, actress_name) VALUES (%s, %s, %s, %s)"
                cursor.execute(movie_query, (event_id, movie.getGenre(), movie.getActorName(), movie.getActressName()))
            elif event.getEventType() == "concert":
                concert = event
                concert_query = "INSERT INTO Concert (event_id, artist, concert_type) VALUES (%s, %s, %s)"
                cursor.execute(concert_query, (event_id, concert.getArtist(), concert.setConcertType()))
            elif event.getEventType() == "sports":
                sports = event
                sports_query = "INSERT INTO Sports (event_id, sport_name, teams_name) VALUES (%s, %s, %s)"
                cursor.execute(sports_query, (event_id, sports.getSportName(), sports.getTeamsName()))

            self.conn.commit()
            cursor.close()

            return event_id

        except mysql.connector.Error as e:
            print("DataBase Error:", e)
            return False

    def getEventDetails(self):
        try:
            cursor = self.conn.cursor()

            movie_query = "SELECT e.*, m.genre, m.actor_name, m.actress_name FROM Event e JOIN Movie m ON e.event_id = m.event_id"
            cursor.execute(movie_query)
            movie_data = cursor.fetchall()

            sports_query = "SELECT e.*, s.sport_name, s.teams_name FROM Event e JOIN Sports s ON e.event_id = s.event_id"
            cursor.execute(sports_query)
            sports_data = cursor.fetchall()

            concert_query = "SELECT e.*, c.artist, c.concert_type FROM Event e JOIN Concert c ON e.event_id = c.event_id"
            cursor.execute(concert_query)
            concert_data = cursor.fetchall()

            self.conn.commit()
            cursor.close()

            movies = [Movie(*data) for data in movie_data]
            sports = [Sports(*data) for data in sports_data]
            concerts = [Concert(*data) for data in concert_data]

            return [movies, sports, concerts]

        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def getAvailableNoOfTickets(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT event_type, SUM(available_seats) FROM Event GROUP BY event_type"
            cursor.execute(query)
            available_seats = cursor.fetchall()
            cursor.close()
            return available_seats
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def CreateVenue(self, venue):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO Venue (venue_name, address) VALUES (%s, %s)"
            values = (venue.getVenueName(), venue.getAddress())
            cursor.execute(query, values)
            self.conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False