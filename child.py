class Child:
    def __init__(self, name, dob, parent_name, contact):
        self.name = name
        self.dob = dob
        self.parent_name = parent_name
        self.contact = contact

    @staticmethod
    def register_child():
        name = input("Enter Child's Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        parent_name = input("Enter Parent/Guardian Name: ")
        contact = input("Enter Contact Number: ")
        print("Child registered successfully!")
        return Child(name, dob, parent_name, contact)