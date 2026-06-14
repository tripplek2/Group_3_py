import argparse
from rich.table import Table
from rich.console import Console
from gym import Gym
from models.user import User

def main():
    # Always load users from disk at startup
    gym = Gym.load_users("data/users.json")

    # Create CLI parser
    parser = argparse.ArgumentParser(description="Gym Management CLI System")
    subparsers = parser.add_subparsers(dest="command")

    # add-user command
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--username", required=True)
    add_user.add_argument("--password", required=True)
    add_user.add_argument("--role", required=True)

    # list-users command
    subparsers.add_parser("list-users")

    # login command
    login = subparsers.add_parser("login")
    login.add_argument("--username", required=True)
    login.add_argument("--password", required=True)

    # save command
    subparsers.add_parser("save")

    # Parse arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "add-user":
        user = User(args.name, args.username, args.password, args.role)
        gym.add_user(user, "data/users.json")   # save immediately
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

    else:
        print("Invalid command. Use --help")

if __name__ == "__main__":
    main()



