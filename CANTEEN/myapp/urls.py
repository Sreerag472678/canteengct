from django.urls import path,include
from myapp import views
urlpatterns = [
    path('login/',views.login),
    path('register/',views.register),
]
