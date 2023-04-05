from django.shortcuts import render, redirect
from .forms import NewUserCreation
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# def register_users(request):
#     return render(request, "register.html", {"register_form" : NewUserCreation()})

# def register_users(request):  # to user UserCreationForm
#     return render(request, "register.html", {"register_form" : UserCreationForm()})   

def register_users(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("register")
    form = NewUserCreation()  # GET method
    return render(request = request, template_name= "register.html", context= {"register_form" : form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
            else:
                return redirect("login_user")
        else:
            return redirect("login_user")
    form = AuthenticationForm()    # GET method
    return render(request=request, template_name="login.html", context={"login_form" : form})

def logout_user(request):
    logout(request)
    return redirect("login_user")


# ---------------------------------- PAGINATOR --------------------------------------------
# The paginator classes lives in django.core.paginator. We will be working mostly with the Paginator 

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

# Pagination with Function-Based Views-----

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'users': users })



# --------- CLASS BASED VIEW ---------------------------

# Login View:-

from django.contrib.auth import forms
from django.contrib.auth.views import LoginView, LogoutView

class LoginPageView(LoginView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, context={"login_form" : form})

    def post(self,request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])

            if user:
                login(request, user)
                return redirect('home_page')
        return render(request, self.template_name, context={"login_form" : form})




