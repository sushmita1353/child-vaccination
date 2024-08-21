class Schedule:
    # Define the vaccination schedule in a dictionary
    vaccination_schedules = {
        'BCG': {'Age': 'At birth'},
        'Polio': {'Age': 'At 6 weeks, 10 weeks, 14 weeks'},
        'DPT': {'Age': 'At 6 weeks, 10 weeks, 14 weeks'},
        'MMR': {'Age': 'At 12 months'},
        'Hepatitis B': {'Age': 'At birth, 1-2 months, 6-18 months'},
        'Hib': {'Age': 'At 2 months, 4 months, 6 months, 12-15 months'},
        'Varicella': {'Age': 'At 12-15 months'},
        'Influenza': {'Age': 'Annually starting at 6 months'}
    }

    @staticmethod
    def view_schedule(child):
        """
        Display the vaccination schedule for a given child.
        """
        print(f"Displaying vaccination schedule for {child.name}:")
        for vaccine, schedule in Schedule.vaccination_schedules.items():
            print(f"- {vaccine}: {schedule['Age']}")

    @staticmethod
    def next_due_vaccination(child_age_months):
        """
        Determine the next due vaccination based on the child's age.
        """
        # Age thresholds in months for various vaccinations
        vaccine_due_dates = {
            'BCG': 0,
            'Polio': [6, 10, 14],
            'DPT': [6, 10, 14],
            'MMR': 12,
            'Hepatitis B': [0, 2, 18],
            'Hib': [2, 4, 6, 15],
            'Varicella': 15,
            'Influenza': None  # Annual vaccination
        }
        
        next_due = []
        for vaccine, due_dates in vaccine_due_dates.items():
            if due_dates is None:
                next_due.append(vaccine)  # Annual vaccines
            elif isinstance(due_dates, list):
                for date in due_dates:
                    if child_age_months < date:
                        next_due.append(f"{vaccine} due at {date} months")
                        break
            elif child_age_months < due_dates:
                next_due.append(f"{vaccine} due at {due_dates} months")
        
        if next_due:
            print(f"Next due vaccinations for {child_age_months}-month-old child:")
            for due in next_due:
                print(f"- {due}")
        else:
            print("No upcoming vaccinations due based on the current age.")

# Example usage
class Child:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

# Test the Schedule class
child = Child("John Doe", "2022-08-01")
Schedule.view_schedule(child)
Schedule.next_due_vaccination(7)  # 7 months old child
