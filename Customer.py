# Import the Booking class to handle customer bookings
from Booking import Booking


class Customer:
    def __init__(self, userID, username, email, password, contactNumber):
        """
        Constructor to initialize Customer attributes.
        """
        # Protected attributes for customer details
        self._userID = userID  # Unique ID for the customer
        self._username = username  # Username for login
        self._email = email  # Customer's email address
        self._password = password  # Customer's password
        self._contactNumber = contactNumber  # Customer's contact number
        self._bookings = []  # List to store all bookings made by the customer
        self._purchaseHistory = None  # Attribute to store the purchase history

    # --- Getters and Setters ---
    def getUserID(self):
        """
        Returns the User ID.
        """
        return self._userID

    def setUserID(self, userID):
        """
        Sets the User ID.
        """
        self._userID = userID

    def getUsername(self):
        """
        Returns the Username.
        """
        return self._username

    def setUsername(self, username):
        """
        Sets the Username.
        """
        self._username = username

    def getEmail(self):
        """
        Returns the Customer's Email.
        """
        return self._email

    def setEmail(self, email):
        """
        Sets the Customer's Email.
        """
        self._email = email

    def getPassword(self):
        """
        Returns the Customer's Password.
        """
        return self._password

    def setPassword(self, password):
        """
        Sets the Customer's Password.
        """
        self._password = password

    def getContactNumber(self):
        """
        Returns the Customer's Contact Number.
        """
        return self._contactNumber

    def setContactNumber(self, contactNumber):
        """
        Sets the Customer's Contact Number.
        """
        self._contactNumber = contactNumber

    # --- Methods for Booking and History ---
    def makeBooking(self, ticket, payment):
        """
        Creates a new Booking for the Customer.
        """
        try:
            # Create a new Booking instance
            # Booking format: (Booking ID, Customer, Ticket, Date, Status)
            booking = Booking("B001", self, ticket, "2025-05-11", "Pending")

            # Associate the payment with the booking
            booking.setPayment(payment)

            # Add the new booking to the customer's booking list
            self._bookings.append(booking)

            # Display a confirmation message with the Ticket ID
            print(f"Booking made successfully for Ticket ID: {ticket.getTicketID()}")
            return booking
        except Exception as e:
            # If any error occurs during booking, it gets printed here
            print(f"Booking error: {e}")
            return None

    def viewPurchaseHistory(self):
        """
        Displays the customer's purchase history if available.
        """
        if self._purchaseHistory is not None:
            return self._purchaseHistory
        else:
            print("No purchase history found.")
            return None

    def getBookings(self):
        """
        Returns the list of all bookings made by the customer.
        """
        return self._bookings

    def getPurchaseHistory(self):
        """
        Returns the purchase history of the customer.
        """
        return self._purchaseHistory

    def setPurchaseHistory(self, history):
        """
        Sets the purchase history of the customer.
        """
        self._purchaseHistory = history

