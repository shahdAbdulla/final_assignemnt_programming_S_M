from WeekendTicket import WeekendTicket

# Test Case 1: Creating WeekendTicket Objects
print("\n--- Test Case 1: Creating WeekendTicket Objects ---")
try:
    # Creating two WeekendTicket objects with different attributes
    ticket1 = WeekendTicket("WT001", "Standard", 400.0, "C12", True, "June 14-15, 2025")
    ticket2 = WeekendTicket("WT002", "VIP", 800.0, "D14", False, "August 19-20, 2025")

    # Displaying ticket details for verification
    print(f"Ticket 1 created successfully: {ticket1.getTicketID()} {ticket1.getType()} {ticket1.getPrice()} {ticket1.getSeatNumber()} {ticket1.getIsAvailable()} {ticket1.getValidWeekend()}")
    print(f"Ticket 2 created successfully: {ticket2.getTicketID()} {ticket2.getType()} {ticket2.getPrice()} {ticket2.getSeatNumber()} {ticket2.getIsAvailable()} {ticket2.getValidWeekend()}")
except Exception as e:
    # Handling any errors during creation
    print(f"Error during WeekendTicket creation: {e}")

# Test Case 2: Testing Getters and Setters
print("\n--- Test Case 2: Testing Getters and Setters ---")
try:
    # Displaying current values using getters
    print(f"Ticket ID: {ticket1.getTicketID()}")
    print(f"Type: {ticket1.getType()}")
    print(f"Price: {ticket1.getPrice()}")
    print(f"Seat Number: {ticket1.getSeatNumber()}")
    print(f"Is Available: {ticket1.getIsAvailable()}")
    print(f"Valid Weekend: {ticket1.getValidWeekend()}")

    # Updating values using setters
    ticket1.setTicketID("WT003")
    ticket1.setType("Premium")
    ticket1.setPrice(900.0)
    ticket1.setSeatNumber("E20")
    ticket1.setIsAvailable(False)
    ticket1.setValidWeekend("July 20-21, 2025")

    # Displaying updated values for verification
    print("\n--- After Updates ---")
    print(f"Updated Ticket ID: {ticket1.getTicketID()}")
    print(f"Updated Type: {ticket1.getType()}")
    print(f"Updated Price: {ticket1.getPrice()}")
    print(f"Updated Seat Number: {ticket1.getSeatNumber()}")
    print(f"Updated Availability: {ticket1.getIsAvailable()}")
    print(f"Updated Valid Weekend: {ticket1.getValidWeekend()}")

except Exception as e:
    # Handling any errors during getter and setter tests
    print(f"Error during getter and setter testing: {e}")

# Test Case 3: Testing Availability
print("\n--- Test Case 3: Testing Availability ---")
try:
    # Checking if tickets are available
    print(f"Ticket 1 Availability: {ticket1.getIsAvailable()}")
    print(f"Ticket 2 Availability: {ticket2.getIsAvailable()}")
except Exception as e:
    # Handling any errors during availability check
    print(f"Error during availability check: {e}")
