from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
app_name = 'user'
urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name ='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login')
    
    ]
