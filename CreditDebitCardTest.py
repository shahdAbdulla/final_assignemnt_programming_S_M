# CreditDebitCardTest.py
# This script tests the functionality of the CreditDebitCard class,
# including creating card payments, updating details, validating the card,
# processing payments, and handling errors.

# Import the CreditDebitCard class for testing
from CreditDebitCard import CreditDebitCard


print("\nTest Case 1: Creating CreditDebitCard Objects")
try:
    # Creating two CreditDebitCard objects with card details
    card1 = CreditDebitCard("P001", 500.0, "2025-05-12", "1234567890123456", "Maha Alhosani", "12/25", "123")
    card2 = CreditDebitCard("P002", 1000.0, "2025-06-18", "6543210987654321", "Hamdan Alhosani", "11/26", "456")

    # Displaying the details of both cards to confirm successful creation
    print(f"Card 1 created successfully: {card1.get_card_number()} {card1.get_cardholder_name()} {card1.get_expiry_date()} {card1.get_cvv()}")
    print(f"Card 2 created successfully: {card2.get_card_number()} {card2.get_cardholder_name()} {card2.get_expiry_date()} {card2.get_cvv()}")

except Exception as e:
    # If there is an error during card creation, it will be displayed here
    print(f"Error during CreditDebitCard creation: {e}")


print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original values of card1 using getters
    print(f"Card Number: {card1.get_card_number()}")
    print(f"Cardholder Name: {card1.get_cardholder_name()}")
    print(f"Expiry Date: {card1.get_expiry_date()}")
    print(f"CVV: {card1.get_cvv()}")

    # Updating card details using setter methods
    card1.set_card_number("0987654321098765")
    card1.set_cardholder_name("Maha Updated")
    card1.set_expiry_date("01/28")
    card1.set_cvv("321")

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Card Number: {card1.get_card_number()}")
    print(f"Updated Cardholder Name: {card1.get_cardholder_name()}")
    print(f"Updated Expiry Date: {card1.get_expiry_date()}")
    print(f"Updated CVV: {card1.get_cvv()}")

except Exception as e:
    # If there is an error during getter or setter testing, it will be displayed here
    print(f"Error during getter and setter testing: {e}")


print("\nTest Case 3: Validating the Card")
try:
    # Validating both card1 and card2 to check if they are valid
    print("\nValidating Card 1:")
    card1.validate_card()

    print("\nValidating Card 2:")
    card2.validate_card()

except Exception as e:
    # If there is an error during card validation, it will be displayed here
    print(f"Error during card validation: {e}")


print("\nTest Case 4: Processing Card Payment")
try:
    # Attempting to process payments for both cards
    print("\nProcessing Payment for Card 1:")
    card1.processPayment()

    print("\nProcessing Payment for Card 2:")
    card2.processPayment()

except Exception as e:
    # If there is an error during card payment processing, it will be displayed here
    print(f"Error during card payment processing: {e}")


print("\nTest Case 5: Error Handling")
try:
    # Attempting to set an invalid card number (less than 16 digits)
    print("\nTesting Invalid Card Number:")
    card1.set_card_number("123")  # Invalid length
    card1.validate_card()

    # Attempting to set an invalid CVV (less than 3 digits)
    print("\nTesting Invalid CVV:")
    card1.set_cvv("12")  # Invalid length
    card1.validate_card()

    # Attempting to set an empty cardholder name
    print("\nTesting Empty Cardholder Name:")
    card1.set_cardholder_name("")  # Empty name

except Exception as e:
    # If there is an error during the error handling tests, it will be displayed here
    print(f"Error during error handling tests: {e}")
