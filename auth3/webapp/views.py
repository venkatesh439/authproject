from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import  signupform
from django.http import HttpResponseRedirect


# Create your views here.
def homeview(request):
    return render(request,'myapp/home.html')
@login_required()
def javaview(request):
    return render (request,'myapp/java.html')
@login_required
def pythonview(request):
    return render (request,'myapp/python.html')
@login_required
def aptview(request):
    return render (request,'myapp/apt.html')
def logout(request):
    return render(request,'myapp/logout.html')
def Studentformview(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render (request,'myapp/signout.html',{'form':form})



