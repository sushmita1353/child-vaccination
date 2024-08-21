from child import Child
from appointment import Appointment
from schedule import Schedule
from record import Record
import utils

def main():
    children = []
    appointments = []
    records = []

    while True:
        utils.display_menu()
        choice = input("Please select an option: ")

        if choice == '1':
            children.append(Child.register_child())
        elif choice == '2':
            utils.view_vaccination_schedule(children)
        elif choice == '3':
            appointments.append(Appointment.book_appointment(children))
        elif choice == '4':
            utils.view_upcoming_appointments(appointments)
        elif choice == '5':
            records.append(Record.update_vaccination_record(children))
        elif choice == '6':
            utils.view_vaccination_record(records)
        elif choice == '7':
            print("Thank you for using the Child Vaccination Management System. Stay safe!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
