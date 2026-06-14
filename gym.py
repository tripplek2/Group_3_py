import json
from models.user import User


class Gym:
    """Manages a collection of gym users and handles data persistence."""

    def __init__(self):
        """Initializes an empty list to store User objects."""
        self.users = []

    def add_user(self, user):
        """Adds a new User object to the gym system."""
        self.users.append(user)

    def list_users(self):
        """Iterates through and prints all registered users."""
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
                        user_data["name"],
                        user_data["username"],
                        user_data["password"],
                        user_data["role"]
                    )
                    gym.add_user(user)

        # Silently ignore the error if the target file does not exist yet
        except FileNotFoundError:
            pass

        return gym