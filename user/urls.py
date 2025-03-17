from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from . import views
app_name = 'user'
urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name ='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('change_password/', PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='change_password_done'),
    path('password_reset_form/', PasswordResetView.as_view(template_name="password_reset_form.html"), name = "password_reset_form" ),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name = "password_reset_done" ),
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name = "password_reset_confirm" )
]


