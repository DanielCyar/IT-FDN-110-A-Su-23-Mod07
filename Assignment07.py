# --------------------------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Creating a script that explains how pickling and exception handling works.
#              It reads and writes user data such as name and age of multiple users.
#
# ChangeLog (Who,When,What):
# DanielCastro,8.22.2023,Created starting script
# DanielCastro,8.23.2023,Added functions to write, read, get and display with error handling
# --------------------------------------------------------------------------------------------- #

import pickle

# DATA SECTION
user_data = None                # Empty storage variable
data_list = []                  # Empty List
file_name = 'UserData.dat'      # .dat File Name
# DATA SECTION


# PROCESS SECTION
class Process:

    @staticmethod
    def save_data(objFile, data_list):
        try:
            file = open(objFile, 'wb')
            pickle.dump(data_list, file)
            file.close()
            print("\nUser data saved successfully.")
        except IOError:
            print("ERROR: Could not save user data.")

    @staticmethod
    def load_data(objFile):
        try:
            file = open(objFile, 'rb')
            user_data = pickle.load(file)
            file.close()
            return user_data

        except FileNotFoundError:
            print("User data file not found.")
# PROCESS SECTION


# INPUT/OUTPUT SECTION
class IO:

    @staticmethod
    def get_input():

        try:
            name = input("\nEnter user's name (or type 'exit' to finish): ")

            if name.lower() == 'exit':
                input("\n[Press enter to Exit...]")
                exit()
            age = input("Enter user's age: ")

            if name.isnumeric():
                raise Exception("\nERROR: Name should be a string.")            # Structured Error Handling
            elif not age.isnumeric():
                raise ValueError("\nERROR: Age should be an integer.")
            else:
                return {"name": name, "age": age}

        except Exception as e:                                                  # Exception handling
            print(e)
        except ValueError as a:
            print(a)

    @staticmethod
    def display_data(data_list):
        print("\nLoaded user data:")
        for row in data_list:
            print(f"[Name: {row['name']}, Age: {row['age']}]")
# INPUT/OUTPUT SECTION


# MAIN BODY OF THE SCRIPT
while True:

    user_data = IO.get_input()
    if user_data is None:
        break
    data_list.append(user_data)
    Process.save_data(file_name, data_list)
    loaded_users = Process.load_data(file_name)
    IO.display_data(loaded_users)
