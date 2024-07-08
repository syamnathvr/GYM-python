from django.shortcuts import render,redirect
from  django.core.files.storage import FileSystemStorage
from . models import *


def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def classes(request):
    return render(request, "class.html")

def feature(request):
    return render(request, "feature.html")

def login(request):
    useremail = request.POST.get('useremail')
    userpass = request.POST.get('userpass')
    if useremail == 'admin@gmail.com' and userpass =='admin':
        request.session['adminemail'] = useremail
        request.session['admin'] ='admin'
        return render(request,'adminbase.html',{'status': 'admin login successfull'} )

    elif userdata.objects.filter(useremail=useremail,userpass=userpass).exists():
        udet=userdata.objects.get(useremail=request.POST['useremail'],userpass=userpass)
        if udet.userpass == request.POST['userpass']:
            request.session['uid'] = udet.id
            request.session['uname'] = udet.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'
            return render(request,'userbase.html',{'status': 'user login successfull'})

    else:
            return render(request, 'login.html', {'status': 'incorrect credentials'})
    return render(request, "login.html")



def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)



def signup(request):
    if request.method=="POST":
        userphoto=request.FILES['userphoto']
        up=FileSystemStorage()
        img=up.save(userphoto.name,userphoto)
        username=request.POST.get('username')
        useremail=request.POST.get('useremail')
        userpass=request.POST.get('userpass')
        data=userdata(username=username,useremail=useremail,userpass=userpass,userphoto=userphoto)
        data.save()
    return render(request, "signup.html")


def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)


def adminuserlist(request):
    data=userdata.objects.all()
    return render(request, "adminuserlist.html",{'result':data})

def adminuserdelete(request,id):
    mark=userdata.objects.get(pk=id)
    mark.delete()
    return redirect(adminuserlist)

def adminbase(request):
    return render(request, "adminbase.html")

def userbase(request):
    userid=request.session['uid']
    data = userdata.objects.get(id=userid)
    return render(request, "userbase.html", {'result':data})

def addstaff(request):
    if request.method=="POST":
        staffphoto=request.FILES['staffphoto']
        up=FileSystemStorage()
        img=up.save(staffphoto.name,staffphoto)
        staffname=request.POST.get('staffname')
        staffspec=request.POST.get('staffspec')
        data=staffdetails(staffname=staffname,staffspec=staffspec,staffphoto=staffphoto)
        data.save()
    return render(request, "addstaff.html")


def adminstaffview(request):
    data=staffdetails.objects.all()
    return render(request, "adminstaffview.html",{'result':data})

def adminclass(request):
    return render(request, "adminclass.html")

def addequip(request):
    return render(request, "addequip.html")

def userprofileview(request):
    userid=request.session['uid']
    data = userdata.objects.get(id=userid)
    return render(request, "userprofileview.html", {'result':data})


def addequip(request):
    if request.method=="POST":
        eqphoto=request.FILES['eqphoto']
        up=FileSystemStorage()
        img=up.save(eqphoto.name,eqphoto)
        eqname=request.POST.get('eqname')
        data=eqdetails(eqname=eqname,eqphoto=eqphoto)
        data.save()
    return render(request, "addequip.html")

def adminviewequip(request):
    data=eqdetails.objects.all()
    return render(request, "adminviewequip.html",{'result':data})

def addclass(request):
    if request.method=="POST":
        staffnames=request.POST.get('staffnames')
        staffspecs=request.POST.get('staffspecs')
        classtime=request.POST.get('classtime')
        classdate=request.POST.get('classdate')
        data=classdetails(staffnames=staffnames,staffspecs=staffspecs,classtime=classtime,classdate=classdate)
        data.save()
    data1=staffdetails.objects.all()
    return render(request,"adminclass.html",{'result':data1})

def adminclassview(request):
    data=classdetails.objects.all()
    return render(request, "adminclassview.html",{'result':data})

def userclassview(request):
    data=classdetails.objects.all()
    return render(request, "userclassview.html",{'result':data})

def userenrollclass(request):
    userid=request.session['uid']
    if request.method=="POST":
        staffnames=request.POST.get('staffnames')
        staffspecs=request.POST.get('staffspecs')
        classtime=request.POST.get('classtime')
        classdate=request.POST.get('classdate')
        data=enrollclass(userid=userid,staffnames=staffnames,staffspecs=staffspecs,classtime=classtime,classdate=classdate)
        data.save()
    data1=staffdetails.objects.all()
    return render(request,"enrollclass.html",{'result':data1})

def enrollclassview(request):
    userid=request.session['uid']
    data = enrollclass.objects.filter(userid=userid)
    return render(request, "enrollclassview.html",{'result':data})


def userequipview(request):
    data=eqdetails.objects.all()
    return render(request, "userequipview.html",{'result':data})

