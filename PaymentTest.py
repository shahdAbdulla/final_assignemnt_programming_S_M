# PaymentTest.py
# This script tests the functionality of the Payment class,
# including creating payments, updating details, processing, refunding, and handling errors.

# Import the Payment class for testing
from Payment import Payment

print("\nTest Case 1: Creating Payment Objects")
try:
    # Creating two Payment objects with payment details
    payment1 = Payment("P001", 500.0, "2025-05-12")
    payment2 = Payment("P002", 1000.0, "2025-06-18")

    # Displaying the details of both payments to confirm successful creation
    print(
        f"Payment 1 created successfully: {payment1.getPaymentID()} {payment1.getAmount()} {payment1.getPaymentDate()} {payment1.getStatus()}")
    print(
        f"Payment 2 created successfully: {payment2.getPaymentID()} {payment2.getAmount()} {payment2.getPaymentDate()} {payment2.getStatus()}")

except Exception as e:
    # If there is an error during payment creation, it will be displayed here
    print(f"Error during payment creation: {e}")

print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original values of payment1 using getters
    print(f"Payment 1 ID: {payment1.getPaymentID()}")
    print(f"Payment 1 Amount: {payment1.getAmount()}")
    print(f"Payment 1 Date: {payment1.getPaymentDate()}")
    print(f"Payment 1 Status: {payment1.getStatus()}")

    # Updating payment details using setter methods
    payment1.setPaymentID("P003")
    payment1.setAmount(750.0)
    payment1.setPaymentDate("2025-07-10")
    payment1.setStatus("Pending")
    payment1.setDescription("Early bird discount applied")

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Payment 1 ID: {payment1.getPaymentID()}")
    print(f"Updated Payment 1 Amount: {payment1.getAmount()}")
    print(f"Updated Payment 1 Date: {payment1.getPaymentDate()}")
    print(f"Updated Payment 1 Status: {payment1.getStatus()}")
    print(f"Updated Payment 1 Description: {payment1.getDescription()}")

except Exception as e:
    # If there is an error during getter or setter testing, it will be displayed here
    print(f"Error during getter and setter testing: {e}")

print("\nTest Case 3: Processing Payment")
try:
    # Attempting to process the payment
    success = payment1.processPayment()

    # If the payment is successful, display the new status
    if success:
        print(f"Payment processed successfully: {payment1.getStatus()}")
    else:
        print("Payment processing failed.")

except Exception as e:
    # If there is an error during payment processing, it will be displayed here
    print(f"Error during payment processing: {e}")

print("\nTest Case 4: Refunding Payment")
try:
    # Attempting to refund the payment
    refunded = payment1.refundPayment()

    # If the refund is successful, display the new status
    if refunded:
        print(f"Payment refunded successfully: {payment1.getStatus()}")
    else:
        print("Refund failed.")

except Exception as e:
    # If there is an error during the refund process, it will be displayed here
    print(f"Error during refunding payment: {e}")

print("\nTest Case 5: Invalid Operations")
try:
    # Trying to set a negative amount (should throw an error)
    payment2.setAmount(-500.0)

    # Attempting to process and refund a negative payment amount
    payment2.processPayment()
    payment2.refundPayment()

except Exception as e:
    # Displaying the handled error if an exception is thrown
    print(f"Handled Error: {e}")
