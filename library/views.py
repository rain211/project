from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from library.models import Manager, Bookinfo, Borrow, Readerinfo
from reader.views import page_num


def login_view(request):
    # def set_cookie():
    #     response = HttpResponse()
    #     response.set_cookie('uname', 'zhangsan', max_age=24 * 60 * 60)

    if request.method == 'GET':
        return render(request, "login.html")
    else:
        name= request.POST.get('name')
        pwd  = request.POST.get('pwd')
        count = Manager.objects.filter(user=name,pwd=pwd).count()
        manager = Manager.objects.filter(user=name,pwd=pwd)
        message = '账号或密码有误'
        if count == 1:
            # set_cookie()
            return redirect('/library/main/')

        return render(request,'login.html',{'message':message,'manager':manager})
def main_view(request):
    infos = Bookinfo.objects.all()
    # booktype = Bookinfo.objects.filter(btid=bid)
    # print(infos)
    # borrow = Bookinfo.objects.get().borrow_set.all().count()
    return render(request,"main.html",{'infos':infos})


def library_modify_view(request):
    return render(request,"library_modify.html")

def manager_view(request):
    return render(request,"manager.html")

def parameter_modify_view(request):
    return render(request,"parameter_modify.html")


def bookcase_view(request):
    return render(request,"bookcase.html")


def readerType_view(request):
    return render(request, "../reader/templates/readerType.html")


def reader_view(request):
    return render(request, "../reader/templates/readerset.html")


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


def bookQuery_view(request,num = '1'):
    return render(request, 'bookQuery.html')



def borrowQuery_view(request):
    # infos,page = page_num(num,10)
    if request.method == 'GET':
        return render(request,"borrowQuery.html")
    else:

        key = request.POST.get('key')
        flagb = request.POST.get('flagb')
        flaga = request.POST.get('flaga')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        if not flaga == 'a':

            if flagb == 'b':
                infos = Borrow.objects.filter(borrowtime__gte=sdate, borrowtime__lte=edate)
                return render(request, "borrowQuery.html", {'infos': infos})
            return render(request,'borrowQuery.html')
        if flagb == 'b':
            if request.POST.get('method') == 'isbn':
                infos = Borrow.objects.filter(bid__isbn=key, borrowtime__gte=sdate, borrowtime__lte=edate)
            elif request.POST.get('method') == 'bname':
                infos = Borrow.objects.filter(bid__bname=key, borrowtime__gte=sdate, borrowtime__lte=edate)
            elif request.POST.get('method') == 'barcode':
                infos = Borrow.objects.filter(rid__barcode=key, borrowtime__gte=sdate, borrowtime__lte=edate)
            elif request.POST.get('method') == 'rname':
                infos = Borrow.objects.filter(rid__rname=key, borrowtime__gte=sdate, borrowtime__lte=edate)

            return render(request, "borrowQuery.html", {'infos': infos})
        else:
            if request.POST.get('method') == 'isbn':
                infos = Borrow.objects.filter(bid__isbn=key)

            elif request.POST.get('method') == 'bname':
                infos = Borrow.objects.filter(bid__bname=key)
            elif request.POST.get('method') == 'barcode':
                infos = Borrow.objects.filter(rid__barcode=key)
            elif request.POST.get('method') == 'rname':
                infos = Borrow.objects.filter(rid__rname=key)
            return render(request, "borrowQuery.html", {'infos': infos})




def bremind_view(request):
    borrows = Borrow.objects.all()
    return render(request,"bremind.html",{'borrows':borrows})
def pwd_Modify_view(request):
    if request.method == 'GET':
        return render(request, "pwd_Modify.html")
    else:
        name= request.POST.get('name')
        oldpwd = request.POST.get('oldpwd')
        pwd1 = request.POST.get('pwd1')
        pwd = request.POST.get('pwd')
        manager = Manager.objects.filter(user = name, pwd = oldpwd)
        if manager.count() == 1:
            manager.update( pwd=pwd1)
            message = '修改成功'
            return render(request, 'pwd_Modify.html', {'message': message})
        else:
            message = '账号或原密码有误'
            return render(request, 'pwd_Modify.html', {'message': message})







