import argparse
import json
from rich.table import Table
from rich.console import Console
from gym import Gym
from models.user import User
from models.trainer import Trainer   

def main():
    # Load users at startup
    gym = Gym.load_users("data/users.json")
    trainers_gym = Gym.load_trainers("data/trainers.json")
    gym.trainers = trainers_gym.trainers

    # CLI parser
    parser = argparse.ArgumentParser(description="Gym Management CLI System")
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--username", required=True)
    add_user.add_argument("--password", required=True)
    add_user.add_argument("--role", required=True)

    # list-users
    subparsers.add_parser("list-users")

    # login
    login = subparsers.add_parser("login")
    login.add_argument("--username", required=True)
    login.add_argument("--password", required=True)

    # save
    subparsers.add_parser("save")

    # add-trainer
    add_trainer = subparsers.add_parser("add-trainer")
    add_trainer.add_argument("--name", required=True)
    add_trainer.add_argument("--specialty", required=True)

    # list-trainers
    subparsers.add_parser("list-trainers")

    # report
    subparsers.add_parser("report")

    # Parse args
    args = parser.parse_args()

    # Handle commands
    if args.command == "add-user":
        user = User(args.name, args.username, args.password, args.role)
        gym.add_user(user, "data/users.json")
        print("User added successfully!")

    elif args.command == "list-users":
        if not gym.users:
            print("No users found.")
        else:
            table = Table(title="Gym Users")
            table.add_column("Name")
            table.add_column("Username")
            table.add_column("Role")
            for user in gym.users:
                table.add_row(user.name, user.username, user.role)
            console = Console()
            console.print(table)

    elif args.command == "login":
        user = gym.authenticate(args.username, args.password)
        if user:
            print(f"Welcome {user.name} ({user.role})")
        else:
            print("Invalid credentials")

    elif args.command == "save":
        gym.save_users("data/users.json")
        print("Data saved successfully!")

    elif args.command == "add-trainer":
        trainer = Trainer(args.name, args.specialty)
        gym.add_trainer(trainer)
        with open("data/trainers.json", "w") as f:
            json.dump([t.to_dict() for t in gym.trainers], f, indent=4)
        print(f"Trainer {trainer.name} added successfully!")

    elif args.command == "list-trainers":
        if not gym.trainers:
            print("No trainers found.")
        else:
            table = Table(title="Gym Trainers")
            table.add_column("Name")
            table.add_column("Specialty")
            table.add_column("Members Assigned")
            for trainer in gym.trainers:
                table.add_row(trainer.name, trainer.specialty, str(len(trainer.members)))
            console = Console()
            console.print(table)

    elif args.command == "report":
        stats = gym.user_statistics()
        table = Table(title="User Statistics")
        table.add_column("Role")
        table.add_column("Count")
        for role, count in stats.items():
            table.add_row(role, str(count))
        console = Console()
        console.print(table)

    else:
        print("Invalid command. Use --help")

if __name__ == "__main__":
    main()


