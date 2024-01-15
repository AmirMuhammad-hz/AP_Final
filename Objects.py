class User:
    def __init__(self, id, name, email, password, user_type):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type

    def register(self):
        pass

    def login(self):
        pass

    def update_profile(self):
        pass

    def view_appointments(self):
        pass


class Clinic:
    def __init__(self, id, name, address, contact, services, availability):
        self.id = id
        self.name = name
        self.address = address
        self.contact = contact
        self.services = services
        self.availability = availability

    def add_clinic(self):
        pass

    def update_clinic_info(self):
        pass

    def set_availability(self):
        pass

    def view_appointments(self):
        pass


class Doctor:
    def __init__(self, id, name, clinic, specialization):
        self.id = id
        self.name = name
        self.clinic = clinic
        self.specialization = specialization

    def add_doctor(self):
        pass

    def update_doctor_info(self):
        pass

    def view_appointments(self):
        pass


class Appointment:
    def __init__(self, id, clinic_id, patient_id, date_time, status):
        self.id = id
        self.clinic_id = clinic_id
        self.patient_id = patient_id
        self.date_time = date_time
        self.status = status

    def book_appointment(self):
        pass

    def cancel_appointment(self):
        pass

    def reschedule_appointment(self):
        pass


class Notification:
    def __init__(self, id, user_id, message, date_time):
        self.id = id
        self.user_id = user_id
        self.message = message
        self.date_time = date_time

    def send_notification(self):
        pass


class Admin:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def add_user(self):
        pass

    def add_clinic(self):
        pass

    def add_doctor(self):
        pass


class System:
    def __init__(self):
        self.users = []
        self.clinics = []
        self.doctors = []
        self.appointments = []
        self.notifications = []

