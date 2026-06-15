from rich.console import Console
from rich.table import Table

console = Console()


def display_users(users):

    table = Table(title="Gym Users")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Username")
    table.add_column("Role")

    for user in users:
        table.add_row(
            str(user.id),
            user.name,
            user.username,
            user.role
        )

    console.print(table)

def display_trainers(trainers):

    table = Table(title="Gym Trainers")

    table.add_column("Name")
    table.add_column("Specialty")
    table.add_column("Members Assigned")
    

    for trainer in trainers:
        table.add_row(
            trainer.name,
            trainer.specialty,
            str(len(trainer.members))
        )

    console.print(table)

def display_report(stats):

    table = Table(title="Gym Report")

    table.add_column("Metric")
    table.add_column("Count")

    for key, value in stats.items():
        table.add_row(
            key.capitalize(),
            str(value)
        )

    console.print(table)