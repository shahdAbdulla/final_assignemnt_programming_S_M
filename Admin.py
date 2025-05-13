# Import the User class to extend it for Admin
from User import User
from Event import Event


class Admin(User):
    def __init__(self, userID, username, email, password, contact_number, admin_level, department):
        """
        Constructor to initialize Admin attributes.
        It calls the User constructor and adds admin-specific attributes.
        """
        # Initialize the parent class (User)
        super().__init__(userID, username, email, password, contact_number)

        # Private attributes specific to Admin
        self.__admin_level = admin_level  # Admin access level (e.g., Manager, Supervisor)
        self.__department = department  # Admin department (e.g., Events, Security)

    # --- Setters and Getters ---
    def set_admin_level(self, level):
        """
        Sets the admin level for the Admin.
        """
        self.__admin_level = level

    def get_admin_level(self):
        """
        Gets the admin level of the Admin.
        """
        return self.__admin_level

    def set_department(self, department):
        """
        Sets the department of the Admin.
        """
        self.__department = department

    def get_department(self):
        """
        Gets the department of the Admin.
        """
        return self.__department

    # --- Methods ---

    def create_event(self, name, location, date, capacity, event_type):
        """
        Allows the admin to create a new event.
        :param name: Name of the event
        :param location: Location of the event
        :param date: Date of the event
        :param capacity: Maximum number of attendees
        :param event_type: Type of the event (e.g., Sports, Concert)
        :return: The created Event object
        """
        # Create a new Event object with the given details
        event = Event(name, location, date, capacity, event_type)

        # Display a confirmation message
        print(f"Event '{name}' created successfully.")

        # Return the created event object
        return event

    def modify_event(self, event, name=None, location=None, date=None, capacity=None, event_type=None):
        """
        Allows the admin to modify the details of an event.
        Only the provided parameters are updated; others are left unchanged.
        :param event: The Event object to be modified
        """
        # Update only if a new value is provided
        if name:
            event.setName(name)
        if location:
            event.setLocation(location)
        if date:
            event.setDate(date)
        if capacity:
            event.setTotalCapacity(capacity)
        if event_type:
            event.setEventType(event_type)

        # Display a confirmation message
        print(f"Event '{event.getName()}' has been modified successfully.")
        return True

    def generate_sales_report(self):
        """
        Generates a sales report. (Not yet implemented)
        """
        # Stub method for future implementation
        print("Generating sales report... (To be implemented)")

    def manage_users(self, user, action):
        """
        Manages user accounts by adding, removing, or updating users.
        :param user: The User object to be managed
        :param action: The action to be performed (add, remove, update)
        """
        if action == "add":
            print(f"User '{user.getUsername()}' added successfully.")
        elif action == "remove":
            print(f"User '{user.getUsername()}' removed successfully.")
        elif action == "update":
            print(f"User '{user.getUsername()}' updated successfully.")
        else:
            # Display error if the action is not valid
            print("Invalid action specified.")
