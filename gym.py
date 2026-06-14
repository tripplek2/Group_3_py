import json
from models.user import User


class Gym:
    """Manages a collection of gym users and handles data persistence."""

    def __init__(self):
        """Initializes an empty list to store User and trainer objects."""
        self.users = []
        self.trainers = []

    def add_user(self, user):
        """Adds a new User object to the gym system."""
        self.users.append(user)

    def list_users(self):
        """Iterates through and prints all registered users."""
        if not self.users:
            print("No users found.")
            return
        for user in self.users:
            print(user)

    def save_users(self, filename):
        """Serializes and saves the current user list to a JSON file."""
        data = []

        # Convert each User object into a dictionary format
        for user in self.users:
            data.append({
                "name": user.name,
                "username": user.username,
                "password": user.password,
                "role": user.role
            })

        # Write the serialized dictionary list to the specified file
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return user
        return None

    @classmethod
    def load_users(cls, filename):
        """Loads user data from a JSON file and returns a new Gym instance."""
        gym = cls()

        try:
            # Open and read the JSON file contents
            with open(filename, "r") as file:
                data = json.load(file)

                # Reconstruct User objects and add them to the new gym instance
                for user_data in data:
                    user = User(
                        name=user_data["name"],
                        username=user_data["username"],
                        password=user_data["password"],
                        role=user_data["role"]
                    )
                    gym.add_user(user)

        # Silently ignore the error if the target file does not exist yet
        except FileNotFoundError:
            pass

        return gym