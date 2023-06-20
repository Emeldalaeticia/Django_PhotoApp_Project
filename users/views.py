from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView


from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from .forms import SignUpForm

class SignUpView(CreateView):

    template_name = 'users/signup.html'

    form_class = SignUpForm

    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):
        to_return = super().form_valid(form)

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        email = form.cleaned_data["email"]

        user = User.objects.create_user(username=username, email=email, password=password)
        user = authenticate(username=username, password=password)

        login(self.request, user)

        return to_return

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True