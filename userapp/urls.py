from urllib.parse import urlparse
from django.urls import path
from . import views as vs
app_name = 'userapp'

urlpatterns = [
    path('sign-up/', vs.sign_up, name='sign-up'),
    path('password_change/', vs.change_password, name='password_change'), ]
