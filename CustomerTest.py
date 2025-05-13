# CustomerTest.py
# This script tests the functionality of the Customer class,
# including creating customers, managing their details, making bookings,
# viewing purchase history, and integrating with Event objects.

# Import necessary classes
from Customer import Customer
from Ticket import Ticket
from Payment import Payment
from Event import Event

print("\nTest Case 1: Creating Customer Objects")
try:
    # Creating two Customer objects with their personal details
    customer1 = Customer("C001", "maha", "maha@gmail.com", "pass123", "0501234567")
    customer2 = Customer("C002", "hamdan", "hamdan@gmail.com", "pass456", "0507654321")

    # Displaying details of both customers to confirm successful creation
    print(
        f"Customer 1 created successfully: {customer1.getUserID()} {customer1.getUsername()} {customer1.getEmail()} {customer1.getContactNumber()}"
    )
    print(
        f"Customer 2 created successfully: {customer2.getUserID()} {customer2.getUsername()} {customer2.getEmail()} {customer2.getContactNumber()}"
    )

except Exception as e:
    # If there is an error during creation, it will be displayed here
    print(f"Error during customer creation: {e}")

print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the original details of customer1 using getter methods
    print(f"Customer 1 ID: {customer1.getUserID()}")
    print(f"Customer 1 Username: {customer1.getUsername()}")
    print(f"Customer 1 Email: {customer1.getEmail()}")
    print(f"Customer 1 Password: {customer1.getPassword()}")
    print(f"Customer 1 Contact Number: {customer1.getContactNumber()}")

    # Updating the details of customer1 using setter methods
    customer1.setUserID("C003")
    customer1.setUsername("maha_updated")
    customer1.setEmail("maha_updated@gmail.com")
    customer1.setPassword("newpass123")
    customer1.setContactNumber("0509999999")

    # Displaying the updated details to confirm the setters worked correctly
    print("\nAfter Updates")
    print(f"Updated Customer 1 ID: {customer1.getUserID()}")
    print(f"Updated Customer 1 Username: {customer1.getUsername()}")
    print(f"Updated Customer 1 Email: {customer1.getEmail()}")
    print(f"Updated Customer 1 Password: {customer1.getPassword()}")
    print(f"Updated Customer 1 Contact Number: {customer1.getContactNumber()}")

except Exception as e:
    # If there is an error during getter or setter tests, it will be displayed here
    print(f"Error during getter and setter testing: {e}")

print("\nTest Case 3: Making a Booking")
try:
    # Creating a Ticket object with ticket details
    ticket1 = Ticket("T001", "VIP", 1500.0, "A12", True)

    # Creating a Payment object with payment details
    payment1 = Payment("P001", 1500.0, "2025-05-11")

    # Making a booking for customer1 with the ticket and payment
    booking1 = customer1.makeBooking(ticket1, payment1)

except Exception as e:
    # If there is an error during booking, it will be displayed here
    print(f"Error during booking creation: {e}")

print()

print("\nTest Case 4: Viewing Purchase History")
try:
    # Manually setting a purchase history for customer1
    customer1.setPurchaseHistory('Purchase History:\n1. VIP Ticket - 1500 AED\n2. Grand Prix Weekend Pass - 3000 AED')

    # Viewing the purchase history of customer1
    history = customer1.viewPurchaseHistory()

    # If a history exists, it is printed; otherwise, a message is displayed
    if history:
        print(history)
    else:
        print("No purchase history found.")

except Exception as e:
    # If there is an error during purchase history retrieval, it will be displayed here
    print(f"Error during viewing purchase history: {e}")

print("\nTest Case 5: Testing Integration with Event")
try:
    # Creating an Event object with event details
    event = Event("Formula 1", "Yas Marina Circuit", "2025-05-11", 5000, "Sports")

    # Displaying event details to confirm successful creation
    print(f"Event created successfully: {event.getName()} {event.getLocation()} {event.getDate()}")

    # Adding customer1 and customer2 to the event's user list
    event.addUser(customer1)
    event.addUser(customer2)

    # Displaying the list of users added to the event
    print(f"Customers added to event: {[user.getUsername() for user in event.getUserList()]}")

    # Removing customer1 from the event's user list
    event.removeUser(customer1)

    # Displaying the list of users after removal to confirm the change
    print(f"Customers after removal: {[user.getUsername() for user in event.getUserList()]}")

except Exception as e:
    # If there is an error during event integration, it will be displayed here
    print(f"Error during event integration: {e}")
