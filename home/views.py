from django.shortcuts import render

# Create your views here.
def home_list(request):
    if request.user.is_authenticated:
        ctx = {
            "logged_user": request.user.profile,
        }
    else:
        ctx = {}

    return render(request, "home.html", ctx)