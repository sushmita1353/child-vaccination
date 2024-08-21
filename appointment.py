# Import the utils module
import utils

class Appointment:
    @staticmethod
    def book_appointment(children):
        child = utils.select_child(children)
        if child:
            # Continue with the appointment booking logic
            print(f"Booking appointment for {child.name}")
            # For example, you could add the appointment to a list here
            return child  # Example return, adjust as needed
        return None