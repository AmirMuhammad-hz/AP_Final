from django.db import models

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    hashed_password = models.CharField(max_length=45)
    tmp_password = models.CharField(max_length=45)
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=45)
    specialization = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    availability = models.IntegerField()
    capacity = models.IntegerField()
    admin_name = models.CharField(max_length=45)
    admin_email = models.EmailField(unique=True)
    admin_hashedpassword = models.CharField(max_length=45)
    admin_tmppassword = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DateTime = models.DateTimeField()
    Status = models.SmallIntegerField()

    def __str__(self):
        return f"Appointment at {self.clinic.name} with Dr. {self.doctor.name} for {self.user.name} on {self.DateTime}"

class ClinicDoctor(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor.name} at {self.clinic.name}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Notification to {self.user.name} at {self.date_time}"

class Admin(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

