from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from . models import *  
from . forms import *


# Create your views here.
def home(request):
	template = 'index.html'
	context_dict = {}
	return render(request, template, context_dict)

def refresh_application(request):
    tertiary_details = TertiaryDetails()
    template = 'website/applications/tertiary-details.html'
    context_dict = { 'tertiary_details': tertiary_details }
    return render(request, template, context_dict)

def submit_application(request):
    primary_details = PrimaryDetails()
    secondary_details = SecondaryDetails()
    tertiary_details = TertiaryDetails()
    combine_form = CombineForm()
    context_dict = {}
    template = 'website/applications/form.html'
    if request.method == 'GET' and 'submit' in request.GET:
        # print request.GET
        first_name = request.GET.get('first_name')
        first_name = first_name.upper()
        last_name = request.GET.get('last_name')
        last_name = last_name.upper()

        # referred_by = request.GET.get('referred_by')
        position_applied = request.GET.get('position_applied')
        application_source = request.GET.get('application_source')
        availability = request.GET.get('availability')
        us_visa = request.GET.get('us_visa')
        present_company = request.GET.get('present_company')
        vessel_type = request.GET.get('vessel_type')
        principal = request.GET.get('principal')
        request.GET = request.GET.copy()
        if position_applied:
            try:
                id = Position.objects.filter(id=position_applied)
                # if not position_id:
                #     pass
                    # position = Position.objects.get_or_create(position=position_applied)
                    # if position:
                    #     pass
                        # request.GET['position_applied'] = position[0].id

            except:
                instance = Position.objects.get_or_create(position=position_applied)
                request.GET['position_applied'] = instance[0].id
                #! NOTE: Email makes the system slow, must find alternative
                # send_mail('Sample subject', 'Sample Message', settings.EMAIL_HOST_USER, ['armadadean@yahoo.com'])
        if application_source:
            try:
                instance_id = AppSource.objects.filter(id=application_source)
            except:
                instance = AppSource.objects.get_or_create(source=application_source)
                request.GET['application_source'] = instance[0].id
        if availability:
            try:
                instance_id = Availability.objects.filter(id=availability)
            except:
                instance = Availability.objects.get_or_create(availability=availability)
                request.GET['availability'] = instance[0].id
        if us_visa:
            try:
                instance_id = USVisa.objects.filter(id=us_visa)
            except:
                instance = USVisa.objects.get_or_create(visa=us_visa)
                request.GET['us_visa'] = instance[0].id
        if present_company:
            try:
                instance_id = Company.objects.filter(id=present_company)
            except:
                instance = Company.objects.get_or_create(company=present_company)
                request.GET['present_company'] = instance[0].id
        if vessel_type:
            try:
                instance_id = VType.objects.filter(id=vessel_type)
            except:
                instance = VType.objects.get_or_create(vessel_type=vessel_type)
                request.GET['vessel_type'] = instance[0].id
        if principal:
            try:
                instance_id = Principal.objects.filter(id=principal)
            except:
                instance = Principal.objects.get_or_create(principal=principal)
                request.GET['principal'] = instance[0].id         


        primary_details = PrimaryDetails(request.GET)
        secondary_details = SecondaryDetails(request.GET)
        tertiary_details = TertiaryDetails(request.GET)
        combine_form = CombineForm(request.GET)
        if primary_details.is_valid() and secondary_details.is_valid() and tertiary_details.is_valid():
            a = combine_form.save(commit=False)

            a.name = last_name+", "+first_name
            date = datetime.date.today()
            date = Date.objects.get_or_create(date=date)
            a.application_date = date[0]
            try:
                a.save()
            except:
                return HttpResponse("Duplicate Name <button class='btn btn-success submit-another'>Submit Another Application</button>")   
            return HttpResponse("Thank you for applying in Manship <button class='btn btn-success submit-another'>Submit Another Application</button>")
        else:
            print primary_details.errors, secondary_details.errors, tertiary_details.errors
            context_dict = { 'primary_details': primary_details, 'secondary_details': secondary_details,
                    'tertiary_details': tertiary_details }
            return render(request, template, context_dict)
            # return HttpResponse("2")
    else:
        # print request.GET
        context_dict = { 'primary_details': primary_details, 'secondary_details': secondary_details,
                    'tertiary_details': tertiary_details }
        return render(request, template, context_dict)
        # return HttpResponse("3")

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