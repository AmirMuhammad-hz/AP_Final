import datetime
import hashlib


class User:
    def __init__(self, name: str, email: str, password: str, id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.log_in = False
        self.tmp_password = None

    def sign_in(self):
        if self.tmp_password is None:
            sql = f"SELECT * FROM user WHERE hashed_password = '{hashlib.sha256(self.password)}' " \
                  f"and email ='{self.email}'"
        else:
            sql = f"SELECT * FROM user WHERE hashed_password = '{hashlib.sha256(self.tmp_password)}' " \
                  f"and email ='{self.email}'"

    def log_out(self):
        if self.log_in:
            self.log_in = False

    def update_profile(self):
        print("User profile updated")

    def view_appointments(self):
        sql = f"SELECT * FROM appointment INNER JOIN user WHERE user.email = '{self.email}'"


class Clinic:
    def __init__(self, name: str, address: str, contact: str, availability: bool, capacity: int, id: int = None):
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
    def __init__(self, name: str, specialization: str, id: int = None):
        self.id = id
        self.name = name
        self.specialization = specialization

    def add_doctor(self):
        sql = ''

    def update_doctor_info(self):
        print("Doctor info updated")

    def view_appointments(self):
        sql = f"SELECT * FROM appointment INNER JOIN doctor WHERE doctor.name = '{self.name}' " \
              f"and doctor.specialization = '{self.specialization}'"


class Appointment:
    def __init__(self, clinic: Clinic, user: User, doctor: Doctor, date_time: datetime.datetime, status: int,
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
    def __init__(self, user: User, message: str, date_time: datetime.datetime, id: int = None):
        self.id = id
        self.user = user
        self.message = message
        self.date_time = date_time

    def send_notification(self):
        print("Notification sent")


class Admin:
    def __init__(self, name: str, email: str, password: str, clinic: Clinic, id: int = None):
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
