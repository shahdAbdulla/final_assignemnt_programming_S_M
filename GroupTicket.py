# GroupTicket.py
# This class represents a group ticket for events.
# It extends the Ticket class to include the number of people in the group.

from Ticket import Ticket

class GroupTicket(Ticket):
    """
    GroupTicket is a specialized type of Ticket.
    It includes a group size for the ticket reservation.
    """

    def __init__(self, ticketID, ticket_type, price, seatNumber, isAvailable, groupSize):
        """
        Constructor to initialize the GroupTicket attributes.
        Inherits from Ticket and adds groupSize.
        """
        # Call the constructor of the parent class (Ticket) to initialize its attributes
        super().__init__(ticketID, ticket_type, price, seatNumber, isAvailable)

        # Initialize the specific attribute for GroupTicket
        self._groupSize = groupSize  # Number of people included in the group ticket


    # Getters and Setters

    def getGroupSize(self):
        """
        Returns the group size of the ticket.
        """
        return self._groupSize

    def setGroupSize(self, groupSize):
        """
        Sets the group size of the ticket.
        """
        self._groupSize = groupSize
