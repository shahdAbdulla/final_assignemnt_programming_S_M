class User:
    def __init__(self, userID, username, email, password, contactNumber):
        """
        Constructor to initialize the User attributes.
        """
        # Protected attributes for User details
        self._userID = userID  # Unique ID for the user (e.g., U001)
        self._username = username  # Username for login (e.g., maha)
        self._email = email  # User's email address (e.g., maha@gmail.com)
        self._password = password  # User's password (e.g., pass123)
        self._contactNumber = contactNumber  # User's contact number (e.g., 0501234567)

    # --- Getters and Setters ---

    # Get and Set for userID
    def getUserID(self):
        """
        Returns the User ID.
        """
        return self._userID

    def setUserID(self, userID):
        """
        Sets the User ID.
        """
        self._userID = userID

    # Get and Set for username
    def getUsername(self):
        """
        Returns the Username.
        """
        return self._username

    def setUsername(self, username):
        """
        Sets the Username.
        """
        self._username = username

    # Get and Set for email
    def getEmail(self):
        """
        Returns the User's Email.
        """
        return self._email

    def setEmail(self, email):
        """
        Sets the User's Email.
        """
        self._email = email

    # Get and Set for password
    def getPassword(self):
        """
        Returns the User's Password.
        """
        return self._password

    def setPassword(self, password):
        """
        Sets the User's Password.
        """
        self._password = password

    # Get and Set for contact number
    def getContactNumber(self):
        """
        Returns the User's Contact Number.
        """
        return self._contactNumber

    def setContactNumber(self, contactNumber):
        """
        Sets the User's Contact Number.
        """
        self._contactNumber = contactNumber

    # --- Methods for User Actions ---

    def login(self):
        """
        Simulates a login action.
        Returns True if login is successful.
        """
        try:
            # Basic check to simulate login, can be extended with actual logic
            if self._username and self._password:
                print(f"{self._username} logged in successfully.")
                return True
            else:
                print("Login failed. Username or password missing.")
                return False
        except Exception as e:
            # If there is an error during login, display the error
            print(f"Login error: {e}")
            return False

    def logout(self):
        """
        Simulates a logout action.
        """
        try:
            # Display a message indicating successful logout
            print(f"{self._username} has been logged out.")
        except Exception as e:
            # If there is an error during logout, display the error
            print(f"Logout error: {e}")
