# Import necessary modules and models
from django.forms import ValidationError 
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Home(requests):
    return render(requests,'main/home.html')

@login_required
def About(request):
    return render(request,'main/about.html')

@login_required
def contact(requests):
    return render(requests,'main/contact.html')

@login_required
def product(requests):
    return render(requests,'main/product.html')


def Login(request): 
    # Check if the HTTP request method is POST
    if request.method == "POST":
        username = request.POST.get('username') # get username
        password = request.POST.get('password') # get password
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists(): # if user is not exist
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
        else:
            # Authenticate the user with the provided username and password
            user = authenticate(username=username, password=password)
            
            if user is None:
                # Display an error message if authentication fails (invalid password)
                messages.error(request, "Invalid Password")
            else:
                # Log in the user and redirect to the home page upon successful login
                login(request, user)  # Use Django's auth_login to log in
                return redirect('home')  # Redirect to your home page  
    
    # Render the login page template
    return render(request, 'main/login.html')

def Signup(request):

    # Check if the HTTP request method is POST
    if request.method == "POST":
        # get the username and email and password
        username = request.POST.get('username') 
        Email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists in the database
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'main/signup.html')  # Render the signup form with an error message

        # Check if email already exists in the database
        if User.objects.filter(email=Email).exists():
            messages.error(request, "Email is already registered. Please use a different one.")
            return render(request, 'main/signup.html')  # Render the signup form with an error message
        try:
            # Create and save the new user
            user = User.objects.create_user(username=username, email=Email, password=password)
            user.save()  # Save the user to the database
            messages.success(request, 'Signup successful! You can now log in.')
            return redirect("login")  # Redirect to the login page

        except ValidationError as v:
            messages.error(request, f'Error creating user: {v}')  # Handle validation errors
            return render(request, 'main/signup.html')  # Render the signup form with an error message
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {e}')  # Handle unexpected errors
            return render(request, 'main/signup.html')  # Render the signup form with an error message

    else:
        return render(request, 'main/signup.html')  # Render the signup form for GET requests

def Logout(request):
    logout(request) # logout the user
    return redirect('home') # redirect to home page


# @login_required
# def download_app(request):

#     file_path = os.path.join('static', 'App.zip') 
#     response = FileResponse(open(file_path, 'rb'), as_attachment=True)
#     return response