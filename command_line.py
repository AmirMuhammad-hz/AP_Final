# Import the classes from the objects.py file
from Objects import User, Clinic, Doctor, Appointment, Notification, Admin

# Define a function to parse the command-line arguments using the argparse module
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="A command-line interface for an appointment system for clinics and doctors")
    # Add a positional argument for the role of the user (user or secretary)
    parser.add_argument("role", choices=["user", "secretary"], help="The role of the user")
    # Add an optional argument for the username of the user
    parser.add_argument("-u", "--username", type=str, help="The username of the user")
    # Add an optional argument for the password or the one-time password of the user
    parser.add_argument("-p", "--password", type=str, help="The password or the one-time password of the user")
    # Add an optional argument for the email of the user
    parser.add_argument("-e", "--email", type=str, help="The email of the user")
    # Add an optional argument for the action of the user (book, cancel, reschedule, view, increase, delete)
    parser.add_argument("-a", "--action", choices=["book", "cancel", "reschedule", "view", "increase", "delete"],
                        help="The action of the user")
    # Add an optional argument for the keyword of the doctor or clinic
    parser.add_argument("-k", "--keyword", type=str, help="The keyword of the doctor or clinic")
    # Add an optional argument for the id of the appointment
    parser.add_argument("-i", "--id", type=int, help="The id of the appointment")
    # Add an optional argument for the date and time of the appointment
    parser.add_argument("-d", "--date_time", type=str, help="The date and time of the appointment")
    # Add an optional argument for the capacity of the clinic
    parser.add_argument("-c", "--capacity", type=int, help="The capacity of the clinic")
    # Add an optional argument for the name of the clinic
    parser.add_argument("-n", "--name", type=str, help="The name of the clinic")
    # Add an optional argument for the address of the clinic
    parser.add_argument("-a", "--address", type=str, help="The address of the clinic")
    # Parse the arguments and return them
    parser.add_argument("-c", "--contact", type=str, help="The telephone of the clinic")
    args = parser.parse_args()
    return args


# Define a function to execute the command-line interface
def main():
    # Parse the command-line arguments
    args = parse_args()
    # Get the role of the user
    role = args.role
    # Get the username of the user
    address = args.address
    name = args.name
    contanct = args.contact
    username = args.username
    # Get the password or the one-time password of the user
    password = args.password
    # Get the email of the user
    email = args.email
    # Get the action of the user
    action = args.action
    # Get the keyword of the doctor or clinic
    keyword = args.keyword
    # Get the id of the appointment
    id = args.id
    # Get the date and time of the appointment
    date_time = args.date_time
    # Get the capacity of the clinic
    capacity = args.capacity
    # Check the role of the user
    if role == "user":
        # Create a user object with the username, password, and email
        user = User(username, password, email)
        # Sign in the user
        user.sign_in()
        # Check the action of the user
        if action == "book":
            # Search for the doctor or clinic with the keyword
            # This is a method of the user class that returns a list of possible matches
            results = user.search(keyword)
            # Print the results
            print(f"Here are the results for {keyword}:")
            for result in results:
                print(result)
            # Ask the user to choose one of the results
            choice = input("Please enter the id of the doctor or clinic you want to book an appointment with: ")
            # Get the doctor or clinic object with the choice
            # This is a method of the user class that returns a doctor or clinic object
            # Get the available slots for the doctor or clinic
            # This is a method of the user class that returns a list of available slots
            slots = user.get_slot()
            # Print the slots
            print(f"Here are the available slots")
            for slot in slots:
                print(slot)
            # Ask the user to choose one of the slots
            slot = input("Please enter the date and time of the slot you want to book: ")
            slot = slots[slot]
            # Create an appointment object with the user, doctor or clinic, and slot
            appointment = Appointment(clinic=slot['clinic'], user=user, doctor=slot['doct0or'],
                                      date_time=slot['datetime'], status=0)
            # Book the appointment
            appointment.book_appointment()

        elif action == "view":
            # Get the current appointments for the user
            # This is a method of the user class that returns a list of current appointments
            print(f"Here are your current appointments:")
            appointments = user.view_appointments()
        else:
            # Print an error message
            print(f"Invalid action: {action}")
        # Log out the user
        user.log_out()
    elif role == "secretary":
        # Create a clinic object with the name and address
        # This is a dummy object that represents the clinic that the secretary works for
        clinic = Clinic(name=name, address=address, contact=contanct)
        # Create a secretary object with the username, password, email, and clinic
        # This is a subclass of the admin class that inherits the attributes and methods of the admin class
        secretary = Admin(username, password, email, clinic)
        # Define a sign_in method for the secretary
        # This is a method that checks the username, password, and email of the secretary and signs them in
        # Sign in the secretary
        secretary.sign_in()
        # Check the action of the secretary
        if action == "increase":
            i = input('amount')
            # Increase the capacity of the clinic
            # This is a method of the admin class that makes a HTTP request to the API to change the capacity
            secretary.change_capacity(id, i)

        else:
            # Print an error message
            print(f"Invalid action: {action}")
        # Log out the secretary
        secretary.log_out()
    else:
        # Print an error message
        print(f"Invalid role: {role}")


# Execute the main function
if __name__ == "__main__":
    main()
