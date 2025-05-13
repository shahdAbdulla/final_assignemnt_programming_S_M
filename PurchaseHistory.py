# PurchaseHistory.py
# This class is responsible for managing the purchase history of a customer,
# including their bookings, the total amount spent, and the last purchase date.

from Booking import Booking

class PurchaseHistory:
    """
    PurchaseHistory class keeps track of all bookings made by a customer,
    along with the total amount spent and the last purchase date.
    """

    def __init__(self, customerID):
        """
        Constructor to initialize PurchaseHistory attributes.
        """
        self.__customerID = customerID                # Stores the unique ID of the customer
        self.__bookings = []                          # List to store all booking objects
        self.__totalSpent = 0.0                       # Tracks the total amount the customer has spent
        self.__lastPurchaseDate = None                # Stores the date of the last booking


    # Getters and Setters

    def getCustomerID(self):
        """
        Returns the Customer ID.
        """
        return self.__customerID

    def setCustomerID(self, id):
        """
        Sets the Customer ID.
        """
        self.__customerID = id

    def getBookings(self):
        """
        Returns the list of bookings.
        """
        return self.__bookings

    def setBookings(self, bookings):
        """
        Sets the list of bookings if it's a list of Booking objects.
        """
        # Ensure the list is valid and contains only Booking objects
        if isinstance(bookings, list) and all(isinstance(b, Booking) for b in bookings):
            self.__bookings = bookings
        else:
            print("Invalid bookings list. Must be a list of Booking objects.")

    def getTotalSpent(self):
        """
        Returns the total amount spent.
        """
        return self.__totalSpent

    def setTotalSpent(self, amount):
        """
        Sets the total amount spent if the amount is not negative.
        """
        try:
            if amount >= 0:
                self.__totalSpent = amount
            else:
                # Raise an error if the amount is negative
                raise ValueError("Amount cannot be negative.")
        except ValueError as e:
            # Display the error message
            print("Error setting total spent:", e)

    def getLastPurchaseDate(self):
        """
        Returns the last purchase date.
        """
        return self.__lastPurchaseDate

    def setLastPurchaseDate(self, date):
        """
        Sets the last purchase date.
        """
        self.__lastPurchaseDate = date


    # Methods

    def addBooking(self, booking):
        """
        Adds a booking to the list of bookings.
        """
        try:
            # Check if the provided object is of type Booking
            if isinstance(booking, Booking):
                self.__bookings.append(booking)
                print(f"Booking {booking.getBookingID()} added successfully.")
            else:
                # Raise an error if the object is not a Booking
                raise TypeError("Invalid booking type.")
        except TypeError as e:
            # Display the error message
            print("Error adding booking:", e)

    def removeBooking(self, bookingID):
        """
        Removes a booking from the list using its ID.
        """
        try:
            # Loop through the list to find the booking by ID
            for booking in self.__bookings:
                if booking.getBookingID() == bookingID:
                    # Remove the booking if the ID matches
                    self.__bookings.remove(booking)
                    print(f"Booking {bookingID} removed successfully.")
                    return True
            # Display a message if the booking was not found
            print("Booking not found.")
            return False
        except Exception as e:
            # Display the error if one occurs
            print("Error removing booking:", e)
            return False

    def calculateTotalSpent(self):
        """
        Calculates the total amount spent by summing up the prices of all tickets in bookings.
        """
        try:
            # Sum the price of each ticket in the list of bookings
            self.__totalSpent = sum(booking.getTicket().getPrice() for booking in self.__bookings)
            print(f"Total spent calculated: {self.__totalSpent}")
        except Exception as e:
            # Display the error if something goes wrong
            print("Error calculating total spent:", e)

    def updateLastPurchaseDate(self, date):
        """
        Updates the last purchase date with the given date.
        """
        # Set the last purchase date to the provided date
        self.__lastPurchaseDate = date
        print(f"Last purchase date updated to: {date}")

    def viewHistory(self):
        """
        Displays all the bookings in the customer's purchase history.
        """
        print("Customer Purchase History:")
        # Loop through the bookings and display their details
        for booking in self.__bookings:
            print(f"- Booking ID: {booking.getBookingID()} | Ticket: {booking.getTicket().getTicketID()} | Date: {booking.getBookingDate()}")
        # Return the list of bookings for reference
        return self.__bookings
