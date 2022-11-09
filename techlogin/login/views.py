from django.shortcuts import render
from .models import Account,ForgetPass
import random,smtplib,string
from django.http import HttpResponse
from email.message import EmailMessage

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login("boomtech6996@gmail.com", "hpghfvgymaupbkox")

def loginpage(request):
    return render(request, 'login.html',{'iscor':""})

def createacc(request):
    return render(request,'create.html')

def ctom(request):
    email= request.POST['email']
    passw = request.POST['passw']
    name = request.POST['name']
    Account(email=email,passw=passw,name=name).save()
    return render(request,'mainpage.html',{'name':name})

def ltom(request):
    email= request.POST['email']
    passw = request.POST['passw']
    
    user = Account.objects.filter(email=email,passw=passw)
    if user.first()==None:
        return render(request, 'login.html',{'iscor':"there is something wrong with the email or password"})
    return render(request,'mainpage.html',{'name':user.values()[0]['name']})
    
def forpass(request):
    return render(request,'forgot.html')

def chforgot(request):
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=6))
    email = request.POST['email']
    
    em = EmailMessage()
    em['From'] = "boomtech6996@gmail.com"
    em['To'] = email
    em['Subject'] = "Nione"
    em.set_content("http://127.0.0.1:8000//"+res)
    s.sendmail("boomtech6996@gmail.com", email, em.as_string())
    ForgetPass(email=email,rlink=res).save()
    return HttpResponse("change password link has been sent to mail")

def chpass(request,email):
    fr = ForgetPass.objects.filter(rlink=email)
    if fr!=None:
        return render(request,"chpage.html",{'email':fr.values()[0]['email']})
    return HttpResponse("wrong link")

def change(request):
    fr = Account.objects.get(email = request.POST['email'])
    fr.passw = request.POST['passw']
    fr.save()
    
    return HttpResponse("password changed")

