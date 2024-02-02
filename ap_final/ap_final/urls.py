# myapp/urls.py
from django.urls import path
from ap_final.Clinic_reservation_app.views import (
    user_sign_in, user_sign_up, user_search, user_book_appointment,
    user_view_last_reservation, user_view_current_reservations, user_cancel_reservation,
    secretary_sign_in, secretary_sign_up, secretary_view_current_reservations,
    secretary_cancel_reservation, secretary_increase_capacity
)

urlpatterns = [
    path('user/signin/<str:email>/<str:password>/', user_sign_in, name='user-signin'),
    path('user/signup/<str:name>/<str:email>/<str:password>/', user_sign_up, name='user-signup'),
    path('user/search/<str:keyword>/', user_search, name='user-search'),
    path('user/book/<int:clinic_id>/<int:doctor_id>/<int:user_id>/<str:date_time>/', user_book_appointment, name='user-book'),
    path('user/view/last-reservation/<int:user_id>/', user_view_last_reservation, name='user-view-last-reservation'),
    path('user/view/current-reservations/<int:user_id>/', user_view_current_reservations, name='user-view-current-reservations'),
    path('user/cancel-reservation/<int:user_id>/<int:appointment_id>/', user_cancel_reservation, name='user-cancel-reservation'),

    path('secretary/signin/<str:email>/<str:password>/', secretary_sign_in, name='secretary-signin'),
    path('secretary/signup/<str:name>/<str:email>/<str:password>/<int:clinic_id>/', secretary_sign_up, name='secretary-signup'),
    path('secretary/view/current-reservations/<int:secretary_id>/', secretary_view_current_reservations, name='secretary-view-current-reservations'),
    path('secretary/cancel-reservation/<int:secretary_id>/<int:appointment_id>/', secretary_cancel_reservation, name='secretary-cancel-reservation'),
    path('secretary/increase-capacity/<int:secretary_id>/<int:amount>/', secretary_increase_capacity, name='secretary-increase-capacity'),
]