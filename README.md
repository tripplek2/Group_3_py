## Gym Management CLI System
# Overview

The Gym Management CLI System is a Python-based command-line application designed to help manage gym operations efficiently. The system allows administrators to manage users and trainers, authenticate users, assign members to trainers, generate reports, and store data persistently using JSON files.

This project demonstrates the use of Object-Oriented Programming (OOP), file handling, data persistence, and command-line interfaces in Python.

# Features
1.Add new users
2.List all registered users
3.User authentication (login)
4.Add trainers
5.List trainers
6.Assign members to trainers
7.Delete users
8.Delete trainers
9.Generate gym reports
10.Save and load data using JSON files
11.Rich CLI tables for improved user experience
12.Error handling and input validation

# Technologies Used
1.Python 3
2.Argparse
3.Rich
4.JSON
5.Object-Oriented Programming (OOP)

# Project Structure
Group_py/
│
├── main.py
├── gym.py
│
├── models/
│   ├── person.py
│   ├── user.py
│   └── trainer.py
│
├── utils/
│   └── display.py
│
├── data/
│   ├── users.json
│   └── trainers.json
│
└── README.md

# Installation
1.Clone the Repository
git clone <repository-url>
2.cd Group_py
Create a Virtual Environment
3.python3 -m venv venv
Activate the Virtual Environment

Linux/Mac:source venv/bin/activate

Windows:venv\Scripts\activate

# Install Dependencies
-pip install rich

-Running the Application
-Display Help
-python3 main.py --help
# Usage Example
-Add a User
python3 main.py add-user \
    --name Kelvin \
    --username kelvin123 \
    --password 1234 \
    --role member

# Generate a Report
-python3 main.py report
-Data Persistence


# OOP Concepts Demonstrated
1.Inheritance
User inherits from Person
Trainer inherits from Person
2.Encapsulation
Property getters and setters are used for validation.
User attributes are protected through controlled access.
3.Abstraction
The Gym class hides the complexity of managing users and trainers.
4.Polymorphism
Shared behavior through inherited methods such as __str__().

# Challenges Encountered
1.Managing data persistence with JSON.
2.Preventing duplicate users and trainers.
3.Validating user input.
4.Maintaining unique user IDs.
5.Designing a clean command-line interface.
6.Handling exceptions gracefully.

# Future Improvements
1.Membership plans and subscriptions.
2.Workout tracking.
3.Attendance management.
4.Payment processing.
5.Trainer performance reports.
6.Database integration using SQLite or PostgreSQL.
7.Role-based permissions and dashboards.

# Authors

1.Kelvin Korir
2.Shayne Wanjiru
3.Ethan Paul
4.Sam Wanjohi

Python CLI Gym Management System Project

# License

This project is for educational purposes and learning Object-Oriented Programming in Python.

# Loom recording
https://www.loom.com/share/ab8ad0a2eefb4e3c843d13c17cffe7c5