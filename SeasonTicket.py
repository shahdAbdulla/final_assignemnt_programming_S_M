# SeasonTicket.py
# This class represents a Season Ticket for events.
# It extends the Ticket class to include the duration of the season.

from Ticket import Ticket


class SeasonTicket(Ticket):
    """
    SeasonTicket is a specialized type of Ticket.
    It includes the duration of the season for the ticket.
    """

    def __init__(self, ticketID, ticket_type, price, seatNumber, isAvailable, seasonDuration):
        """
        Constructor to initialize the SeasonTicket attributes.
        Inherits from Ticket and adds seasonDuration.
        """
        # Call the constructor of the parent class (Ticket) to initialize its attributes
        super().__init__(ticketID, ticket_type, price, seatNumber, isAvailable)

        # Initialize the specific attribute for SeasonTicket
        self._seasonDuration = seasonDuration  # Duration for how long the ticket is valid (e.g., 3 months, 1 year)

    # Getters and Setters

    def getSeasonDuration(self):
        """
        Returns the duration of the season for the ticket.
        """
        return self._seasonDuration

    def setSeasonDuration(self, seasonDuration):
        """
        Sets the duration of the season for the ticket.
        """
        self._seasonDuration = seasonDuration
