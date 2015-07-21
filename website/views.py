from django.shortcuts import render
from django.db.models import Q
from . models import Application

# Create your views here.
def home(request):
	template = 'index.html'
	context_dict = {}
	return render(request, template, context_dict)

def navigation_autocomplete(request):
    q = request.GET.get('q', '')
    us_visa = '' 
    position = ''
    vessel_type = '' 
    availability = '' 
    app_source = '' 
    principal = '' 
    is_active = '' 
    age = '' 
    time_indicator = '' 
    length_rank = '' 

    if q:
        name = Q(name__icontains=q)
        company = Q(present_company__company__icontains=q)
        remarks = Q(remarks__icontains=q)
        
        applications = Application.objects.filter(
            name |
            company |
            remarks
        ).distinct() 

        if request.GET.get('us_visa'):
        	us_visa = request.GET.get('us_visa')
        	applications = applications.filter(us_visa__visa=us_visa)
        if request.GET.get('position'):
            position = request.GET.get('position')
            applications = applications.filter(position_applied__position=position)
        if request.GET.get('vessel_type'):
            vessel_type = request.GET.get('vessel_type')
            applications = applications.filter(vessel_type__vessel_type=vessel_type)
        if request.GET.get('availability'):
            availability = request.GET.get('availability')
            applications = applications.filter(availability__availability=availability)
        if request.GET.get('app_source'):
            app_source = request.GET.get('app_source')
            applications = applications.filter(application_source__source=app_source)
        if request.GET.get('principal'):
            principal = request.GET.get('principal')
            applications = applications.filter(principal__principal=principal)
        if request.GET.get('is_active'):
            is_active = request.GET.get('is_active')
            applications = applications.filter(is_active=is_active)
        if request.GET.get('age'):
            age = request.GET.get('age')
            if age < 20:
            	applications = applications.filter(age__age=age)
            else:
            	age_limiter = int(age)+10-1
            	applications = applications.filter(age__age__gte=age, age__age__lte=age_limiter)
        if request.GET.get('time_indicator'):
            time_indicator = request.GET.get('time_indicator')
            applications = applications.filter(time_indicator__indicator=time_indicator)
        if request.GET.get('length_rank'):
            length_rank = request.GET.get('length_rank')
            applications = applications.filter(num_years_rank=length_rank)

        template='website/applications/autocomplete.html'
        context_dict = {'applications': applications}
        return render(request, template, context_dict)
    else:
        pass