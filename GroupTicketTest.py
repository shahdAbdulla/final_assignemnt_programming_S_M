# GroupTicketTest.py
# This script tests the functionality of the GroupTicket class,
# including creating group tickets, updating details, and checking their availability status.

from GroupTicket import GroupTicket


print("\nTest Case 1: Creating GroupTicket Objects")
try:
    # Creating two GroupTicket objects with their details
    ticket1 = GroupTicket("GT001", "Standard", 2000.0, "J10", True, 5)
    ticket2 = GroupTicket("GT002", "VIP", 5000.0, "K14", False, 10)

    # Displaying the details of both tickets to confirm successful creation
    print(f"Ticket 1 created successfully: {ticket1.getTicketID()} {ticket1.getType()} {ticket1.getPrice()} {ticket1.getSeatNumber()} {ticket1.getIsAvailable()} Group Size: {ticket1.getGroupSize()}")
    print(f"Ticket 2 created successfully: {ticket2.getTicketID()} {ticket2.getType()} {ticket2.getPrice()} {ticket2.getSeatNumber()} {ticket2.getIsAvailable()} Group Size: {ticket2.getGroupSize()}")

except Exception as e:
    # If there is an error during ticket creation, it will be displayed here
    print(f"Error during GroupTicket creation: {e}")


print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original values of ticket1 using getters
    print(f"Ticket ID: {ticket1.getTicketID()}")
    print(f"Type: {ticket1.getType()}")
    print(f"Price: {ticket1.getPrice()}")
    print(f"Seat Number: {ticket1.getSeatNumber()}")
    print(f"Is Available: {ticket1.getIsAvailable()}")
    print(f"Group Size: {ticket1.getGroupSize()}")

    # Updating ticket details using setter methods
    ticket1.setTicketID("GT003")
    ticket1.setType("Premium")
    ticket1.setPrice(6000.0)
    ticket1.setSeatNumber("L20")
    ticket1.setIsAvailable(False)
    ticket1.setGroupSize(8)

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Ticket ID: {ticket1.getTicketID()}")
    print(f"Updated Type: {ticket1.getType()}")
    print(f"Updated Price: {ticket1.getPrice()}")
    print(f"Updated Seat Number: {ticket1.getSeatNumber()}")
    print(f"Updated Availability: {ticket1.getIsAvailable()}")
    print(f"Updated Group Size: {ticket1.getGroupSize()}")

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
