import datetime
import hashlib
import requests
import json
import mysql.connector

reserve_url = "https://localhost/reserve/"
slot_url = "https://localhost/slots/"
db_server = ''
db_user = ''
db_password = ''
database = ''
mydb = mysql.connector.connect(
    host=db_server,
    user=db_user,
    password=db_password,
    database=database
)
cursor = mydb.cursor()


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
        cursor.execute(sql)
        res = cursor.fetchone()
        if res.values() is None:
            print("Wrong email or password")
        else:
            self.log_in = True
            print('Wellcome')

    def log_out(self):
        if self.log_in:
            self.log_in = False

    def view_appointments(self):
        sql = f"SELECT doctor.name, clinic.name, appointmnet.datetime " \
              f"FROM appointment INNER JOIN user ON userid = fk_user" \
              f"INNER JOIN doctor ON dooctorid = fk_doctor" \
              f"INNER JOIN clinic ON clinicid = fk_clinic " \
              f"WHERE user.email = '{self.email}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        for record in res:
            print(record)

    def get_slot(self):
        slots = requests.get(slot_url).json()
        slots = json.loads(slots)[0]
        print(slots)

    def set_slot(self, id, resrved):
        requests.post(reserve_url, data=json.dumps({'id': id, 'reserved': resrved}))


class Clinic:
    def __init__(self, name: str, address: str, contact: str, availability: bool, capacity: int, id: int = None):
        self.id = id
        self.name = name
        self.address = address
        self.contact = contact
        self.availability = availability
        self.capacity = capacity


class Doctor:
    def __init__(self, name: str, specialization: str, id: int = None):
        self.id = id
        self.name = name
        self.specialization = specialization

    def add_doctor(self):
        # Get the doctor attributes from the object
        name = self.name
        specialization = self.specialization
        # Create a SQL query to insert the doctor data into the doctor table
        sql = f"INSERT INTO doctor (Name, specialization) VALUES ('{name}', '{specialization}')"
        # Execute the query
        cursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Print a confirmation message
        print("Doctor added")

    def update_doctor_info(self):
        # Get the doctor attributes from the object
        id = self.id
        name = self.name
        specialization = self.specialization
        # Create a SQL query to update the doctor data in the doctor table
        sql = f"UPDATE doctor SET Name = '{name}', specialization = '{specialization}' WHERE idDoctor = {id}"
        # Execute the query
        cursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Print a confirmation message
        print("Doctor info updated")

    def view_appointments(self):
        name = self.name
        specialization = self.specialization
        sql = f"""  SELECT appointment.DateTime, appointment.Status, user.name AS user_name, clinic.name AS clinic_name 
                    FROM appointment INNER JOIN doctor ON appointment.FK_Doctor = doctor.idDoctor
                    INNER JOIN user ON appointment.FK_User = user.idUser
                    INNER JOIN clinic ON appointment.FK_Clinic = clinic.idClinic
                    WHERE doctor.name = '{name}' AND doctor.specialization = '{specialization}'"""
        cursor.execute(sql)
        # Fetch all the results
        results = cursor.fetchall()
        # Print the results
        for row in results:
            print(row)


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
        # Get the appointment attributes from the object
        clinic_id = self.clinic.id
        user_id = self.user.id
        doctor_id = self.doctor.id
        date_time = self.date_time
        status = self.status
        # Create a SQL query to insert the appointment data into the appointment table
        sql = f"INSERT INTO appointment (FK_Clinic, FK_User, FK_Doctor, DateTime, Status) VALUES ({clinic_id}, {user_id}, {doctor_id}, '{date_time}', {status})"
        # Execute the query
        cursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Print a confirmation message
        print("Appointment booked")

    def cancel_appointment(self):
        # Get the appointment id from the object
        appointment_id = self.id
        # Create a SQL query to delete the appointment data from the appointment table
        sql = f"DELETE FROM appointment WHERE idAppointment = {appointment_id}"
        # Execute the query
        cursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Print a confirmation message
        print("Appointment cancelled")

    def reschedule_appointment(self):
        # Get the appointment id and new date_time from the object
        appointment_id = self.id
        date_time = self.date_time
        # Create a SQL query to update the appointment data in the appointment table
        sql = f"UPDATE appointment SET DateTime = '{date_time}' WHERE idAppointment = {appointment_id}"
        # Execute the query
        cursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Print a confirmation message
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

    def add_clinic(self):
        # Get the clinic attributes from the clinic object
        name = self.clinic.name
        address = self.clinic.address
        contact = self.clinic.contact
        availability = self.clinic.availability
        capacity = self.clinic.capacity
        admin_name = self.name
        admin_email = self.email
        admin_password = self.password
        # Generate a temporary password for the admin
        admin_tmppassword = hashlib.sha256(admin_password).hexdigest()
        # Create a SQL query to insert the clinic data into the clinic table
        sql = f"INSERT INTO clinic (Name, address, contact, availability, capacity, admin_name, admin_email, admin_hashedpassword, admin_tmppassword) VALUES ('{name}', '{address}', '{contact}', {availability}, {capacity}, '{admin_name}', '{admin_email}', '{admin_password}', '{admin_tmppassword}')"
        # Execute the query
        cursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Print a confirmation message
        print("Clinic added by admin")

    def change_capacity(self, id, capacity):
        requests.post(reserve_url, data=json.dumps({'id': id, 'reserved': -capacity}))

    def get_slot(self):
        slots = requests.get(slot_url).json()
        slots = json.loads(slots)[0]
        print(slots)
