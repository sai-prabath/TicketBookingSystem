from abc import ABC, abstractmethod

class EventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event):
        pass

    @abstractmethod
    def getEventDetails(self):
        pass

    @abstractmethod
    def getAvailableNoOfTickets(self):
        pass

    @abstractmethod
    def CreateVenue(self, venue):
        pass
