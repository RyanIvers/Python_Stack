from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validate_register(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/home')
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw
    )
    print(new_user.first_name)
    request.session['user_id'] = new_user.id
    return redirect('/home')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id           
            return redirect("/home")
        messages.error(request, "Invalid Credentials")
        return redirect('/')
    messages.error(request, "Email doesn't exist, register an account")
    return redirect("/")


def home(request):
    if "user_id" not in request.session:
        return redirect('/')
    user_id = int(request.session['user_id'])
    context = {
        "specified_user" : User.objects.get(id=user_id),
    }
    return render(request, "welcome.html", context)

def log_out(request):
    del request.session['user_id']
    return redirect('/')
