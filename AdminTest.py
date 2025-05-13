# AdminTest.py
# This script tests the functionality of the Admin class,
# including creating admin accounts, managing events, generating reports, and managing users.

# Import necessary classes
from Admin import Admin
from User import User

print("\nTest Case 1: Creating Admin Object")
try:
    # Creating an Admin object with admin-specific details
    admin1 = Admin("A001", "admin_user", "admin@gmail.com", "adminpass", "0501234567", "SuperAdmin", "Events")

    # Displaying the admin details to confirm successful creation
    print(
        f"Admin created successfully: {admin1.getUserID()} {admin1.getUsername()} {admin1.getEmail()} {admin1.getContactNumber()} {admin1.get_admin_level()} {admin1.get_department()}")

except Exception as e:
    # If there is an error during admin creation, it will be displayed here
    print(f"Error during admin creation: {e}")

print("\nTest Case 2: Testing Getters and Setters")
try:
    # Displaying the initial values for admin's level and department
    print(f"Admin Level: {admin1.get_admin_level()}")
    print(f"Department: {admin1.get_department()}")

    # Updating the admin level and department using setters
    admin1.set_admin_level("Manager")
    admin1.set_department("Marketing")

    # Displaying the updated values to confirm the changes
    print("\nAfter Updates")
    print(f"Updated Admin Level: {admin1.get_admin_level()}")
    print(f"Updated Department: {admin1.get_department()}")

except Exception as e:
    # If there is an error during getter or setter tests, it will be displayed here
    print(f"Error during getter and setter testing: {e}")

print("\nTest Case 3: Creating an Event")
try:
    # The admin creates a new event with specific details
    event1 = admin1.create_event("Formula 1 Grand Prix", "Yas Marina Circuit", "2025-11-20", 5000, "Sports")

    # Displaying the event details to confirm successful creation
    print(
        f"Event Created: {event1.getName()} at {event1.getLocation()} on {event1.getDate()} with capacity {event1.getTotalCapacity()}")

except Exception as e:
    # If there is an error during event creation, it will be displayed here
    print(f"Error during event creation: {e}")

print("\nTest Case 4: Modifying an Event")
try:
    # The admin modifies the existing event with new details
    admin1.modify_event(event1, name="Formula 1 Abu Dhabi", location="Yas Island", capacity=6000)

    # Displaying the modified event details to confirm changes
    print(f"Modified Event: {event1.getName()} at {event1.getLocation()} with capacity {event1.getTotalCapacity()}")

except Exception as e:
    # If there is an error during event modification, it will be displayed here
    print(f"Error during event modification: {e}")

print("\nTest Case 5: Generating Sales Report (Stub)")
try:
    # The admin attempts to generate a sales report (currently a placeholder method)
    admin1.generate_sales_report()

except Exception as e:
    # If there is an error during report generation, it will be displayed here
    print(f"Error during sales report generation: {e}")

print("\nTest Case 6: Managing Users (Add, Remove, Update)")
try:
    # Creating a user to be managed by the admin
    user1 = User("U001", "user_maha", "maha@gmail.com", "pass123", "0501234567")

    # Admin adds the user to the system
    admin1.manage_users(user1, "add")

    # Admin updates the user details
    admin1.manage_users(user1, "update")

    # Admin removes the user from the system
    admin1.manage_users(user1, "remove")

except Exception as e:
    # If there is an error during user management, it will be displayed here
    print(f"Error during user management: {e}")
