# PurchaseHistoryTest.py
# This script tests the functionality of the PurchaseHistory class,
# including creating purchase histories, adding and removing bookings,
# calculating the total amount spent, and viewing the full history.

# Import necessary classes
from PurchaseHistory import PurchaseHistory
from Booking import Booking
from Customer import Customer
from Ticket import Ticket

print("\nTest Case 1: Creating PurchaseHistory Object")
try:
    # Creating a PurchaseHistory object for a specific customer
    purchase_history = PurchaseHistory("C001")

    # Displaying confirmation message with the customer ID
    print(f"PurchaseHistory created successfully for Customer ID: {purchase_history.getCustomerID()}")

except Exception as e:
    # If there is an error during creation, it will be displayed here
    print(f"Error during PurchaseHistory creation: {e}")

print("\nTest Case 2: Testing Getters and Setters")
try:
    # Testing getter methods to retrieve details
    print(f"Customer ID: {purchase_history.getCustomerID()}")
    print(f"Total Spent: {purchase_history.getTotalSpent()}")
    print(f"Last Purchase Date: {purchase_history.getLastPurchaseDate()}")

    # Setting new values for the attributes
    purchase_history.setCustomerID("C002")
    purchase_history.setTotalSpent(1000.0)
    purchase_history.setLastPurchaseDate("2025-08-15")

    # Displaying the updated values to confirm changes
    print("\nAfter Updates")
    print(f"Updated Customer ID: {purchase_history.getCustomerID()}")
    print(f"Updated Total Spent: {purchase_history.getTotalSpent()}")
    print(f"Updated Last Purchase Date: {purchase_history.getLastPurchaseDate()}")

except Exception as e:
    # If there is an error during getter or setter testing, it will be displayed here
    print(f"Error during getter and setter testing: {e}")

print("\nTest Case 3: Adding and Removing Bookings")
try:
    # Creating Customer, Ticket, and Booking objects to simulate purchases
    customer1 = Customer("C001", "maha", "maha@gmail.com", "pass123", "0501234567")

    # Creating two tickets and corresponding bookings
    ticket1 = Ticket("T001", "VIP", 1500.0, "A12", True)
    booking1 = Booking("B001", customer1, ticket1, "2025-05-12", "Confirmed")

    ticket2 = Ticket("T002", "Standard", 800.0, "B15", True)
    booking2 = Booking("B002", customer1, ticket2, "2025-06-15", "Confirmed")

    # Adding these bookings to the purchase history
    purchase_history.addBooking(booking1)
    purchase_history.addBooking(booking2)

    # Displaying all current bookings in the purchase history
    print("Current Bookings:")
    for b in purchase_history.getBookings():
        print(
            f"- Booking ID: {b.getBookingID()} | Ticket: {b.getTicket().getTicketID()} | Price: {b.getTicket().getPrice()}")

    # Removing one of the bookings from the list
    purchase_history.removeBooking("B001")

    # Displaying the list of bookings after removal
    print("\nAfter removal:")
    for b in purchase_history.getBookings():
        print(
            f"- Booking ID: {b.getBookingID()} | Ticket: {b.getTicket().getTicketID()} | Price: {b.getTicket().getPrice()}")

except Exception as e:
    # If there is an error during adding or removing bookings, it will be displayed here
    print(f"Error during adding and removing bookings: {e}")

print("\nTest Case 4: Calculating Total Spent")
try:
    # Recalculating the total spent based on the prices of current bookings
    purchase_history.calculateTotalSpent()

    # Displaying the total amount spent after calculation
    print(f"Total Spent after calculation: {purchase_history.getTotalSpent()}")

except Exception as e:
    # If there is an error during the total calculation, it will be displayed here
    print(f"Error during total spent calculation: {e}")

print("\nTest Case 5: Viewing History")
try:
    # Creating another ticket and booking for testing the view history
    ticket3 = Ticket("T003", "General", 300.0, "C10", True)
    booking3 = Booking("B003", customer1, ticket3, "2025-07-20", "Confirmed")

    # Adding the new booking to the purchase history
    purchase_history.addBooking(booking3)

    # Displaying the full history of bookings for the customer
    print("\nCustomer Purchase History")
    purchase_history.viewHistory()

except Exception as e:
    # If there is an error during viewing history, it will be displayed here
    print(f"Error during viewing history: {e}")
