# WeekendTicket.py

from Ticket import Ticket


class WeekendTicket(Ticket):
    """
    WeekendTicket is a specialized type of Ticket.
    It includes the valid weekend for the ticket.
    """

    def __init__(self, ticketID, ticket_type, price, seatNumber, isAvailable, validWeekend):
        """
        Constructor to initialize the WeekendTicket attributes.
        Inherits from Ticket and adds validWeekend.
        """
        # Initialize the parent class (Ticket) attributes
        super().__init__(ticketID, ticket_type, price, seatNumber, isAvailable)

        # Protected attribute for the valid weekend
        self._validWeekend = validWeekend


    # Getters and Setters


    def getValidWeekend(self):
        """
        Returns the valid weekend for the ticket.
        """
        return self._validWeekend

    def setValidWeekend(self, validWeekend):
        """
        Sets the valid weekend for the ticket.
        """
        self._validWeekend = validWeekend
