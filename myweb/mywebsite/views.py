from django.shortcuts import render
from django.http import HttpResponse
from .models import project, skill, Contact
# Create your views here.


def index(request):

    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        msg = request.POST.get('msg', '')
        print(name,email,msg)

        contact = Contact(name=name, email=email, msg=msg)
        contact.save()

        projects = project.objects.all()
        skills = skill.objects.all()
        params = {'project': projects, 'skill': skills}

        return render(request, 'myweb/index.html', params)

    else:
        projects = project.objects.all()
        skills = skill.objects.all()
        params = {'project': projects, 'skill': skills}
        return render(request, 'myweb/index.html', params)



