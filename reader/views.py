import datetime

from django.shortcuts import render, redirect
from library.models import *
# Create your views here.
def readerset_view(request):
    read = Readerinfo.objects.all()
    return render(request,'readerset.html',{'read':read})


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
                                           paperno=paperno,birthday=birthday,rtid=readtype,barcode=barcode,createdate=time)
        reader.save()
        return redirect('/reader/addreader/')