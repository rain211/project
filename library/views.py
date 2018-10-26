from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from library.models import Manager


def login_view(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        name= request.POST.get('name')
        pwd  = request.POST.get('pwd')
        count = Manager.objects.filter(user = name,pwd = pwd).count()
        message = '账号或密码有误'
        if count == 1:
            return render(request,'main.html')
        return render(request,'login.html',{'message':message})
def main_view(request):
    return render(request,"main.html")


def library_modify_view(request):
    return render(request,"library_modify.html")

def manager_view(request):
    return render(request,"manager.html")

def parameter_modify_view(request):
    return render(request,"parameter_modify.html")


def bookcase_view(request):
    return render(request,"bookcase.html")


def readerType_view(request):
    return render(request,"readerType.html")


def reader_view(request):
    return render(request,"reader.html")


def bookType_view(request):
    return render(request,"bookType.html")


def book_view(request):
    return render(request,"book.html")


def bookBorrow_view(request):
    return render(request,"bookBorrow.html")


def bookRenew_view(request):
    return render(request,"bookRenew.html")


def bookBack_view(request):
    return render(request,"bookBack.html")


def bookQuery_view(request):
    return render(request,"bookQuery.html")


def borrowQuery_view(request):
    return render(request,"borrowQuery.html")


def bremind_view(request):
    return render(request,"bremind.html")


def pwd_Modify_view(request):
    return render(request,"pwd_Modify.html")

