# SinglePassTicket.py
# This class represents a single-use ticket for a specific event.
# It extends the Ticket class to include a valid date for the ticket.

from Ticket import Ticket


class SinglePassTicket(Ticket):
    """
    SinglePassTicket is a specialized type of Ticket.
    It includes a valid date for when the ticket can be used.
    """

    def __init__(self, ticketID, ticket_type, price, seatNumber, isAvailable, validDate):
        """
        Constructor to initialize the SinglePassTicket attributes.
        Inherits from Ticket and adds validDate.
        """
        # Call the constructor of the parent class (Ticket) to initialize its attributes
        super().__init__(ticketID, ticket_type, price, seatNumber, isAvailable)

        # Initialize the specific attribute for SinglePassTicket
        self._validDate = validDate  # Date when the ticket is valid for use


    # Getters and Setters

    def getValidDate(self):
        """
        Returns the valid date of the ticket.
        """
        return self._validDate

    def setValidDate(self, validDate):
        """
        Sets the valid date of the ticket.
        """
        self._validDate = validDate

