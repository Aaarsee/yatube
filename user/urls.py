from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
app_name = 'user'
urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='user/logged_out.html'), name ='logout')
    
    ]
