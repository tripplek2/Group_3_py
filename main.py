import argparse
from gym import gym
from models.user import User 

#load system
gym = gym.load_users("data/users.json")

#create CLI pack
parser = argparse.ArgumentParser(
    description="Gym Management CLI System"
)

subparsers = parser.add_subparsers(dest="command")

#add user command
add_user = subparsers.add_parser("add-user")

add_user.add_argument("--name", required=True)
add_user.add_argument("--username", required=True)
add_user.add_argument("--password", required=True)
add_user.add_argument("--role", required=True)
#list users
subparsers.add_parser("list-users")

#login command
login = subparsers.add_parser("login")

login.add_argument("--username", required=True)
login.add_argument("--password", required=True)

#save command
subparsers.add_parser("save")
#parse arguements
args = parser.parse_args()

#add user
if args.command == "add-user":

    user = User(
        args.name,
        args.username,
        args.password,
        args.role
    )

    gym.add_user(user)

    print("User added successfully!")


#list users
elif args.command == "list-users":

    gym.list_users()

#login authentification
elif args.command == "login":

    user = gym.authenticate(
        args.username,
        args.password
    )

    if user:
        print(f"Welcome {user.name} ({user.role})")
    else:
        print("Invalid credentials")

#save data
elif args.command == "save":

    gym.save_users("data/users.json")

    print("Data saved successfully!")

else:
    print("Invalid command. Use --help")

def main():
    args = parser.parse_args()
    ...
    
if __name__ == "__main__":
    main()



