from django.contrib import admin
from django.contrib.admin.filters import AllValuesFieldListFilter
from . models import Bio, Cert, Contract, Country, Doc, Principal, Rank, Service, Vessel, Vtype
# Register your models here.

# class DropdownFilter(AllValuesFieldListFilter):
# 	template = 'admin/filter.html'

class BioAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'rank', 'principal', 'status', 
				'last_vessel', 'vessel_type', 'view_info', 'view_picture') 
	# list_filter = ('principal', 'vessel_type', 'vessel', 'rank', 'status')
	# list_filter = (('status', DropdownFilter), ('rank', DropdownFilter))
	list_per_page = 15;
	list_max_show_all = 100;

	search_fields = ('name', 'code')

	# Removes the link of the object to update or edit
	def __init__(self, *args, **kwargs):
		super(BioAdmin, self).__init__(*args, **kwargs)
		self.list_display_links = (None, )

	# Removes adding button and function
	def has_add_permission(self, request):
		return False

	# Removes the get actions dropdown select above the table
	def get_actions(self, request):
		actions = super(BioAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions

admin.site.register(Bio, BioAdmin)