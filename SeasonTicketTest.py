# SeasonTicketTest.py
# This script tests the functionality of the SeasonTicket class,
# including creating season tickets, updating details, and checking their availability status.

from SeasonTicket import SeasonTicket


print("\nTest Case 1: Creating SeasonTicket Objects")
try:
    # Creating two SeasonTicket objects with their details
    ticket1 = SeasonTicket("ST001", "Standard", 1500.0, "F10", True, "March 2025 - September 2025")
    ticket2 = SeasonTicket("ST002", "VIP", 2500.0, "G14", False, "February 2025 - November 2025")

    # Displaying the details of both tickets to confirm successful creation
    print(f"Ticket 1 created successfully: {ticket1.getTicketID()} {ticket1.getType()} {ticket1.getPrice()} {ticket1.getSeatNumber()} {ticket1.getIsAvailable()} {ticket1.getSeasonDuration()}")
    print(f"Ticket 2 created successfully: {ticket2.getTicketID()} {ticket2.getType()} {ticket2.getPrice()} {ticket2.getSeatNumber()} {ticket2.getIsAvailable()} {ticket2.getSeasonDuration()}")

except Exception as e:
    # If there is an error during ticket creation, it will be displayed here
    print(f"Error during SeasonTicket creation: {e}")


print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original values of ticket1 using getters
    print(f"Ticket ID: {ticket1.getTicketID()}")
    print(f"Type: {ticket1.getType()}")
    print(f"Price: {ticket1.getPrice()}")
    print(f"Seat Number: {ticket1.getSeatNumber()}")
    print(f"Is Available: {ticket1.getIsAvailable()}")
    print(f"Season Duration: {ticket1.getSeasonDuration()}")

    # Updating ticket details using setter methods
    ticket1.setTicketID("ST003")
    ticket1.setType("Premium")
    ticket1.setPrice(3000.0)
    ticket1.setSeatNumber("H20")
    ticket1.setIsAvailable(False)
    ticket1.setSeasonDuration("April 2025 - October 2025")

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Ticket ID: {ticket1.getTicketID()}")
    print(f"Updated Type: {ticket1.getType()}")
    print(f"Updated Price: {ticket1.getPrice()}")
    print(f"Updated Seat Number: {ticket1.getSeatNumber()}")
    print(f"Updated Availability: {ticket1.getIsAvailable()}")
    print(f"Updated Season Duration: {ticket1.getSeasonDuration()}")

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
