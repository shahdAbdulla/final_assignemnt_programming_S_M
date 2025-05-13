# BookingTest.py
# This script tests the functionality of the Booking class,
# including creating bookings, modifying details, confirming bookings, and canceling them.

# Import necessary classes
from Booking import Booking
from Customer import Customer
from Ticket import Ticket

print("\nTest Case 1: Creating Booking Objects")
try:
    # Creating a Customer object with user details
    customer1 = Customer("C001", "maha", "maha@gmail.com", "pass123", "0501234567")

    # Creating a Ticket object with ticket details
    ticket1 = Ticket("T001", "VIP", 1500.0, "A12", True)

    # Creating a Booking object that links the customer and the ticket
    booking1 = Booking("B001", customer1, ticket1, "2025-05-12", "Pending")

    # Displaying the booking details to confirm successful creation
    print(
        f"Booking 1 created successfully: {booking1.getBookingID()} {booking1.getCustomer().getUsername()} {booking1.getTicket().getTicketID()} {booking1.getBookingDate()} {booking1.getStatus()}")

except Exception as e:
    # If there is an error during booking creation, it will be displayed here
    print(f"Error during booking creation: {e}")

print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original details of the booking using getters
    print(f"Booking ID: {booking1.getBookingID()}")
    print(f"Customer: {booking1.getCustomer().getUsername()}")
    print(f"Ticket: {booking1.getTicket().getTicketID()}")
    print(f"Booking Date: {booking1.getBookingDate()}")
    print(f"Status: {booking1.getStatus()}")

    # Updating the booking details using setters
    booking1.setBookingID("B002")
    booking1.setBookingDate("2025-06-10")
    booking1.setStatus("Confirmed")

    # Displaying the updated booking details to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Booking ID: {booking1.getBookingID()}")
    print(f"Updated Booking Date: {booking1.getBookingDate()}")
    print(f"Updated Status: {booking1.getStatus()}")

except Exception as e:
    # If there is an error during getter or setter testing, it will be displayed here
    print(f"Error during getter and setter testing: {e}")

print("\nTest Case 3: Confirming a Booking")
try:
    # Creating a second Customer object
    customer2 = Customer("C002", "hamdan", "hamdan@gmail.com", "pass456", "0507654321")

    # Creating a second Ticket object
    ticket2 = Ticket("T002", "Standard", 500.0, "B15", True)

    # Creating a second Booking object with status "Pending"
    booking2 = Booking("B003", customer2, ticket2, "2025-07-01", "Pending")

    # Displaying the status before confirmation
    print(f"Booking Status before confirmation: {booking2.getStatus()}")

    # Confirming the booking and changing the status to "Confirmed"
    booking2.confirmBooking()

    # Displaying the status after confirmation
    print(f"Booking Status after confirmation: {booking2.getStatus()}")

except Exception as e:
    # If there is an error during booking confirmation, it will be displayed here
    print(f"Error during booking confirmation: {e}")

print("\nTest Case 4: Cancelling a Booking")
try:
    # Displaying the booking status before cancellation
    print(f"Booking Status before cancellation: {booking2.getStatus()}")

    # Attempting to cancel the booking; it only works if the status is "Confirmed"
    booking2.cancelBooking()

    # Displaying the status after cancellation
    print(f"Booking Status after cancellation: {booking2.getStatus()}")

except Exception as e:
    # If there is an error during booking cancellation, it will be displayed here
    print(f"Error during booking cancellation: {e}")
