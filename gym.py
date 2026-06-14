import json
from models.user import User
import os


class Gym:
    """Manages a collection of gym users and handles data persistence."""

    def __init__(self):
        """Initializes an empty list to store User and trainer objects."""
        self.users = []
        self.trainers = []

    def add_user(self, user, filename="users.json"):

        if self.find_user(user.username):
            raise ValueError("Username already exists.")
        self.users.append(user)
        self.save_users(filename)
        

    def load_users(self, filename="users.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.users = [User(**u) for u in data]
        except FileNotFoundError:
            self.users = []


    def list_users(self):
        """Iterates through and prints all registered users."""
        if not self.users:
            print("No users found.")
            return []
        for user in self.users:
            print(user)
        return self.users
            

    def save_users(self, filename):
        with open(filename, "w") as file:
            json.dump(
            [user.to_dict() for user in self.users],
            file,
            indent=4
            )
    
    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def delete_user(self, username):

        user = self.find_user(username)

        if user:
            self.users.remove(user)
            return True

        return False

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return user
        return None
    
    def user_statistics(self):

        stats = {
        "members": 0,
        "trainers": 0,
        "admins": 0
        }

        for user in self.users:

            if user.role == "member":
                stats["members"] += 1

            elif user.role == "trainer":
                stats["trainers"] += 1

            elif user.role == "admin":
                stats["admins"] += 1

        return stats
    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def list_trainers(self):
        return self.trainers
    
    def find_trainer(self, name):

        for trainer in self.trainers:

            if trainer.name.lower() == name.lower():
                return trainer

        return None
    

    def assign_member_to_trainer(
        self,
        username,
        trainer_name
    ):

        user = self.find_user(username)

        trainer = self.find_trainer(
            trainer_name
        )

        if not user:
            raise ValueError("User not found.")

        if not trainer:
            raise ValueError("Trainer not found.")

        trainer.add_member(user)

    @classmethod
    def load_users(cls, filename):
        """Loads user data from a JSON file and returns a new Gym instance."""
        gym = cls()

             # Return empty instance if file does not exist or has no content
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return gym

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