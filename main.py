import argparse
import json
from gym import Gym
from models.user import User
from models.trainer import Trainer   
from utils.display import (
    display_users,
    display_trainers,
    display_report
)

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

    assign_trainer = subparsers.add_parser(
        "assign-trainer"
    )

    assign_trainer.add_argument(
        "--username",
        required=True
    )

    assign_trainer.add_argument(
        "--trainer",
        required=True
    )
    # report
    subparsers.add_parser("report")
    
        # delete-user
    delete_user = subparsers.add_parser(
        "delete-user"
    )

    delete_user.add_argument(
        "--username",
        required=True
    )

    # delete-trainer
    delete_trainer = subparsers.add_parser(
        "delete-trainer"
    )

    delete_trainer.add_argument(
        "--name",
        required=True
    )

    # Parse args
    args = parser.parse_args()

    # Handle commands
    try:
        # Route to user creation logic
        if args.command == "add-user":
            # Instantiate a new User object with parsed arguments
            user = User(
                args.name,
                args.username,
                args.password,
                args.role
            )

            # Append the user to the gym registry and write to the JSON file
            gym.add_user(
                user,
                "data/users.json"
            )

            print("User added successfully!")

        # Route to user listing logic
        elif args.command == "list-users":

            # Check if the registry is currently empty
            if not gym.users:
                print("No users found.")
            else:
                # Render the list of existing users to the console
                display_users(gym.users)

        # Route to user authentication logic
        elif args.command == "login":

            # Verify credentials against registered gym users
            user = gym.authenticate(
                args.username,
                args.password
            )

            # Check if authentication was successful
            if user:
                print(
                    f"Welcome {user.name} ({user.role})"
                )
            else:
                print("Invalid credentials")

        # Route to manual state persistence
        elif args.command == "save":

            # Backup current in-memory user registry to disk
            gym.save_users(
                "data/users.json"
            )

            print("Data saved successfully!")

        elif args.command == "delete-user":

            if gym.delete_user(
                args.username,
                "data/users.json"
            ):
                print(
                    "User deleted successfully!"
                )

            else:
                print(
                    "User not found."
                )

            

        # Route to trainer creation logic
        elif args.command == "add-trainer":

            # Instantiate a new Trainer object with parsed arguments
            trainer = Trainer(
                args.name,
                args.specialty
            )

            # Append the trainer to the gym registry and write to the JSON file
            gym.add_trainer(
                trainer,
                "data/trainers.json"
            )

            print(
                f"Trainer {trainer.name} added successfully!"
            )
        elif args.command == "assign-trainer":

            gym.assign_member_to_trainer(
                args.username,
                args.trainer
            )

            gym.save_trainers(
                "data/trainers.json"
            )

            print(
                f"{args.username} assigned to {args.trainer}"
            )

        # Route to trainer listing logic
        elif args.command == "list-trainers":

            # Check if the trainer registry is currently empty
            if not gym.trainers:
                print("No trainers found.")
            else:
                # Render the list of existing trainers to the console
                display_trainers(
                    gym.trainers
                )

        elif args.command == "delete-trainer":

            if gym.delete_trainer(
                args.name,
                "data/trainers.json"
            ):
                print(
                    "Trainer deleted successfully!"
                )

            else:
                print(
                    "Trainer not found."
                )

        # Route to administrative report generation
        elif args.command == "report":

            # Compile data and output gym user metrics
            display_report(
                gym.user_statistics()
            )

        # Handle unrecognised input subcommands
        else:
            print(
                "Invalid command. Use --help"
            )

    # Intercept data validation or runtime errors safely
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
