# Event.py
from Ticket import Ticket


class Event:
    """
    The Event class represents an event with its details,
    including location, date, capacity, type, and a list of tickets.
    This class now demonstrates composition by creating Ticket objects internally.
    """

    def __init__(self, name, location, date, totalCapacity, eventType):
        """
        Constructor to initialize the Event attributes and create tickets.
        """
        # Event attributes
        self.__name = name  # Event name
        self.__location = location  # Location of the event
        self.__date = date  # Date of the event
        self.__totalCapacity = totalCapacity  # Maximum capacity of the event
        self.__eventType = eventType  # Type of the event (e.g., Music, Sports)

        # Composition: Tickets are created inside Event
        # If the event is deleted, the tickets are also deleted.
        self.__ticketList = [
            Ticket(f"{name[:3]}-{i}", eventType, 100.0, f"Seat-{i}", True)
            for i in range(1, totalCapacity + 1)
        ]

        # List to store users who booked tickets
        self.__userList = []

    # --- Getter methods ---
    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def getDate(self):
        return self.__date

    def getTotalCapacity(self):
        return self.__totalCapacity

    def getEventType(self):
        return self.__eventType

    def getTicketList(self):
        return self.__ticketList

    def getUserList(self):
        return self.__userList

    # --- Setter methods ---
    def setName(self, name):
        self.__name = name

    def setLocation(self, location):
        self.__location = location

    def setDate(self, date):
        self.__date = date

    def setTotalCapacity(self, capacity):
        self.__totalCapacity = capacity

    def setEventType(self, eventType):
        self.__eventType = eventType

    def setTicketList(self, tickets):
        self.__ticketList = tickets

    def setUserList(self, users):
        self.__userList = users

    # --- Management methods ---
    def addTicket(self, ticket):
        """
        Adds a ticket to the ticket list.
        """
        if isinstance(ticket, Ticket):
            self.__ticketList.append(ticket)

    def removeTicket(self, ticket):
        """
        Removes a ticket from the ticket list if it exists.
        """
        if ticket in self.__ticketList:
            self.__ticketList.remove(ticket)

    def addUser(self, user):
        """
        Adds a user to the event's user list.
        """
        self.__userList.append(user)

    def removeUser(self, user):
        """
        Removes a user from the event's user list if they exist.
        """
        if user in self.__userList:
            self.__userList.remove(user)

    def getAvailableTickets(self):
        """
        Retrieves a list of available tickets (those marked as available).
        """
        return [ticket for ticket in self.__ticketList if ticket.getIsAvailable()]

    def displayTickets(self):
        """
        Displays all tickets for the event.
        """
        print(f"\nTickets for Event: {self.__name}")
        for ticket in self.__ticketList:
            status = "Available" if ticket.getIsAvailable() else "Sold"
            print(f"{ticket.getTicketID()} | {ticket.getType()} | {ticket.getSeatNumber()} | {status}")
