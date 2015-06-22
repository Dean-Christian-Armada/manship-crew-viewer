from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context_dict = {}
	template = 'crew/index.html'
	return render(request, template, context_dict)

def bio(request):
	context_dict = {}
	template = 'crew/bio.html'
	return render(request, template, context_dict)

def ranks(request):
	context_dict = {}
	template = 'crew/ranks.html'
	return render(request, template, context_dict)

def certificate(request):
	context_dict = {}
	template = 'crew/certificate.html'
	return render(request, template, context_dict)

def principals(request):
	context_dict = {}
	template = 'crew/principals.html'
	return render(request, template, context_dict)

def service(request):
	context_dict = {}
	template = 'crew/service.html'

	return render(request, template, context_dict)