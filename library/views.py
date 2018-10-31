import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from library.models import Manager, Bookinfo, Borrow, Readerinfo, Bookcase
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
    if request.method == 'GET':
        return render(request,'bookBorrow.html')
    else:
        barcode = request.POST.get('barcode')
        key = request.POST.get('inputkey')
        radio = request.POST.get('f')
        btime = request.POST.get('inputbtime')
        bactime = request.POST.get('inputbacktime')
        submit = request.POST.get('submit3')
        submit4 = request.POST.get('submit4')
        submit5 = request.POST.get('submit5')
        if  barcode == '':
            readers = ''
        else:
            readers = Readerinfo.objects.get(barcode=barcode)
        if key == '':
            infos = ''
        else:
            if radio == 'isbn':
                infos = Bookinfo.objects.get(isbn=key)
                if submit5 == '完成归还':
                    Borrow.objects.filter(rid=readers, bid__isbn=key).update(ifback=1)
            if radio == 'bookname':
                infos = Bookinfo.objects.get(bname=key)
                if submit5 == '完成归还':
                    Borrow.objects.filter(rid=readers,bid__bname=key).update(ifback=1)

        if submit == '完成借阅':
            if btime == '' or bactime == '':
                borrowtime = ''
                bactkime = ''
            else:
                borrowtime = datetime.datetime.strptime(btime, '%Y-%m-%d')
                backtime = datetime.datetime.strptime(bactime, '%Y-%m-%d')
                Borrow.objects.create(rid= readers,bid = infos,borrowtime = borrowtime,backtime = backtime,operator = '张老汉',ifback = 0)
        if submit4 == '完成续借':
            if btime == '' or bactime == '':
                borrowtime = ''
                bactkime = ''
            else:
                borrowtime = datetime.datetime.strptime(btime, '%Y-%m-%d')
                backtime = datetime.datetime.strptime(bactime, '%Y-%m-%d')
                Borrow.objects.filter(rid= readers,bid = infos,borrowtime = borrowtime,operator = '张老汉',ifback = 0).update(backtime = backtime,)

        return render(request,"bookBorrow.html",{'readers':readers,'infos':infos,'barcode':barcode,
                                                 'key':key,'borrowtime':btime,'backtime':bactime})


def bookRenew_view(request):
    if request.method == 'GET':
        return render(request,'bookRenew.html')
    else:
        barcode = request.POST.get('barcode')
        bactime = request.POST.get('inputbacktime')
        submit = request.POST.get('submit3')

        if barcode == '':
            readers = ''
        else:
            readers = Readerinfo.objects.get(barcode=barcode)

        if submit == '完成续借':
            if  bactime == '':
                bactkime = ''
            else:

                backtime = datetime.datetime.strptime(bactime, '%Y-%m-%d')
                Borrow.objects.update(backtime = backtime,operator = '张老汉',ifback = 0)
        infos = Bookinfo.objects.get(borrow__rid__barcode=barcode)
        return render(request,"bookRenew.html",{'readers':readers,'barcode':barcode,'backtime':bactime,'infos':infos})


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







