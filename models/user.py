# Import the base Person class from the local person module
from .person import Person


class User(Person):
    """Represents a system user, inheriting base attributes from Person."""

    # Class variable to automatically generate unique, sequential IDs
    id_counter = 1

    def __init__(self, name, username, password, role, id=None):
        """Initialize a new User instance."""
        # Call the parent class (Person) constructor to initialize the name
        super().__init__(name)

        # If id is provided (from JSON), use it; otherwise generate a new one
        if id is not None:
            self.id = id

        # Assign a unique ID and increment the class counter for the next user
        else:
            self.id = User.id_counter
            User.id_counter += 1

        # Set user attributes (username triggers the setter validation)
        self.username = username
        self.role = role
        self.password = password

    @property
    def username(self):
        """Getter for the username property."""
        return self._username

    @username.setter
    def username(self, value):
        """Setter for username that enforces a minimum length of 5 characters."""
        if len(value) < 5:
            raise ValueError("Username too short")

        # Store the validated value in a protected attribute
        self._username = value

    @property
    def password(self):
       """Getter for password property"""
       return self._password

    @password.setter
    def password(self, value):
        if len(value) < 4:
            raise ValueError(
            "Password must be at least 4 characters long."
            )

        self._password = value

    @property
    def role(self):
        """Getter for role property"""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property with validation"""
        allowed_roles = ["user", "trainer", "member"]
        if value.lower() not in allowed_roles:
            raise ValueError("Invalid role.")
        self._role = value.lower()    


    def check_password(self, password):
        return self.password == password

    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "username": self.username,
        "password": self.password,
        "role": self.role
        }    

    

    def __str__(self):
        """Return a formatted string representation of the User object."""
        return (
            f"ID: {self.id} | "
            f"{self.name} | "
            f"{self.role}"
        )