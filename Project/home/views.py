from django.shortcuts import render
from .models import department,Doctors
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def index(request):
    numbers={
        'num':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,"index.html",numbers)


def about(request):
    return render(request,"about.html")



def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)


def Department(request):
    dict_dept={
        'dept': department.objects.all()
    }
    return render(request, 'department.html', dict_dept)




def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_docs)




def contact(request):
    return render(request,"contact.html")



