from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Clinic, Doctor, Appointment, Notification, Admin


def user_sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, hashed_password=password)
            user.log_in = True
            user.save()
            return HttpResponse("User logged in successfully!")
        except User.DoesNotExist:
            return HttpResponse("Invalid email or password")

    return render(request, 'login.html')


def user_sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(name=name, email=email, hashed_password=password)
        user.save()
        return HttpResponse("User signed up successfully!")

    return render(request, 'register.html')


def user_search(request, keyword):
    # Implement your search logic here based on the provided keyword
    # Return the search results to the user
    return render(request, 'search_results.html', {'results': ''})


def user_book_appointment(request):
    if request.method == 'POST':
        # Retrieve values from the POST request
        clinic_id = request.POST.get('clinic_id')
        doctor_id = request.POST.get('doctor_id')
        user_id = request.POST.get('user_id')
        date_time = request.POST.get('date_time')

        # Do something with the values...

        # Example: Return a response with the received values
        return HttpResponse(
            f"Book appointment for Clinic {clinic_id}, Doctor {doctor_id}, User {user_id}, DateTime {date_time}")

    else:
        # Handle other cases, such as displaying the form initially
        return render(request, 'book.html')


def user_view_last_reservation(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('user_id')
            user = User.objects.get(id=user_id)
            last_reservation = Appointment.objects.filter(FK_User=user).order_by('-DateTime').first()
            return render(request, 'user_last_reservation.html', {'reservation': last_reservation})
        except User.DoesNotExist:
            return HttpResponse("User not found")

    # Handle GET request or initial form display
    return render(request, 'last_reservations.html', {'reservation': None})


def user_view_current_reservations(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            current_reservations = Appointment.objects.filter(FK_User=user, Status=0)
            return render(request, 'user_current_reservations.html', {'reservations': current_reservations})
        except User.DoesNotExist:
            return HttpResponse("User not found")

    return render(request, 'user.html')


def user_cancel_reservation(request, user_id, appointment_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            appointment = Appointment.objects.get(idAppointment=appointment_id, FK_User=user, Status=0)
            appointment.delete()
            return HttpResponse("Reservation canceled successfully!")
        except (User.DoesNotExist, Appointment.DoesNotExist):
            return HttpResponse("Invalid user or reservation")

    return render(request, 'user_cancel_reservation_page.html')


def user_page(request):
    user = request.user  # Assuming you are using Django authentication
    return render(request, 'home.html')


# Secretary views

def secretary_sign_in(request, email, password):
    try:
        secretary = Admin.objects.get(admin_email=email, admin_hashedpassword=password)
        secretary.log_in = True
        secretary.save()
        return HttpResponse("Secretary logged in successfully!")
    except Admin.DoesNotExist:
        return HttpResponse("Invalid email or password")


def secretary_sign_up(request, name, email, password, clinic_id):
    clinic = Clinic.objects.get(idClinic=clinic_id)
    secretary = Admin(name=name, email=email, password=password, clinic=clinic)
    secretary.save()
    return HttpResponse("Secretary signed up successfully!")


def secretary_view_current_reservations(request, secretary_id):
    try:
        secretary = Admin.objects.get(id=secretary_id)
        current_reservations = Appointment.objects.filter(FK_Clinic=secretary.clinic, Status=0)
        return render(request, 'secretary_current_reservations.html', {'reservations': current_reservations})
    except Admin.DoesNotExist:
        return HttpResponse("Secretary not found")


def secretary_cancel_reservation(request, secretary_id, appointment_id):
    try:
        secretary = Admin.objects.get(id=secretary_id)
        appointment = Appointment.objects.get(idAppointment=appointment_id, FK_Clinic=secretary.clinic, Status=0)
        appointment.delete()
        return HttpResponse("Reservation canceled successfully!")
    except (Admin.DoesNotExist, Appointment.DoesNotExist):
        return HttpResponse("Invalid secretary or reservation")


def secretary_increase_capacity(request, secretary_id, amount):
    try:
        secretary = Admin.objects.get(id=secretary_id)
        secretary.clinic.capacity += amount
        secretary.clinic.save()
        return HttpResponse("Clinic capacity increased successfully!")
    except Admin.DoesNotExist:
        return HttpResponse("Secretary not found")


def default_view(request):
    # You can customize this view based on your needs
    return render(request, 'home.html')
