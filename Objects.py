import datetime


class User:
    def init(self, name: str, email: str, password: str, id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def sign_in(self):
        print("User registered")

    def log_out(self):
        print("User logged in")

    def update_profile(self):
        print("User profile updated")

    def view_appointments(self):
        print("User appointments:")


class Clinic:
    def init(self, name: str, address: str, contact: str, availability: bool, capacity: int, id: int = None):
        self.id = id
        self.name = name
        self.address = address
        self.contact = contact
        self.availability = availability
        self.capacity = capacity

    def add_clinic(self):
        print("Clinic added")

    def update_clinic_info(self):
        print("Clinic info updated")

    def set_availability(self):
        print("Clinic availability set")

    def view_appointments(self):
        print("Clinic appointments:")


class Doctor:
    def init(self, name: str, specialization: str, id: int = None):
        self.id = id
        self.name = name
        self.specialization = specialization

    def add_doctor(self):
        print("Doctor added")

    def update_doctor_info(self):
        print("Doctor info updated")

    def view_appointments(self):
        print("Doctor appointments:")


class Appointment:
    def init(self, clinic: Clinic, user: User, doctor: Doctor, date_time: datetime.datetime, status: int,
             id: int = None):
        self.id = id
        self.clinic = clinic
        self.user = user
        self.doctor = doctor
        self.date_time = date_time
        self.status = status

    def book_appointment(self):
        print("Appointment booked")

    def cancel_appointment(self):
        print("Appointment cancelled")

    def reschedule_appointment(self):
        print("Appointment rescheduled")


class Notification:
    def init(self, user: User, message: str, date_time: datetime.datetime, id: int = None):
        self.id = id
        self.user = user
        self.message = message
        self.date_time = date_time

    def send_notification(self):
        print("Notification sent")


class Admin:
    def init(self, name: str, email: str, password: str, clinic: Clinic, id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.clinic = clinic

    def add_user(self):
        print("User added by admin")

    def add_clinic(self):
        print("Clinic added by admin")

    def add_doctor(self):
        print("Doctor added by admin")
