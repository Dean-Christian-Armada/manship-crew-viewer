import urlparse
import urllib2
# import os
# from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from . models import Bio, Cert, Contract, Country, Doc, Principal, Rank, Service, Vessel, Vtype
# from django.contrib.admin.helpers import ActionForm
# from crew_viewer.middlewares import AdminMiddleWare


# Register your models here.

class Variables(object):
	BioObject = Bio.objects

class PrincipalFilter(admin.SimpleListFilter, Variables):
	title = _('Principal')
	parameter_name = 'principal'

	def lookups(self, request, model_admin):
		vessel_type = request.GET.get('vessel_type')
		# vessel_type = Variables.RequestVariables()
		rank = request.GET.get('rank')
		last_vessel = request.GET.get('last_vessel')
		status = request.GET.get('status')
		principal = request.GET.get('principal')

		bio = Variables.BioObject
		if vessel_type or vessel_type == '':
			bio = bio.filter(last_vessel__vessel_type__exact=vessel_type)
		if last_vessel or last_vessel == '':
			bio = bio.filter(last_vessel__exact=last_vessel)
		if rank or rank == '':
			bio = bio.filter(rank__exact=rank)
		if status or status == '':
			bio = bio.filter(status__exact=status)
		else:
			pass

		distinct = bio.distinct().order_by('last_vessel__principal')
		return distinct.values_list('last_vessel__principal', 'last_vessel__principal')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(last_vessel__principal__exact=param)

class VesselTypeFilter(admin.SimpleListFilter, Variables):
	title = _('Vessel Type')
	parameter_name = 'vessel_type'

	def lookups(self, request, model_admin):
		vessel_type = request.GET.get('vessel_type')
		rank = request.GET.get('rank')
		last_vessel = request.GET.get('last_vessel')
		status = request.GET.get('status')
		principal = request.GET.get('principal')

		bio = Variables.BioObject
		if principal:
			bio = bio.filter(last_vessel__principal__exact=principal)
		if last_vessel or last_vessel == '':
			bio = bio.filter(last_vessel__exact=last_vessel)
		if rank or rank == '':
			bio = bio.filter(rank__exact=rank)
		if status or status == '':
			bio = bio.filter(status__exact=status)
		else:
			pass

		distinct = bio.distinct().order_by('last_vessel__vessel_type')
		return distinct.values_list('last_vessel__vessel_type', 'last_vessel__vessel_type')
	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(last_vessel__vessel_type__exact=param)

class LastVesselFilter(admin.SimpleListFilter, Variables):
	title = _('Last Vessel')
	parameter_name = 'last_vessel'

	def lookups(self, request, model_admin):
		vessel_type = request.GET.get('vessel_type')
		rank = request.GET.get('rank')
		last_vessel = request.GET.get('last_vessel')
		status = request.GET.get('status')
		principal = request.GET.get('principal')

		bio = Variables.BioObject
		if principal:
			bio = bio.filter(last_vessel__principal__exact=principal)
		if vessel_type or vessel_type == '':
			bio = bio.filter(last_vessel__vessel_type__exact=vessel_type)
		if rank or rank == '':
			bio = bio.filter(rank__exact=rank)
		if status or status == '':
			bio = bio.filter(status__exact=status)
		else:
			pass

		distinct = bio.distinct().order_by('last_vessel')
		return distinct.values_list('last_vessel', 'last_vessel')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(last_vessel__exact=param)

class RankFilter(admin.SimpleListFilter, Variables):
	title = _('Rank')
	parameter_name = 'rank'

	def lookups(self, request, model_admin):
		vessel_type = request.GET.get('vessel_type')
		rank = request.GET.get('rank')
		last_vessel = request.GET.get('last_vessel')
		status = request.GET.get('status')
		principal = request.GET.get('principal')

		bio = Variables.BioObject
		if principal:
			bio = bio.filter(last_vessel__principal__exact=principal)
		if vessel_type or vessel_type == '':
			bio = bio.filter(last_vessel__vessel_type__exact=vessel_type)
		if last_vessel or last_vessel == '':
			bio = bio.filter(last_vessel__exact=last_vessel)
		if status or status == '':
			bio = bio.filter(status__exact=status)
		else:
			pass

		distinct = bio.distinct().order_by('rank')
		return distinct.values_list('rank', 'rank')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(rank__exact=param)

