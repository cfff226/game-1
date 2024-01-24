# =====importing libraries===========
import os
from hashlib import sha256
from datetime import datetime, date
from pprint import pprint
import math
from collections import Counter
import sys

DATETIME_STRING_FORMAT = "%Y-%m-%d"

curr_date = date.today()

# If no user.txt file, write one with a default account
if not os.path.exists("user_details.txt"):
    with open("user_details.txt", "w") as default_file:
        default_file.write("admin;5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")

logged_in = False
username_password = {}
username_entered = False


# Function which registers a new user

def reg_user():
    username = input(
        "\n-----------------------------------------------------------------------\n\t\t\tPlease enter a new username or enter '-' to exit:\n"
    )
    if username == "-":
        exit()
    if " " in username:
        print(
            "\n-----------------------------------------------------------------------\n\t\t\tYour username must not contain any spaces\n"
        )
        reg_user()
    if ";" in username:
        print(
            "\n-----------------------------------------------------------------------\n\t\t\tYour username must not contain ';'\n"
        )
        reg_user()
    if len(username) < 8:
        print(
            "\n-----------------------------------------------------------------------\n\t\t\tYour username must be at least 8 characters long\n"
        )
        reg_user()

    while True:
        # Read in user_data
        try:
            with open("user_details.txt", "r") as user_file:
                user_data = user_file.read().split("\n")
                for i in user_data:
                    i = i.split(";")
                    username_password[i[0]] = i[1]
        except FileNotFoundError:
            print(
                "\n-----------------------------------------------------------------------\n\t\t\tSorry! This page is currently down for maintenance and will be up and running again soon!\n"
            )
            sys.exit()

        # There is an issue at the moment because if a user includes ; in their password, it creates an empty list item
        if username == i[0]:
            print(
                "\n-----------------------------------------------------------------------\nThis username is already taken, please choose a different one\n"
            )
            reg_user()
        else:
            # Request a password from the user
            while True:
                password = input(
                    "\n-----------------------------------------------------------------------\nPlease input a password: "
                )
                if len(password) < 8:
                    print(
                        "\n-----------------------------------------------------------------------\nYour username must be at least 8 characters long \n"
                    )
                    continue
                # Ask the user to confirm their password
                while True:
                    confirm_password = input(
                        "\n-----------------------------------------------------------------------\nPlease confirm your password: "
                    )
                    # If passwords match, append the username and password to the user.txt file
                    if password == confirm_password:
                        hashed_password = sha256(confirm_password.encode())
                        with open("user_details.txt", "a") as out_file:
                            out_file.write(
                                "".join(f"\n{username};{hashed_password.hexdigest()}")
                            )

                            print(
                                "\n-----------------------------------------------------------------------\nYour account has been created \n"
                            )
                            main()

                    # Output a message to show that passwords do not match and continue the loop
                    else:
                        print(
                            "\n-----------------------------------------------------------------------\nPasswords do not match \n"
                        )
                        continue

while not logged_in:
    # Read in user_data
    try:
        with open("user_details.txt", "r") as user_file:
            user_data = user_file.read().split("\n")
            for i in user_data:
                i = i.split(";")
                username_password[i[0]] = i[1]
    except FileNotFoundError:
        print(
            "\n-----------------------------------------------------------------------\n\t\t\tSorry! This page is currently down for maintenance and will be up and running again soon!\n"
        )

    login_username = input(
        "\n-----------------------------------------------------------------------\n\t\t\tPlease enter your username or enter '-' to register:\n"
    )

    if login_username == "-":
        reg_user()

    username_entered = True
    if login_username not in username_password:
        print(
            "\n-----------------------------------------------------------------------\n\t\t\tThere is no account associated with this username\n"
        )
        continue
    else:
        while username_entered == True:
            login_password = input(
                "\n-----------------------------------------------------------------------\n\t\t\tPlease enter your password:\n"
            )
            password_hash = sha256(login_password.encode("utf-8")).hexdigest()
            if username_password[login_username] != password_hash:
                print(
                    "\n-----------------------------------------------------------------------\n\t\t\tThis password is incorrect"
                )
                continue
            else:
                print(
                    "\n-----------------------------------------------------------------------\n\t\t\tYour login has been successful\n"
                )
            logged_in = True
            break





# Function to display the main menu

def main():
    print(
        "-----------------------------------------------------------------------\n\t\t\tWelcome to the Gaming System\n"
    )

    while True:
        # Display the menu

        
        print(
            "'r'. Register \n's'. Start a game\n'r'. Resume a game \n'v'. View leader board\n"
            )
        choice = input(
            "\n-----------------------------------------------------------------------\n\t\t\tPlease enter the revelent letter from the menu: \n"
        )

        if choice.lower() == "s":
            start_game()
        if choice.lower() == "r":
            resume_game()
        if choice.lower() == "v":
            view_leader_board()
        if choice.lower() == "e":
            print("Thanks for visiting the Gaming System")
            exit()


main()