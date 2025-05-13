# Booking.py
# This class represents a booking made by a customer for a specific ticket.
# It includes the booking details, status, and associated payment information.

class Booking:
    """
    Booking class represents a booking made by a customer for a specific ticket.
    It includes the booking details, status, and associated payment information.
    """

    def __init__(self, bookingID, customer, ticket, bookingDate, status):
        """
        Constructor to initialize Booking attributes.
        """
        self.__bookingID = bookingID             # Unique ID for the booking
        self.__customer = customer               # Customer object associated with the booking
        self.__ticket = ticket                   # Ticket object linked to the booking
        self.__bookingDate = bookingDate         # Date the booking was made
        self.__status = status                   # Status of the booking (e.g., Pending, Confirmed, Cancelled)
        self.__payment = None                    # Payment information, initially set to None


    # Getters and Setters

    def getBookingID(self):
        """
        Returns the Booking ID.
        """
        return self.__bookingID

    def setBookingID(self, id):
        """
        Sets the Booking ID.
        """
        self.__bookingID = id

    def getCustomer(self):
        """
        Returns the Customer associated with the booking.
        """
        return self.__customer

    def setCustomer(self, customer):
        """
        Sets the Customer for the booking.
        """
        self.__customer = customer

    def getTicket(self):
        """
        Returns the Ticket associated with the booking.
        """
        return self.__ticket

    def setTicket(self, ticket):
        """
        Sets the Ticket for the booking.
        """
        self.__ticket = ticket

    def getBookingDate(self):
        """
        Returns the booking date.
        """
        return self.__bookingDate

    def setBookingDate(self, date):
        """
        Sets the booking date.
        """
        self.__bookingDate = date

    def getStatus(self):
        """
        Returns the status of the booking.
        """
        return self.__status

    def setStatus(self, status):
        """
        Sets the status of the booking.
        """
        self.__status = status

    def getPayment(self):
        """
        Returns the Payment associated with the booking.
        """
        return self.__payment

    def setPayment(self, payment):
        """
        Sets the Payment for the booking.
        """
        self.__payment = payment


    # Methods

    def confirmBooking(self):
        """
        Confirms the booking if it is currently marked as 'Pending'.
        Changes status to 'Confirmed' and displays a message.
        If it's already confirmed, it displays a message indicating that.
        """
        try:
            # Check if the booking is still pending
            if self.__status.lower() == "pending":
                # Change the status to confirmed
                self.__status = "Confirmed"
                print("Booking confirmed successfully.")
                return True
            else:
                # Display a message if the booking is already confirmed
                print("Booking is already confirmed.")
                return False
        except AttributeError as e:
            # If there is an error accessing the status, it displays an error message
            print("Error confirming booking:", e)
            return False

    def cancelBooking(self):
        """
        Cancels the booking if it is currently marked as 'Confirmed'.
        Changes status to 'Cancelled' and displays a message.
        If it's not confirmed, it displays a message indicating that cancellation is not possible.
        """
        try:
            # Check if the booking is confirmed
            if self.__status.lower() == "confirmed":
                # Change the status to cancelled
                self.__status = "Cancelled"
                print("Booking cancelled successfully.")
                return True
            else:
                # Display a message if the booking is not confirmed yet
                print("Cannot cancel a booking that is not confirmed.")
                return False
        except AttributeError as e:
            # If there is an error accessing the status, it displays an error message
            print("Error cancelling booking:", e)
            return False