class StatusFilter(admin.SimpleListFilter, Variables):
	title = _('Status')
	parameter_name = 'status'

	def lookups(self, request, model_admin):
		vessel_type = request.GET.get('vessel_type')
		rank = request.GET.get('rank')
		last_vessel = request.GET.get('last_vessel')
		status = request.GET.get('status')
		principal = request.GET.get('principal')

		bio = Variables.BioObject
		if principal:
			bio = bio.filter(last_vessel__principal__exact=principal)
		if vessel_type or vessel_type == '':
			bio = bio.filter(last_vessel__vessel_type__exact=vessel_type)
		if last_vessel or last_vessel == '':
			bio = bio.filter(last_vessel__exact=last_vessel)
		if rank or rank == '':
			bio = bio.filter(rank__exact=rank)
		else:
			pass

		distinct = bio.distinct().order_by('status')
		return distinct.values_list('status', 'status')

	def queryset(self, request, queryset):
		param = self.value()
		if param or param == '':
			return queryset.filter(status__exact=param)

class ResetFilter(admin.SimpleListFilter):
	title = _('Reset')
	parameter_name = ''
	template = 'admin/reset_filter.html'

	def lookups(self, request, model_admin):
		return (( '', '' ),( '', '' ))

	def queryset(self, request, queryset):
		pass

# To enable the List Per Page Request
class ListPerPage(admin.SimpleListFilter):
	title = _('List Per Page')
	parameter_name = 'list_per_page'

	def lookups(self, request, model_admin):
		pass

	def queryset(self, request, queryset):
		pass

# class UpdateActionForm(ActionForm):
# 	LIST_PAGE_CHOICES = (
# 			(15, 15),
# 			(25, 25),
# 			(50, 50),
# 			(100, 100),
# 		)
# 	List_Per_Page = forms.ChoiceField(choices=LIST_PAGE_CHOICES)

class BioAdmin(admin.ModelAdmin):
	# def list_page(modeladmin, request, queryset):
	# 	price = request.POST['price']
	# 	price = int(price)
	# 	# queryset.update(price=price)

	list_display = ('code', 'name', 'rank', 'principal', 'status', 
				'last_vessel', 'vessel_type', 'view_info', 'view_picture')
	# list_filter = ('last_vessel__principal', 'last_vessel__vessel_type','last_vessel', 'rank', 'status', ResetFilter)
	list_filter = (ListPerPage, PrincipalFilter, VesselTypeFilter, LastVesselFilter, RankFilter, StatusFilter, ResetFilter)

	list_per_page = 15
	# list_max_show_all = 200;

	search_fields = ('first_name', 'middle_name', 'last_name', 'code')
	# action_form = UpdateActionForm
	# actions = [list_page]

	# Removes the link of the object to update or edit
	def __init__(self, *args, **kwargs):
		super(BioAdmin, self).__init__(*args, **kwargs)
		self.list_display_links = (None, )

	# Removes boolean deleted records
	def get_queryset(self, request):
		# if request.method == 'GET':
		# 	dean = request.GET.get('list_per_page')
		# 	if dean:
		# 		print 'dean'
		# 		# list_per_page = 30
		# 		setattr(BioAdmin, 'list_per_page', 50)
		# 	else:
		# 		print 'armada'
		# 		setattr(BioAdmin, 'list_per_page', 100)

		qs = super(BioAdmin, self).get_queryset(request)
		return qs.filter(b_d='')

	# def __call__(self, request, url):
	# 	print 'Deanasdasdzcxxzc'

	# Removes adding button and function
	def has_add_permission(self, request):
		return False

admin.site.register(Bio, BioAdmin)
# Removes the get actions dropdown select above the table
admin.site.disable_action('delete_selected')