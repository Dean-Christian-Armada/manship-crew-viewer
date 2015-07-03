from django.shortcuts import render

# Create your views here.
def home(request):
	template = 'index.html'
	context_dict = {}
	return render(request, template, context_dict)