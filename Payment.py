# Payment.py

class Payment:
    """
    Payment class handles the payment details for bookings,
    including processing payments and handling refunds.
    """

    def __init__(self, paymentID, amount, paymentDate):
        """
        Constructor to initialize Payment attributes.
        """
        self.__paymentID = paymentID             # Private attribute for Payment ID
        self.__amount = amount                   # Private attribute for the amount paid
        self.__paymentDate = paymentDate         # Private attribute for the date of payment
        self.__status = "Pending"                # Private attribute for the status of the payment (default: Pending)
        self.__description = ""                  # Private attribute for the description of the payment


    # Getters and Setters


    def getPaymentID(self):
        """
        Returns the Payment ID.
        """
        return self.__paymentID

    def setPaymentID(self, id):
        """
        Sets the Payment ID.
        """
        self.__paymentID = id

    def getAmount(self):
        """
        Returns the payment amount.
        """
        return self.__amount

    def setAmount(self, amount):
        """
        Sets the payment amount.
        """
        try:
            if amount >= 0:
                self.__amount = amount
            else:
                raise ValueError("Amount cannot be negative.")
        except ValueError as e:
            print("Error setting amount:", e)

    def getPaymentDate(self):
        """
        Returns the payment date.
        """
        return self.__paymentDate

    def setPaymentDate(self, date):
        """
        Sets the payment date.
        """
        self.__paymentDate = date

    def getStatus(self):
        """
        Returns the status of the payment.
        """
        return self.__status

    def setStatus(self, status):
        """
        Sets the status of the payment.
        """
        self.__status = status

    def getDescription(self):
        """
        Returns the description of the payment.
        """
        return self.__description

    def setDescription(self, desc):
        """
        Sets the description of the payment.
        """
        self.__description = desc


    # Methods

    def processPayment(self):
        """
        Processes the payment and updates the status to 'Completed'.
        """
        try:
            if self.__amount > 0:
                self.__status = "Completed"
                print(f"Payment of {self.__amount} processed successfully.")
                return True
            else:
                raise ValueError("Payment amount must be greater than 0.")
        except ValueError as e:
            print("Error processing payment:", e)
            return False

    def refundPayment(self):
        """
        Refunds the payment and updates the status to 'Refunded'.
        """
        try:
            if self.__status == "Completed":
                self.__status = "Refunded"
                print(f"Payment with ID {self.__paymentID} has been refunded.")
                return True
            else:
                raise ValueError("Payment must be completed before a refund.")
        except ValueError as e:
            print("Error refunding payment:", e)
            return False
