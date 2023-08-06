from django.shortcuts import render

def home(request):
    return render(request,'cms/home.html')


def about_us(request):
    return render(request,'cms/about_us.html')

def faculty_info(request):
    info=Faculty.objects.all()
    return render(request,'cms/fac_info.html',{'info':info})