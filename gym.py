import json
import os
from models.user import User
from models.trainer import Trainer

class Gym:
    """Manages a collection of gym users and trainers, with data persistence."""

    def __init__(self):
        self.users = []
        self.trainers = []

    # --- USERS ---
    def add_user(self, user, filename="users.json"):
        if self.find_user(user.username):
            raise ValueError("Username already exists.")
        self.users.append(user)
        self.save_users(filename)

    def save_users(self, filename="users.json"):
        with open(filename, "w") as file:
            json.dump([u.to_dict() for u in self.users], file, indent=4)

    @classmethod
    def load_users(cls, filename="users.json"):
        gym = cls()
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return gym
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                gym.users = [User(**u) for u in data]
        except FileNotFoundError:
            pass
        return gym

    def list_users(self):
        return self.users

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
        stats = {"members": 0, "trainers": 0, "admins": 0}
        for user in self.users:
            if user.role == "member":
                stats["members"] += 1
            elif user.role == "trainer":
                stats["trainers"] += 1
            elif user.role == "admin":
                stats["admins"] += 1
        return stats

    # --- TRAINERS ---
    def add_trainer(self, trainer, filename="trainers.json"):
        self.trainers.append(trainer)
        self.save_trainers(filename)

    def save_trainers(self, filename="trainers.json"):
        with open(filename, "w") as file:
            json.dump([t.to_dict() for t in self.trainers], file, indent=4)

    @classmethod
    def load_trainers(cls, filename="trainers.json"):
        gym = cls()
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return gym
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                gym.trainers = [Trainer(**t) for t in data]
        except FileNotFoundError:
            pass
        return gym

    def list_trainers(self):
        return self.trainers

    def find_trainer(self, name):
        for trainer in self.trainers:
            if trainer.name.lower() == name.lower():
                return trainer
        return None

    def assign_member_to_trainer(self, username, trainer_name):
        user = self.find_user(username)
        trainer = self.find_trainer(trainer_name)
        if not user:
            raise ValueError("User not found.")
        if not trainer:
            raise ValueError("Trainer not found.")
        trainer.add_member(user)
