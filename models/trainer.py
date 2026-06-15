# Import the base Person class from the local person module
from .person import Person


class Trainer(Person):
    """Represents a gym trainer, inheriting base attributes from Person."""

    def __init__(self, name, specialty, members=None):
        """Initialize a new Trainer instance."""
        # Call the parent class (Person) constructor to initialize the name
        super().__init__(name)

        # Set specific trainer attributes and initialize an empty client list
        self.specialty = specialty
        # members will be a list of usernames or User objects
        self.members = members if members else []

    def add_member(self, member):
        """Assign a new member to this trainer's list."""
        if member not in self.members:
            self.members.append(member)

    def view_members(self):
        for member in self.members:
            print(member.name)

    def to_dict(self):
        """Return a dictionary representation of the Trainer object."""
        return {
            "name": self.name,
            "specialty": self.specialty,
            "members": [m.username if hasattr(m, "username") else m for m in self.members]

       }        

    def remove_member(self, member):
        """Remove a member from the trainer's list if they exist in it."""
        if member in self.members:
            self.members.remove(member)

    def __str__(self):
        """Return a formatted string representation of the Trainer object."""
        return {
            "name": self.name,
            "specialty": self.specialty,
            "members": [m.username for m in self.trainer.members]
        
        }
            
        