def userequipbook(request):
    userid=request.session['uid']
    if request.method=="POST":
       eqnames=request.POST.get('eqnames')
       classtime=request.POST.get('classtime')
       data=eqbook(userid=userid,eqnames=eqnames,classtime=classtime)
       data.save()
    data1=eqdetails.objects.all()
    return render(request, "userequipbook.html",{'result':data1})

def usereqbookview(request):
    userid=request.session['uid']
    data = eqbook.objects.filter(userid=userid)
    return render(request, "usereqbookview.html",{'result':data})

def userfeedback(request):
    userid=request.session['uid']
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        data=feedbacks(userid=userid,feedback=feedback)
        data.save()
    data1=userdata.objects.all()
    return render(request, "userfeedback.html",{'result':data1})

def classbookingsview(request):
    data=enrollclass.objects.all()
    return render(request, "classbookingsview.html",{'result':data})

def admineqbookview(request):
    data=eqbook.objects.all()
    return render(request, "admineqbookview.html",{'result':data})

def adminfeedbackview(request):
    data=feedbacks.objects.all()
    return render(request, "adminfeedbackview.html",{'result':data})

def userproupdate(request,id):
    data = userdata.objects.get(pk=id)
    return render(request, "userprofileupdate.html", {'result':data})


def userprofileupdate(request,id):
    if request.method=="POST":
        userphoto=request.FILES['userphoto']
        up=FileSystemStorage()
        img=up.save(userphoto.name,userphoto)
        username=request.POST.get('username')
        useremail=request.POST.get('useremail')
        userpass=request.POST.get('userpass')
        data=userdata(username=username,useremail=useremail,userpass=userpass,userphoto=userphoto,id=id)
        data.save()
        return redirect(userprofileview)
    return render(request, "userprofileupdate.html")


def adminstaffupdate(request,id):
    if request.method=="POST":
        staffphoto=request.FILES['staffphoto']
        up=FileSystemStorage()
        img=up.save(staffphoto.name,staffphoto)
        staffname=request.POST.get('staffname')
        staffspec=request.POST.get('staffspec')
        data=staffdetails(staffname=staffname,staffspec=staffspec,staffphoto=staffphoto,id=id)
        data.save()
        return redirect(adminstaffview)
    return render(request,"adminstaffupdate.html")

def adminstaffupdates(request,id):
    mark=staffdetails.objects.get(pk=id)
    return render(request, "adminstaffupdate.html",{'result':mark})


def adminclassupdate(request,id):
    if request.method=="POST":
        staffnames=request.POST.get('staffnames')
        staffspecs=request.POST.get('staffspecs')
        classtime=request.POST.get('classtime')
        classdate=request.POST.get('classdate')
        data=classdetails(staffnames=staffnames,staffspecs=staffspecs,classtime=classtime,classdate=classdate,id=id)
        data.save()
        return redirect(adminclassview)
    return render(request,"adminclassupdate.html")


def adminclassupdates(request,id):
    data1=classdetails.objects.get(pk=id)
    return render(request,"adminclassupdate.html",{'result':data1})


def adminequpdate(request,id):
    if request.method=="POST":
        eqphoto=request.FILES['eqphoto']
        up=FileSystemStorage()
        img=up.save(eqphoto.name,eqphoto)
        eqname=request.POST.get('eqname')
        data=eqdetails(eqname=eqname,eqphoto=eqphoto,id=id)
        data.save()
        return redirect(adminviewequip)
    return render(request, "adminequpdate.html")

def adminequpdates(request,id):
    data1=eqdetails.objects.get(pk=id)
    return render(request,"adminequpdate.html",{'result':data1})


def adminstaffdelete(request,id):
    mark=staffdetails.objects.get(pk=id)
    mark.delete()
    return redirect(adminstaffview) 

def adminclassdelete(request,id):
    mark=classdetails.objects.get(pk=id)
    mark.delete()
    return redirect(adminclassview) 

def userclassenrolldelete(request,id):
    mark=enrollclass.objects.get(pk=id)
    mark.delete()
    return redirect(enrollclassview)

def admineqdelete(request,id):
    mark=eqdetails.objects.get(pk=id)
    mark.delete()
    return redirect(adminviewequip) 

def adminuserdelete(request,id):
    mark=userdata.objects.get(pk=id)
    mark.delete()
    return redirect(adminuserlist) 

def usereqbookdelete(request,id):
    mark=eqbook.objects.get(pk=id)
    mark.delete()
    return redirect(usereqbookview)

def adminclassbookingdelete(request,id):
    mark=enrollclass.objects.get(pk=id)
    mark.delete()
    return redirect(classbookingsview) 

def admineqbookdelete(request,id):
    mark=eqbook.objects.get(pk=id)
    mark.delete()
    return redirect(admineqbookview) 

def adminfeedbackdelete(request,id):
    mark=feedbacks.objects.get(pk=id)
    mark.delete()
    return redirect(adminfeedbackview) 


