from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Home - Ecommerce"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "After login content"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About - Ecommerce"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    print(request.session['cart_id'])
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(contact_form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            redirect("/")
        else:
            print("Error")
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "title": "Contact - Ecommerce",
        "form": form
    }
    print("User Logged In")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            redirect("/login")
        else:
            print("Error")
    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
    return render(request, "auth/register.html", context)
