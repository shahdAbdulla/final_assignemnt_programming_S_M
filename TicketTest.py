# MasterTest_Ticket.py
# This script tests the functionality of the Ticket class,
# including creating ticket objects, updating details,
# calculating discounts, and integrating tickets with an event.


from Ticket import Ticket
from Event import Event


print("\nTest Case 1: Creating Ticket Objects")
try:
   # Creating two Ticket objects with initial details
   ticket1 = Ticket("T001", "VIP", 1500.0, "A12", True)
   ticket2 = Ticket("T002", "Standard", 500.0, "B15", False)


   # Displaying the details of both tickets to confirm successful creation
   print("Ticket 1 created successfully:", ticket1.getTicketID(), ticket1.getType(), ticket1.getPrice(),
         ticket1.getSeatNumber(), ticket1.getIsAvailable())
   print("Ticket 2 created successfully:", ticket2.getTicketID(), ticket2.getType(), ticket2.getPrice(),
         ticket2.getSeatNumber(), ticket2.getIsAvailable())


except Exception as e:
   # If there is an error during ticket creation, it will be displayed here
   print("Error during ticket creation:", e)


print("\nTest Case 2: Testing Getters and Setters")
try:
   # Displaying the original values of ticket1 using getters
   print("Ticket 1 ID:", ticket1.getTicketID())
   print("Ticket 1 Type:", ticket1.getType())
   print("Ticket 1 Price:", ticket1.getPrice())
   print("Ticket 1 Seat Number:", ticket1.getSeatNumber())
   print("Ticket 1 Availability:", ticket1.getIsAvailable())


   # Updating ticket details using setter methods
   ticket1.setTicketID("T003")
   ticket1.setType("Gold")
   ticket1.setPrice(2000.0)
   ticket1.setSeatNumber("A15")
   ticket1.setIsAvailable(False)


   # Displaying the updated values to confirm the changes
   print("\nAfter Updates")
   print("Updated Ticket 1 ID:", ticket1.getTicketID())
   print("Updated Ticket 1 Type:", ticket1.getType())
   print("Updated Ticket 1 Price:", ticket1.getPrice())
   print("Updated Ticket 1 Seat Number:", ticket1.getSeatNumber())
   print("Updated Ticket 1 Availability:", ticket1.getIsAvailable())


except Exception as e:
   # If there is an error during getter or setter testing, it will be displayed here
   print("Error during getters/setters test:", e)


print("\nTest Case 3: Testing Discount Calculation")
try:
   # Displaying the original price and the discounted price for the tickets
   print("Original Price for VIP:", ticket1.getPrice())
   print("Discounted Price for VIP:", ticket1.calculateDiscount())


   print("Original Price for Standard:", ticket2.getPrice())
   print("Discounted Price for Standard:", ticket2.calculateDiscount())


except Exception as e:
   # If there is an error during discount calculation, it will be displayed here
   print("Error during discount calculation test:", e)


print("\nTest Case 4: Integrating with Event")
try:
   # Creating an Event object for testing
   event1 = Event("Formula 1", "Yas Marina Circuit", "2025-05-11", 5000, "Sports")


   # Displaying the event details to confirm its creation
   print("Event created successfully:", event1.getName(), event1.getLocation(), event1.getDate())

except Exception as e:
   # If there is an error during event integration, it will be displayed here
   print("Error during event integration test:", e)