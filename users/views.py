from django.shortcuts import render, redirect
from .models import User
from .forms import ProfileForm, FeedbackForm


def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        User.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            password=password
        )

        return redirect("login")

    return render(request, "users/register.html")


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(
            email=email,
            password=password
        ).first()

        if user:

            request.session["user_id"] = user.id
            request.session["user_name"] = user.full_name

            return redirect("dashboard")

        return render(
            request,
            "users/login.html",
            {"error": "Invalid email or password"}
        )

    return render(request, "users/login.html")


def logout(request):

    request.session.flush()

    return redirect("login")


def dashboard(request):

    return render(request, "users/dashboard.html")


def profile(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("login")

    user = User.objects.get(id=user_id)

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            instance=user
        )

        if form.is_valid():

            form.save()

            request.session["user_name"] = user.full_name

            return redirect("profile")

    else:

        form = ProfileForm(
            instance=user
        )

    return render(
        request,
        "users/profile.html",
        {"form": form}
    )


def user_list(request):

    users = User.objects.all().order_by("-created_at")

    return render(
        request,
        "users/user_list.html",
        {"users": users}
    )


def splash_view(request):

    return redirect("login")


def home_view(request):

    return render(request, "users/home.html")



# -------------------------
# Feedback Management
# -------------------------
def feedback(request):

    user_id = request.session.get("user_id")

    # Check if user is logged in
    if not user_id:
        return redirect("login")

    # Get logged-in user
    user = User.objects.get(id=user_id)

    if request.method == "POST":

        form = FeedbackForm(request.POST)

        if form.is_valid():

            feedback_data = form.save(commit=False)

            # Connect feedback with logged-in user
            feedback_data.user = user

            feedback_data.save()

            return redirect("feedback")

    else:

        form = FeedbackForm()

    return render(
        request,
        "users/feedback.html",
        {"form": form}
    )

# Agar file 'users/templates/users/token_history.html' me hai:
def token_history_view(request):
    return render(request, 'users/token_history.html')