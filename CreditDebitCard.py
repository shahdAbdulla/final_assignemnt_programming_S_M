# CreditDebitCard.py
# This class handles credit and debit card payments.
# It extends the Payment class and includes additional attributes
# specific to card transactions, such as card number, cardholder name, expiry date, and CVV.

from Payment import Payment

class CreditDebitCard(Payment):
    def __init__(self, paymentID, amount, payment_date, card_number, cardholder_name, expiry_date, cvv):
        """
        Constructor to initialize CreditDebitCard attributes
        """
        # Inherit common attributes from the Payment class
        super().__init__(paymentID, amount, payment_date)

        # Private attributes specific to card payments
        self.__card_number = card_number           # The 16-digit card number
        self.__cardholder_name = cardholder_name   # The name of the cardholder
        self.__expiry_date = expiry_date           # The expiry date of the card
        self.__cvv = cvv                           # The 3-digit security code (CVV)


    # Setters and Getters

    def set_card_number(self, number):
        """
        Sets the card number if it is exactly 16 digits long and only contains numbers.
        """
        if len(number) == 16 and number.isdigit():
            self.__card_number = number
        else:
            # Display an error message if the card number is not valid
            print("Card number must be 16 digits long.")

    def get_card_number(self):
        """
        Returns the card number.
        """
        return self.__card_number

    def set_cardholder_name(self, name):
        """
        Sets the cardholder's name if it is not empty.
        """
        if len(name) > 0:
            self.__cardholder_name = name
        else:
            # Display an error message if the name is empty
            print("Cardholder name cannot be empty.")

    def get_cardholder_name(self):
        """
        Returns the cardholder's name.
        """
        return self.__cardholder_name

    def set_expiry_date(self, date):
        """
        Sets the expiry date of the card.
        """
        self.__expiry_date = date

    def get_expiry_date(self):
        """
        Returns the expiry date of the card.
        """
        return self.__expiry_date

    def set_cvv(self, cvv):
        """
        Sets the CVV if it is exactly 3 digits long and only contains numbers.
        """
        if len(cvv) == 3 and cvv.isdigit():
            self.__cvv = cvv
        else:
            # Display an error message if the CVV is not valid
            print("CVV must be 3 digits long.")

    def get_cvv(self):
        """
        Returns the CVV of the card.
        """
        return self.__cvv


    # Methods

    def validate_card(self):
        """
        Validates the card number, expiry date, and CVV.
        It checks that the card number is 16 digits and the CVV is 3 digits.
        """
        try:
            # Check if the card number is 16 digits and numeric
            if len(self.__card_number) == 16 and self.__card_number.isdigit():
                # Check if the CVV is 3 digits and numeric
                if len(self.__cvv) == 3 and self.__cvv.isdigit():
                    print("Card is valid.")
                    return True
                else:
                    # Display a message if the CVV is not valid
                    print("Invalid CVV.")
            else:
                # Display a message if the card number is not valid
                print("Invalid card number.")
            return False
        except Exception as e:
            # Display the error message if there is an exception
            print(f"Error: {e} - Could not validate the card.")
            return False


    def processPayment(self):
        """
        Processes the card payment if the card is valid.
        Marks the status as 'Completed' if successful, otherwise 'Failed'.
        """
        try:
            # Validate the card before processing the payment
            if self.validate_card():
                # Set the status to completed if the card is valid
                self.setStatus("Completed")
                # Display a message showing the last 4 digits of the card
                print(f"Payment '{self.getPaymentID()}' processed successfully using card ending with {self.__card_number[-4:]}")
                return True
            else:
                # Set the status to failed if validation fails
                print(f"Payment '{self.getPaymentID()}' failed. Card validation unsuccessful.")
                self.setStatus("Failed")
                return False
        except Exception as e:
            # Display the error if payment processing fails
            print(f"Error: {e} - Could not process the payment.")
            return False
