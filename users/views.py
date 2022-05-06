from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .forms import (CustomUserLoginForm, RegisterForm, 
					CustomUserPasswordChangeForm, CutomUserUpdateForm)


class CustomUserProfileView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
	model = CustomUser
	template_name = 'users/profile.html'
	fields = ['username','email']
	success_message = "Profile updated successfully." 


class CustomUserLoginView(SuccessMessageMixin, auth_views.LoginView):
	form_class = CustomUserLoginForm
	template_name = 'users/login.html'
	# redirect_authenticated_user = True
	success_message = "Login successfully." 

	# def get_success_url(self): # + redirect_authenticated_user = True -> send to other view if user is already auth and try to access login page
	# 	return reverse_lazy('employee-list')


class CustomUserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class CustomUserLogoutView(SuccessMessageMixin, auth_views.LogoutView):
	next_page = 'login'
	success_message = "Logout successfully" 


class CustomUserChangePassView(LoginRequiredMixin, auth_views.PasswordChangeView):  
	form_class = CustomUserPasswordChangeForm
	template_name = 'users/password_change_form.html'
	success_url = reverse_lazy('password_change_done')

class CustomUserChangePassDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
	template_name = 'users/password_change_done.html'

	