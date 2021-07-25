from django.urls import path, include
from accounts.views import student_registration, mentor_registration , change_password
from rest_framework.authtoken.views import obtain_auth_token

app_name = "accounts"

urlpatterns = [
    path("register/mentor", mentor_registration, name="mentor-signup"),
    path("register/student", student_registration, name="student-signup"),
    path("login", obtain_auth_token, name="login"),
    path("newpass/", change_password, name="change-password"),

]
