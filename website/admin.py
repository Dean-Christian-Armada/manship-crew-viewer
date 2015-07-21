from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from import_export import resources, widgets, fields
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class Variables(object):
	AppObject = Application.objects

class PositionFilter(admin.SimpleListFilter, Variables):
	title = _('Positions Applied')
	parameter_name = 'position'

	def lookups(self, request, model_admin):
		us_visa = request.GET.get('us_visa')
		vessel_type = request.GET.get('vessel_type')	
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('position_applied__position')
		return distinct.values_list('position_applied__position', 'position_applied__position')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(position_applied__position__exact=param)

class USVisaFilter(admin.SimpleListFilter, Variables):
	title = _('US Visa')
	parameter_name = 'us_visa'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		vessel_type = request.GET.get('vessel_type')		
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('us_visa__visa')
		return distinct.values_list('us_visa__visa', 'us_visa__visa')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(us_visa__visa__exact=param)

class VesselTypeFilter(admin.SimpleListFilter, Variables):
	title = _('Vessel Type')
	parameter_name = 'vessel_type'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('vessel_type__vessel_type')
		return distinct.values_list('vessel_type__vessel_type', 'vessel_type__vessel_type')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(vessel_type__vessel_type__exact=param)

class AvailabilityFilter(admin.SimpleListFilter, Variables):
	title = _('Availability')
	parameter_name = 'availability'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('availability__availability')
		return distinct.values_list('availability__availability', 'availability__availability')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(availability__availability__exact=param)

class AppSourceFilter(admin.SimpleListFilter, Variables):
	title = _('Application Source')
	parameter_name = 'app_source'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		availability = request.GET.get('availability')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('application_source__source')
		return distinct.values_list('application_source__source', 'application_source__source')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(application_source__source__exact=param)

class PrincipalFilter(admin.SimpleListFilter, Variables):
	title = _('Principal')
	parameter_name = 'principal'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('principal__principal')
		return distinct.values_list('principal__principal', 'principal__principal')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(principal__principal__exact=param)

class IsActiveFilter(admin.SimpleListFilter, Variables):
	title = _('Is Active')
	parameter_name = 'is_active'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('IsActive')
		return distinct.values_list('IsActive', 'IsActive')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(IsActive__exact=param)

class AgeFilter(admin.SimpleListFilter):
	title = _('Age')
	parameter_name = 'age'
	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		time_indicator = request.GET.get('time_indicator')
		length_rank = request.GET.get('length_rank')
		ages = []
		choices = []

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if time_indicator or time_indicator == '':
			app = app.filter(time_indicator__indicator__exact=time_indicator)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		else:
			pass
		distinct = app.distinct().order_by('age__age')
		for distincts in distinct:
			ages.append(distincts.age.age)
		ages = set(ages)
		ages = list(ages)
		if 18 in ages:
			choices.append((18, 18))
		if 19 in ages:
			choices.append((19, 19))
		for y in range(20, 30):
			if y in ages:
				choices.append((20, "20's"))
		for y in range(30, 40):
			if y in ages:
				choices.append((30, "30's"))
		for y in range(40, 50):
			if y in ages:
				choices.append((40, "40's"))
		for y in range(50, 60):
			if y in ages:
				choices.append((50, "50's"))
		for y in range(60, 70):
			if y in ages:
				choices.append((60, "60's"))
		for y in range(70, 80):
			if y in ages:
				choices.append((70, "70's"))
		choices = set(choices)
		choices = list(choices)
		choices = sorted(choices)
		return choices

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			print int(param)
			if int(param) < 20:
				return queryset.filter(age__age__exact=param)				
			else:
				param_limiter = int(param)+10-1
				return queryset.filter(age__age__gte=param, age__age__lte=param_limiter)

class TimeIndicatorFilter(admin.SimpleListFilter, Variables):
	title = _('Time Indicator')
	parameter_name = 'time_indicator'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		length_rank = request.GET.get('length_rank')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if length_rank or length_rank == '':
			app = app.filter(num_years_rank=length_rank)
		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

		distinct = app.distinct().order_by('time_indicator__indicator')
		return distinct.values_list('time_indicator__indicator', 'time_indicator__indicator')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(time_indicator__indicator__exact=param)

class LengthRankFilter(admin.SimpleListFilter, Variables):
	title = _('Length Rank')
	parameter_name = 'length_rank'

	def lookups(self, request, model_admin):
		position = request.GET.get('position')
		us_visa = request.GET.get('us_visa')	
		vessel_type = request.GET.get('vessel_type')
		availability = request.GET.get('availability')
		app_source = request.GET.get('app_source')
		principal = request.GET.get('principal')
		is_active = request.GET.get('is_active')
		age = request.GET.get('age')
		time_indicator = request.GET.get('time_indicator')

		app = Variables.AppObject
		if position or position == '':
			app = app.filter(position_applied__position__exact=position)
		if us_visa or us_visa == '':
			app = app.filter(us_visa__visa__exact=us_visa)
		if vessel_type or vessel_type == '':
			app = app.filter(vessel_type__vessel_type__exact=vessel_type)
		if availability or availability == '':
			app = app.filter(availability__availability__exact=availability)
		if app_source or app_source == '':
			app = app.filter(application_source__source__exact=app_source)
		if principal or principal == '':
			app = app.filter(principal__principal__exact=principal)
		if is_active or is_active == '':
			app = app.filter(is_active__exact=is_active)
		if time_indicator or time_indicator == '':
			if time_indicator != 'N/A':
				app = app.filter(time_indicator__indicator__exact=time_indicator)
				distinct = app.distinct().order_by('num_years_rank')
				return distinct.values_list('num_years_rank', 'num_years_rank')

		if age:
			if age < 20:
				app = app.filter(age__age__exact=age)
			else:
				age_limiter = int(age)+10-1
				app = app.filter(age__age__gte=age, age__age__lte=age_limiter)
		else:
			pass

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(num_years_rank=param)

class ApplicationAdmin(admin.ModelAdmin):
	readonly_fields = ('date_added', 'date_modified')
	list_per_page = 15
	list_display = ('name', 'application_date', 'position_applied', 'age', 'us_visa', 'vessel_type', 
				     'years_rank', '_gross_tonnage', '_contact_number', 
				     'present_company', 'availability', 'application_source', 'ces', 'interview_1', 
				     'interview_2', 'interview_3', 'st_at', 'principal', 'remarks', 'IsActive')
	search_fields = ('name', 'present_company__company', 'remarks')
	list_filter = (PositionFilter, USVisaFilter, VesselTypeFilter, AvailabilityFilter, 
					AppSourceFilter, PrincipalFilter, IsActiveFilter, AgeFilter, 
					TimeIndicatorFilter, LengthRankFilter)

	# list_filter = (TimeIndicatorFilter, NumLengthRankFilter)


admin.site.register(Application, ApplicationAdmin)
# admin.site.register(Publication)
# admin.site.register(Article)