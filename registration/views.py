from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from .models import Registration
from .email_utils import send_squid_game_email  # Import the function

def get_player_number():
    """Auto-generate a unique player number."""
    last_player = Registration.objects.order_by('-id').first()
    return (last_player.player_number + 1) if last_player else 1  # Increment previous player number

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        year = request.POST.get('year')
        department = request.POST.get('department')
        college = request.POST.get('college')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Check if email is already registered
        if Registration.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "This email is already registered!"})

        try:
            # Generate a unique player number
            player_number = get_player_number()

            # Create registration entry
            new_registration = Registration.objects.create(
                name=name,
                year=year,
                department=department,
                college=college,
                phone=phone,
                email=email,
                player_number=player_number  # Save player number
            )

            # Send Squid Game themed email
            send_squid_game_email(email, name, player_number)  # Now calling from email_utils.py

            return redirect("success")  # Redirect to success page

        except IntegrityError:
            return render(request, "register.html", {"error": "Something went wrong. Try again!"})

    return render(request, 'register.html')


def success(request):
    return render(request, 'success.html')

def registrations_list(request):
    participants = Registration.objects.all()  # Fetch all records
    return render(request, "registrations.html", {"participants": participants})

def home(request):
    return render(request, 'home.html')

