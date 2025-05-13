# Cash.py
# This class handles cash payments, calculating the change to be returned
# and processing the payment by extending the Payment class.

from Payment import Payment

class Cash(Payment):
    """
    Cash class is a subclass of Payment that handles
    cash payments and calculates the change given.
    """

    def __init__(self, paymentID, amount, paymentDate, cashReceived):
        """
        Constructor to initialize Cash attributes.
        Inherits attributes from Payment and adds specific ones.
        """
        # Calling the parent constructor to initialize payment details
        super().__init__(paymentID, amount, paymentDate)

        # Private attributes specific to cash payments
        self.__cashReceived = cashReceived    # Total cash received during the transaction
        self.__changeGiven = 0.0              # Change to be returned, starts at 0.0


    # Getters and Setters

    def getCashReceived(self):
        """
        Returns the amount of cash received during payment.
        """
        return self.__cashReceived

    def setCashReceived(self, cash):
        """
        Sets the amount of cash received if it is non-negative.
        """
        try:
            # Ensure the cash amount is not negative
            if cash >= 0:
                self.__cashReceived = cash
            else:
                # Raise an error if the value is negative
                raise ValueError("Cash received cannot be negative.")
        except ValueError as e:
            # Display an error message if the cash value is not valid
            print("Error setting cash received:", e)

    def getChangeGiven(self):
        """
        Returns the change given back to the customer.
        """
        return self.__changeGiven

    def setChangeGiven(self, change):
        """
        Sets the change amount if it is non-negative.
        """
        try:
            # Ensure the change amount is not negative
            if change >= 0:
                self.__changeGiven = change
            else:
                # Raise an error if the value is negative
                raise ValueError("Change cannot be negative.")
        except ValueError as e:
            # Display an error message if the change value is not valid
            print("Error setting change given:", e)


    # Methods

    def calculateChange(self):
        """
        Calculates the change to be returned to the customer.
        The change is the difference between cash received and the amount.
        """
        try:
            # Check if the cash received is enough to cover the amount
            if self.__cashReceived >= self.getAmount():
                # Calculate the change to be given back
                self.__changeGiven = self.__cashReceived - self.getAmount()
                return self.__changeGiven
            else:
                # Raise an error if not enough cash was received
                raise ValueError("Insufficient cash received.")
        except ValueError as e:
            # Display an error if the calculation fails
            print("Error calculating change:", e)
            return 0.0

    def processPayment(self):
        """
        Processes the payment if enough cash is provided.
        Updates the status to "Completed" and calculates the change.
        """
        try:
            # Check if the received cash is enough to cover the payment amount
            if self.__cashReceived >= self.getAmount():
                # Calculate the change and complete the payment
                self.calculateChange()
                self.setStatus("Completed")
                print(f"Cash payment of {self.getAmount()} processed. Change given: {self.__changeGiven}")
                return True
            else:
                # Raise an error if there is not enough cash
                raise ValueError("Insufficient cash to complete the payment.")
        except ValueError as e:
            # Display an error if processing fails
            print("Error processing cash payment:", e)
            return False
