from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,"login.html")


def main_view(request):
    return render(request,"main.html")


def library_modify_view(request):
    return render(request,"library_modify.html")