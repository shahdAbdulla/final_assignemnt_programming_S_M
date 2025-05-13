
# Ticket.py
# This class represents a Ticket object with its details,
# including ticket type, price, seat number, availability,
# and methods to manage ticket information and calculate discounts.


class Ticket:


   def __init__(self, ticketID, ticket_type, price, seatNumber, isAvailable):
       """
       Constructor to initialize the Ticket attributes.
       """
       # Initialize ticket attributes
       self._ticketID = ticketID           # Unique ID for the ticket
       self._type = ticket_type            # Type of the ticket (e.g., VIP, Standard)
       self._price = price                 # Price of the ticket
       self._seatNumber = seatNumber       # Seat number assigned to the ticket
       self._isAvailable = isAvailable     # Availability status (True if available, False otherwise)




   # Getters and Setters


   def getTicketID(self):
       """
       Returns the Ticket's ID.
       """
       return self._ticketID


   def setTicketID(self, ticketID):
       """
       Sets the Ticket's ID.
       """
       self._ticketID = ticketID


   def getType(self):
       """
       Returns the Ticket's Type.
       """
       return self._type


   def setType(self, ticket_type):
       """
       Sets the Ticket's Type.
       """
       self._type = ticket_type


   def getPrice(self):
       """
       Returns the Ticket's Price.
       """
       return self._price


   def setPrice(self, price):
       """
       Sets the Ticket's Price if it is non-negative.
       """
       try:
           # Validate that the price is not negative
           if price >= 0:
               self._price = price
           else:
               # Raise an error if the price is negative
               raise ValueError("Price cannot be negative.")
       except ValueError as ve:
           # Display an error message if the value is invalid
           print(f"Error: {ve}")


   def getSeatNumber(self):
       """
       Returns the Ticket's Seat Number.
       """
       return self._seatNumber


   def setSeatNumber(self, seatNumber):
       """
       Sets the Ticket's Seat Number.
       """
       self._seatNumber = seatNumber


   def getIsAvailable(self):
       """
       Returns the Ticket's availability status.
       """
       return self._isAvailable


   def setIsAvailable(self, isAvailable):
       """
       Sets the availability status of the Ticket.
       """
       self._isAvailable = isAvailable




   # Methods


   def calculateDiscount(self):
       """
       Calculates the discount based on the type of ticket.
       - VIP tickets receive a 10% discount.
       - Standard tickets receive a 5% discount.
       - Other types receive no discount.


       Returns:
           float: The discounted price.
       """
       try:
           # Apply a 10% discount if the ticket type is "VIP"
           if self._type.lower() == "vip":
               return self._price * 0.9
           # Apply a 5% discount if the ticket type is "Standard"
           elif self._type.lower() == "standard":
               return self._price * 0.95
           # No discount for other types
           else:
               return self._price
       except Exception as e:
           # Display an error message if the calculation fails
           print(f"Discount Calculation Error: {e}")
           return self._price