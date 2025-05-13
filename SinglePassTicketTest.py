# SinglePassTicketTest.py
# This script tests the functionality of the SinglePassTicket class,
# including creating single-pass tickets, updating details,
# and checking their availability status.

from SinglePassTicket import SinglePassTicket


print("\nTest Case 1: Creating SinglePassTicket Objects")
try:
    # Creating two SinglePassTicket objects with their details
    ticket1 = SinglePassTicket("SP001", "Standard", 300.0, "A12", True, "2025-06-15")
    ticket2 = SinglePassTicket("SP002", "VIP", 500.0, "B14", False, "2025-08-20")

    # Displaying the details of both tickets to confirm successful creation
    print(f"Ticket 1 created successfully: {ticket1.getTicketID()} {ticket1.getType()} {ticket1.getPrice()} {ticket1.getSeatNumber()} {ticket1.getIsAvailable()} {ticket1.getValidDate()}")
    print(f"Ticket 2 created successfully: {ticket2.getTicketID()} {ticket2.getType()} {ticket2.getPrice()} {ticket2.getSeatNumber()} {ticket2.getIsAvailable()} {ticket2.getValidDate()}")

except Exception as e:
    # If there is an error during ticket creation, it will be displayed here
    print(f"Error during SinglePassTicket creation: {e}")


print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original values of ticket1 using getters
    print(f"Ticket ID: {ticket1.getTicketID()}")
    print(f"Type: {ticket1.getType()}")
    print(f"Price: {ticket1.getPrice()}")
    print(f"Seat Number: {ticket1.getSeatNumber()}")
    print(f"Is Available: {ticket1.getIsAvailable()}")
    print(f"Valid Date: {ticket1.getValidDate()}")

    # Updating ticket details using setter methods
    ticket1.setTicketID("SP003")
    ticket1.setType("Premium")
    ticket1.setPrice(450.0)
    ticket1.setSeatNumber("A20")
    ticket1.setIsAvailable(False)
    ticket1.setValidDate("2025-07-20")

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Ticket ID: {ticket1.getTicketID()}")
    print(f"Updated Type: {ticket1.getType()}")
    print(f"Updated Price: {ticket1.getPrice()}")
    print(f"Updated Seat Number: {ticket1.getSeatNumber()}")
    print(f"Updated Availability: {ticket1.getIsAvailable()}")
    print(f"Updated Valid Date: {ticket1.getValidDate()}")

except Exception as e:
    # If there is an error during getter or setter testing, it will be displayed here
    print(f"Error during getter and setter testing: {e}")


print("\nTest Case 3: Testing Availability")
try:
    # Displaying the availability status of both tickets
    print(f"Ticket 1 Availability: {ticket1.getIsAvailable()}")
    print(f"Ticket 2 Availability: {ticket2.getIsAvailable()}")

except Exception as e:
    # If there is an error during availability check, it will be displayed here
    print(f"Error during availability check: {e}")
