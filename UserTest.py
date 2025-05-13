# MasterTest_User.py
# This script tests the functionality of the User class,
# including creating users, managing their details, login/logout operations,
# and integration with the Event class.

# Import necessary classes
from User import User
from Event import Event

# Test Case 1: Creating User Objects
print("\nTest Case 1: Creating User Objects")
try:
    # Creating two User objects with initial details:
    # userID, username, email, password, contact number
    user1 = User("U001", "maha", "maha@gmail.com", "pass123", "0501234567")
    user2 = User("U002", "hamdan", "hamdan@gmail.com", "pass456", "0507654321")

    # Displaying user details to confirm successful creation
    print("User 1 created successfully:", user1.getUserID(), user1.getUsername(), user1.getEmail(),
          user1.getContactNumber())
    print("User 2 created successfully:", user2.getUserID(), user2.getUsername(), user2.getEmail(),
          user2.getContactNumber())

except Exception as e:
    # If there is any error during user creation, it gets printed here
    print("Error during user creation:", e)

# Test Case 2: Testing Getters and Setters
print("\nTest Case 2: Testing Getters and Setters")
try:
    # --- Testing Getters ---
    # Get and print the original details of user1
    print("User 1 ID:", user1.getUserID())  # Display user ID
    print("User 1 Username:", user1.getUsername())  # Display username
    print("User 1 Email:", user1.getEmail())  # Display email
    print("User 1 Password:", user1.getPassword())  # Display password
    print("User 1 Contact Number:", user1.getContactNumber())  # Display contact number

    # --- Testing Setters ---
    # Update user1's details using the setter methods
    user1.setUserID("U003")
    user1.setUsername("maha_updated")
    user1.setEmail("maha_updated@gmail.com")
    user1.setPassword("newpass123")
    user1.setContactNumber("0509999999")

    # Displaying updated values to confirm setters worked
    print("\nAfter Updates")
    print("Updated User 1 ID:", user1.getUserID())  # Updated user ID
    print("Updated User 1 Username:", user1.getUsername())  # Updated username
    print("Updated User 1 Email:", user1.getEmail())  # Updated email
    print("Updated User 1 Password:", user1.getPassword())  # Updated password
    print("Updated User 1 Contact Number:", user1.getContactNumber())  # Updated contact number

except Exception as e:
    # If there is any error during getter or setter tests, it gets printed here
    print("Error during getters/setters test:", e)

# Test Case 3: Testing Login and Logout
print("\nTest Case 3: Testing Login and Logout")
try:
    # Attempting to log in as user1
    print("Trying to log in as:", user1.getUsername())
    login_status = user1.login()  # Calls the login method
    print("Login Status:", login_status)  # Should display True if successful

    # Attempting to log out the user
    print("Trying to log out:")
    user1.logout()  # Calls the logout method, prints a confirmation

    # Testing a failed login scenario
    user1.setUsername("")  # Setting the username to an empty string
    login_fail_status = user1.login()  # Trying to log in without a username
    print("Login with empty username:", login_fail_status)  # Should display False

    # Restore the original username for further tests
    user1.setUsername("maha_updated")

except Exception as e:
    # If there is any error during login/logout, it gets printed here
    print("Error during login/logout test:", e)

# Test Case 4: Integrating with Event
print("\nTest Case 4: Integrating with Event")
try:
    # Creating an Event object with details:
    # name, location, date, capacity, and type
    event1 = Event("Formula 1", "Yas Marina Circuit", "2025-05-11", 5000, "Sports")

    # Display event details to confirm it was created successfully
    print("Event created successfully:", event1.getName(), event1.getLocation(), event1.getDate())

    # Adding the users (user1 and user2) to the event's attendee list
    event1.addUser(user1)
    event1.addUser(user2)

    # Displaying the list of users currently registered for the event
    print("Users added to event:", [user.getUsername() for user in event1.getUserList()])

    # Removing user1 from the event's attendee list
    event1.removeUser(user1)

    # Displaying the list of users after removal to confirm it worked
    print("Users after removal:", [user.getUsername() for user in event1.getUserList()])

except Exception as e:
    # If there is any error during event integration, it gets printed here
    print("Error during event integration test:", e)
