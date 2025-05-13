# EventTest.py
# This script tests the functionality of the Event class,
# including creating events, adding tickets and users, and managing them.

# Import necessary classes
from Event import Event
from User import User

# ============================
# Test Case 1: Creating Event Objects
# ============================
print("\n--- Test Case 1: Creating Event Objects ---")
try:
    # Creating Event objects with details like name, location, date, capacity, and type
    event1 = Event("Formula 1", "Yas Marina Circuit", "2025-05-11", 3, "Sports")

    # Displaying the details of the event to confirm successful creation
    print("Event 1 created successfully:", event1.getName(), event1.getLocation(), event1.getDate(), event1.getTotalCapacity(), event1.getEventType())

    # Displaying all tickets created through composition
    print("\n--- Tickets created through composition ---")
    event1.displayTickets()

except Exception as e:
    # If there is any error during event creation, it gets printed here
    print("Error during event creation:", e)

# ============================
# Test Case 2: Testing Getters and Setters
# ============================
print("\n--- Test Case 2: Testing Getters and Setters ---")
try:
    # Testing Getters to fetch current event information
    print("Event 1 Name:", event1.getName())
    print("Event 1 Location:", event1.getLocation())
    print("Event 1 Date:", event1.getDate())
    print("Event 1 Capacity:", event1.getTotalCapacity())
    print("Event 1 Type:", event1.getEventType())

    # Testing Setters to update event information
    event1.setName("Grand Prix 2025")
    event1.setLocation("Yas Island")
    event1.setDate("2025-12-01")
    event1.setTotalCapacity(5)
    event1.setEventType("Racing")

    # Displaying updated values to confirm setters worked
    print("\n--- After Updates ---")
    print("Updated Event 1 Name:", event1.getName())
    print("Updated Event 1 Location:", event1.getLocation())
    print("Updated Event 1 Date:", event1.getDate())
    print("Updated Event 1 Capacity:", event1.getTotalCapacity())
    print("Updated Event 1 Type:", event1.getEventType())

except Exception as e:
    # If there is any error during getter or setter tests, it gets printed here
    print("Error during getters/setters test:", e)

# ============================
# Test Case 3: Adding and Removing Tickets
# ============================
print("\n--- Test Case 3: Adding and Removing Tickets ---")
try:
    # Adding new tickets directly through Event (Composition)
    event1.addTicket("T004", "Gold", 2000.0, "D20", True)
    event1.addTicket("T005", "Silver", 1000.0, "D21", True)

    # Displaying all tickets after addition
    print("\n--- Tickets after adding new tickets ---")
    event1.displayTickets()

    # Removing one ticket from the event's list
    ticket_to_remove = event1.getTicketList()[0]  # Get the first ticket
    event1.removeTicket(ticket_to_remove)

    # Displaying the list of tickets after one removal
    print("\n--- Tickets after removal ---")
    event1.displayTickets()

except Exception as e:
    # If there is any error during ticket addition or removal, it gets printed here
    print("Error during ticket management test:", e)

# ============================
# Test Case 4: Adding and Removing Users
# ============================
print("\n--- Test Case 4: Adding and Removing Users ---")
try:
    # Creating User objects with ID, name, email, password, and contact number
    user1 = User("U001", "maha", "maha@gmail.com", "pass123", "0501234567")
    user2 = User("U002", "hamdan", "hamdan@gmail.com", "pass456", "0507654321")

    # Adding the users to the event's user list
    event1.addUser(user1)
    event1.addUser(user2)

    # Displaying all users added to the event
    print("Users added to event:", [user.getUsername() for user in event1.getUserList()])

    # Removing one user from the list
    event1.removeUser(user1)

    # Displaying the list of users after one removal
    print("Users after removal:", [user.getUsername() for user in event1.getUserList()])

except Exception as e:
    # If there is any error during user addition or removal, it gets printed here
    print("Error during user management test:", e)

# ============================
# Test Case 5: Testing Available Tickets
# ============================
print("\n--- Test Case 5: Testing Available Tickets ---")
try:
    # Retrieving only the tickets that are currently marked as available
    available_tickets = event1.getAvailableTickets()

    # Displaying the IDs of the available tickets
    print("Available Tickets:", [ticket.getTicketID() for ticket in available_tickets])

except Exception as e:
    # If there is any error during available ticket check, it gets printed here
    print("Error during available tickets test:", e)
