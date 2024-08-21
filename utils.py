from schedule import Schedule

def display_menu():
    print("------------------------------------------------------------")
    print("          Child Vaccination Management System")
    print("------------------------------------------------------------")
    print("1. Register a Child")
    print("2. View Vaccination Schedule")
    print("3. Book a Vaccination Appointment")
    print("4. View Upcoming Appointments")
    print("5. Update Child's Vaccination Record")
    print("6. View Vaccination Record")
    print("7. Exit")
    print("------------------------------------------------------------")

def select_child(children):
    if not children:
        print("No children registered yet.")
        return None

    print("Select your child's name:")
    for i, child in enumerate(children, start=1):
        print(f"{i}. {child.name}")
    
    try:
        index = int(input("Enter the number corresponding to your choice: ")) - 1
        if 0 <= index < len(children):
            return children[index]
        else:
            print("Invalid selection. Please choose a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def view_vaccination_schedule(children):
    child = select_child(children)
    if child:
        Schedule.view_schedule(child)

def view_upcoming_appointments(appointments):
    if not appointments:
        print("No appointments available.")
        return

    # Ensure appointments contain Appointment objects
    try:
        # Collect children from appointments
        children = [appointment.child for appointment in appointments if hasattr(appointment, 'child')]
        child = select_child(children)
        if child:
            upcoming_appointments = [appointment for appointment in appointments if appointment.child == child]
            if upcoming_appointments:
                print(f"Upcoming appointments for {child.name}:")
                for appointment in upcoming_appointments:
                    print(f"- {appointment.vaccination}: {appointment.date}")
            else:
                print(f"No upcoming appointments for {child.name}.")
    except AttributeError:
        print("Error: The appointments list may contain invalid objects or missing attributes.")

def view_vaccination_record(records):
    if not records:
        print("No vaccination records available.")
        return

    try:
        # Collect children from records
        children = [record.child for record in records if hasattr(record, 'child')]
        child = select_child(children)
        if child:
            vaccination_records = [record for record in records if record.child == child]
            if vaccination_records:
                print(f"Displaying vaccination record for {child.name}:")
                for record in vaccination_records:
                    print(f"- {record.vaccination}: {record.date}")
            else:
                print(f"No vaccination records found for {child.name}.")
    except AttributeError:
        print("Error: The records list may contain invalid objects or missing attributes.")
