from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from urllib.parse import urlencode
from django.contrib import messages
from .models import Sessions
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def get_details(request):
	# if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/login/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})


def index(request):
	return render(request, 'login/index.html')

def login(request):
	add = request.GET.get('add')
	form = UserForm()
	session = Sessions.objects.all().first()
	if(session.user == "1"):
		return redirect('loan_admin:index')
	if(session.user == "2"):
		return redirect('loan_officer:index')
	if(add):
		messages.info(request, 'Password incorrect')
	context = {'form':form}
	return render(request, 'login/login.html', context)

@require_POST
def authenticate_and_redirect(request):
	arr = ['', 'Admin', 'Officer']
	print(request.POST)
	user = authenticate(username=arr[int(request.POST['name'])], password=request.POST['password'])
	if user is not None:
		name = request.POST['name']
		ins = Sessions.objects.all().first()
		if(ins is None):
			new = Sessions(user=name)
			new.save()
		else:
			ins.user = name
			ins.save()
		if name is '1':
			return redirect(reverse('loan_admin:index'))
		if name is '2':
			return redirect('loan_officer:index')
	else:
		base_url = reverse('login:login')
		query_string =  urlencode({'add': 'invalid'})
		url = '{}?{}'.format(base_url, query_string)
		return redirect(url)

def logout(request):
	ins = Sessions.objects.all().first()
	ins.user = "None"
	ins.save()
	return redirect('login:login')
