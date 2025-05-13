# CashTest.py
# This script tests the functionality of the Cash class,
# including creating cash payments, updating details, calculating change,
# processing payments, and handling errors.

# Import the Cash class for testing
from Cash import Cash

print("\nTest Case 1: Creating Cash Objects")
try:
    # Creating two Cash payment objects with payment details
    cash1 = Cash("P001", 500.0, "2025-05-12", 600.0)
    cash2 = Cash("P002", 1000.0, "2025-06-18", 1100.0)

    # Displaying the details of both cash payments to confirm successful creation
    print(
        f"Cash 1 created successfully: {cash1.getPaymentID()} {cash1.getAmount()} {cash1.getPaymentDate()} {cash1.getCashReceived()} {cash1.getStatus()}")
    print(
        f"Cash 2 created successfully: {cash2.getPaymentID()} {cash2.getAmount()} {cash2.getPaymentDate()} {cash2.getCashReceived()} {cash2.getStatus()}")

except Exception as e:
    # If there is an error during cash payment creation, it will be displayed here
    print(f"Error during cash creation: {e}")

print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original values of cash1 using getters
    print(f"Cash 1 ID: {cash1.getPaymentID()}")
    print(f"Cash 1 Amount: {cash1.getAmount()}")
    print(f"Cash 1 Date: {cash1.getPaymentDate()}")
    print(f"Cash 1 Cash Received: {cash1.getCashReceived()}")
    print(f"Cash 1 Status: {cash1.getStatus()}")

    # Updating cash payment details using setter methods
    cash1.setPaymentID("P003")
    cash1.setAmount(750.0)
    cash1.setPaymentDate("2025-07-10")
    cash1.setCashReceived(800.0)
    cash1.setChangeGiven(50.0)

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Cash 1 ID: {cash1.getPaymentID()}")
    print(f"Updated Cash 1 Amount: {cash1.getAmount()}")
    print(f"Updated Cash 1 Date: {cash1.getPaymentDate()}")
    print(f"Updated Cash 1 Cash Received: {cash1.getCashReceived()}")
    print(f"Updated Cash 1 Change Given: {cash1.getChangeGiven()}")

except Exception as e:
    # If there is an error during getter or setter testing, it will be displayed here
    print(f"Error during getter and setter testing: {e}")

print("\nTest Case 3: Calculating Change")
try:
    # Attempting to calculate the change after receiving cash
    change = cash1.calculateChange()

    # Displaying the calculated change to confirm it worked
    print(f"Change calculated successfully: {change}")

except Exception as e:
    # If there is an error during change calculation, it will be displayed here
    print(f"Error during change calculation: {e}")

print("\nTest Case 4: Processing Cash Payment")
try:
    # Attempting to process the cash payment
    success = cash1.processPayment()

    # If the payment is successful, display the new status and change given
    if success:
        print(f"Cash payment processed successfully: {cash1.getStatus()} | Change Given: {cash1.getChangeGiven()}")
    else:
        print("Cash payment processing failed.")

except Exception as e:
    # If there is an error during payment processing, it will be displayed here
    print(f"Error during cash payment processing: {e}")

print("\nTest Case 5: Error Handling")
try:
    # Trying to set negative values for cash received and change given
    cash1.setCashReceived(-100)  # This should trigger an error
    cash1.setChangeGiven(-50)  # This should also trigger an error

    # Attempting to process payment with negative values
    cash1.processPayment()

except Exception as e:
    # If there is an error, it will be displayed and handled properly
    print(f"Handled Error: {e}")
