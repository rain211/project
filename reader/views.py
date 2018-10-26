from django.shortcuts import render

# Create your views here.
def readerset_view(request):
    return render(request,'readerset.html')


def readertype_view(request):
    return render(request,'readerType.html')