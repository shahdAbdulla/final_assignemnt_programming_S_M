from Customer import Customer
from SinglePassTicket import SinglePassTicket
from WeekendTicket import WeekendTicket
from SeasonTicket import SeasonTicket
from GroupTicket import GroupTicket
from Cash import Cash
from CreditDebitCard import CreditDebitCard
from PurchaseHistory import PurchaseHistory

# Test Case 1: Full Integration Test

print("\n--- Main Test Case: Full Integration ---")

# Creating a Customer
print("\n--- Creating Customer ---")
customer = Customer("C001", "maha", "maha@gmail.com", "pass123", "0501234567")
# Display customer details to confirm creation
print(f"Customer created: {customer.getUserID()} | {customer.getUsername()} | {customer.getEmail()}")

# Creating Different Ticket Types
print("\n--- Creating Tickets ---")
ticket1 = SinglePassTicket("SP001", "Standard", 300.0, "A12", True, "2025-06-15")
ticket2 = WeekendTicket("WT001", "VIP", 600.0, "B14", True, "July 20-21, 2025")
ticket3 = SeasonTicket("ST001", "Premium", 2500.0, "C20", True, "March 2025 - September 2025")
ticket4 = GroupTicket("GT001", "Standard", 1500.0, "D10", True, 5)
# Display ticket IDs to confirm successful creation
print(f"Tickets created: {ticket1.getTicketID()}, {ticket2.getTicketID()}, {ticket3.getTicketID()}, {ticket4.getTicketID()}")

# Creating Payment Methods
print("\n--- Creating Payments ---")
cash_payment = Cash("P001", 300.0, "2025-05-12", 350.0)
card_payment = CreditDebitCard("P002", 600.0, "2025-06-18", "1234567890123456", "Maha Alhosani", "12/25", "123")
# Display a message to confirm payments were created
print("Payments created successfully.")

# Making Bookings for the Tickets
print("\n--- Making Bookings ---")
booking1 = customer.makeBooking(ticket1, cash_payment)  # Booking with cash payment
booking2 = customer.makeBooking(ticket2, card_payment)  # Booking with card payment
# Display a message to confirm bookings were made
print("Bookings created successfully.")

# Processing Payments for the Bookings
print("\n--- Processing Payments ---")
cash_payment.processPayment()
card_payment.processPayment()

# Confirming the Bookings
print("\n--- Confirming Bookings ---")
booking1.confirmBooking()
booking2.confirmBooking()

# Adding Bookings to the Customer's Purchase History
print("\n--- Adding to Purchase History ---")
purchase_history = PurchaseHistory(customer.getUserID())  # Create a purchase history for the customer
purchase_history.addBooking(booking1)  # Add the first booking
purchase_history.addBooking(booking2)  # Add the second booking
purchase_history.calculateTotalSpent()  # Calculate the total spent
purchase_history.updateLastPurchaseDate("2025-06-18")  # Update the last purchase date

# Viewing the Customer's Purchase History
print("\n--- Viewing Purchase History ---")
purchase_history.viewHistory()
# Display the total amount spent and the last purchase date
print(f"Total Spent: {purchase_history.getTotalSpent()}")
print(f"Last Purchase Date: {purchase_history.getLastPurchaseDate()}")
