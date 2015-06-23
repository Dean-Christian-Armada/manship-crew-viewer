from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	context_dict = {}
	template = 'index.html'
	return render(request, template, context_dict)