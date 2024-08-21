import utils  # Import the utils module

class Record:
    def __init__(self, child, vaccination, date):
        self.child = child
        self.vaccination = vaccination
        self.date = date

    @staticmethod
    def update_vaccination_record(children):
        child = utils.select_child(children)
        if child:
            vaccination = input("Enter Vaccination Name: ")
            date = input("Enter Date of Vaccination (YYYY-MM-DD): ")
            print("Vaccination record updated successfully!")
            return Record(child, vaccination, date)
        else:
            print("No child selected. Record not updated.")
            return None
