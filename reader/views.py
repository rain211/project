import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from library.models import *
from django.http import HttpResponse
# Create your views here.
def page_num(num,size):
    num = int(num)
    paginator = Paginator(Readerinfo.objects.filter(isdelete=0).order_by('rname'),size)
    if num < 1:
        num = 1
    if num > paginator.num_pages:
        num = paginator.num_pages
    start = ((num-1)//3)*3+1
    end = start + 3
    if end > paginator.num_pages:
        end = paginator.num_pages+1
    return paginator.page(num),range(start,end)
def readerset_view(request,num='1'):
    read, page = page_num(num, 10)
    if request.method == 'GET':
        return render(request,'readerset.html',{'read':read,'page':page})
    else:
        key = request.POST.get('key')
        if not key:
            return render(request,'readerset.html',{'read':read,'page':page})
        if request.POST.get('method') == 'barcode':
            reader = Readerinfo.objects.filter(barcode=key)
        elif request.POST.get('method') == 'rname':
            reader = Readerinfo.objects.filter(rname=key)
        else:
            reader = Readerinfo.objects.filter(paperno=key)
        return render(request,'readerset.html',{'read':reader})
def readertype_view(request):
    return render(request,'readerType.html')


def addreader_view(request):
    readtype0 = Readertype.objects.get(rtid=1)
    readtype1 = Readertype.objects.get(rtid=2)
    readtype2 = Readertype.objects.get(rtid=3)
    if request.method == 'GET':
        return render(request,'addreader.html',{'readtype0':readtype0,'readtype1':readtype1,'readtype2':readtype2})
    else:
        rname = request.POST.get('rname')
        gender = request.POST.get('gender')
        tel = request.POST.get('tel')
        add = request.POST.get('address')
        email = request.POST.get('email')
        papertype = request.POST.get('papertype')
        paperno = request.POST.get('paperno')
        birthday = request.POST.get('birthday')
        readtype = request.POST.get('readtype')
        barcode = request.POST.get('barcode')
        time = request.POST.get('time')
        readtype = Readertype.objects.get(rtid=readtype)
        birthday = datetime.datetime.strptime(birthday,'%Y-%m-%d')
        time = datetime.datetime.strptime(time,'%Y-%m-%d')
        reader = Readerinfo.objects.create(rname=rname,gender=gender,tel=tel,address=add,email=email,papertype=papertype,
                                           paperno=paperno,birthday=birthday,rtid=readtype,barcode=barcode,createdate=time,
                                           isdelete=0)
        reader.save()
        return redirect('/reader/addreader/')


def readerchange_view(request,num):
    if request.method == 'GET':
        reader = Readerinfo.objects.get(rid=num)
        return render(request,'readerchange.html',{'reader':reader})
    else:
        rname = request.POST.get('rname')
        gender = request.POST.get('gender')
        tel = request.POST.get('tel')
        add = request.POST.get('address')
        email = request.POST.get('email')
        papertype = request.POST.get('papertype')
        paperno = request.POST.get('paperno')
        birthday = request.POST.get('birthday')
        readtype = request.POST.get('readtype')
        readtype = Readertype.objects.get(rtid=readtype)
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        Readerinfo.objects.filter(rid=num).update(rname=rname,gender=gender,tel=tel,address=add,email=email,papertype=papertype,
                                           paperno=paperno,birthday=birthday,rtid=readtype)
        return redirect('/reader/readerchange/'+num)


def readerdel_view(request,num):
    Readerinfo.objects.filter(rid=num).update(isdelete=1)
    return redirect('/reader/')