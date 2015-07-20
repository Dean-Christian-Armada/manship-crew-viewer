from django.contrib import admin
from import_export import resources, widgets, fields
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class DateResource(resources.ModelResource):
	class Meta:
		model = Date

class AgeResource(resources.ModelResource):
	class Meta:
		model = Age

class USVisaResource(resources.ModelResource):
	class Meta:
		model = USVisa

class VTypeResource(resources.ModelResource):
	class Meta:
		model = VType

class AvailabilityResource(resources.ModelResource):
	class Meta:
		model = Availability

class AppSourceResource(resources.ModelResource):
	class Meta:
		model = AppSource

class CESResource(resources.ModelResource):
	class Meta:
		model = CES

# class TimeNumResource(resources.ModelResource):
# 	class Meta:
# 		model = TimeNum

class StAtResource(resources.ModelResource):
	class Meta:
		model = StAt

class PrincipalResource(resources.ModelResource):
	class Meta:
		model = Principal

class ApplicationResource(resources.ModelResource):
	present_company = fields.Field(column_name='present_company', attribute='present_company', widget=widgets.ForeignKeyWidget(Company, 'company', ))
	application_date = fields.Field(column_name='application_date', attribute='application_date', widget=widgets.ForeignKeyWidget(Date, 'date', ))
	age = fields.Field(column_name='age', attribute='age', widget=widgets.ForeignKeyWidget(Age, 'age', ))
	us_visa = fields.Field(column_name='us_visa', attribute='us_visa', widget=widgets.ForeignKeyWidget(USVisa, 'visa', ))
	vessel_type = fields.Field(column_name='vessel_type', attribute='vessel_type', widget=widgets.ForeignKeyWidget(VType, 'vessel_type', ))
	time_indicator = fields.Field(column_name='time_indicator', attribute='time_indicator', widget=widgets.ForeignKeyWidget(TimeIndicator, 'indicator', ))	
	availability = fields.Field(column_name='availability', attribute='availability', widget=widgets.ForeignKeyWidget(Availability, 'availability', ))	
	application_source = fields.Field(column_name='application_source', attribute='application_source', widget=widgets.ForeignKeyWidget(AppSource, 'source', ))	
	ces = fields.Field(column_name='ces', attribute='ces', widget=widgets.ForeignKeyWidget(CES, 'ces', ))
	st_at = fields.Field(column_name='st_at', attribute='st_at', widget=widgets.ForeignKeyWidget(StAt, 'st_at', ))
	principal = fields.Field(column_name='principal', attribute='principal', widget=widgets.ForeignKeyWidget(Principal, 'principal', ))
	position_applied = fields.Field(column_name='position_applied', attribute='position_applied', widget=widgets.ForeignKeyWidget(Position, 'position', ))

	class Meta:
		model = Application

		exclude = ('date_added', 'date_modified', 'IsActive')

class CompanyResource(resources.ModelResource):
	class Meta:
		model = Company

class PositionResource(resources.ModelResource):
	class Meta:
		model = Position

class DateImport(ImportExportModelAdmin):
	resource_class = DateResource

class AgeImport(ImportExportModelAdmin):
	resource_class = AgeResource

class USVisaImport(ImportExportModelAdmin):
	resource_class = USVisaResource

class VTypeImport(ImportExportModelAdmin):
	resource_class = VTypeResource

class AvailabilityImport(ImportExportModelAdmin):
	resource_class = AvailabilityResource

class AppSourceImport(ImportExportModelAdmin):
	resource_class = AppSourceResource

class CESImport(ImportExportModelAdmin):
	resource_class = CESResource

class CompanyImport(ImportExportModelAdmin):
	resource_class = CompanyResource

# class TimeNumImport(ImportExportModelAdmin):
# 	resource_class = TimeNumResource

class StAtImport(ImportExportModelAdmin):
	resource_class = StAtResource

class PrincipalImport(ImportExportModelAdmin):
	resource_class = PrincipalResource

class ApplicationImport(ImportExportModelAdmin):
	resource_class = ApplicationResource

class PositionImport(ImportExportModelAdmin):
	resource_class = PositionResource

class ApplicationAdmin(admin.ModelAdmin):
	readonly_fields = ('date_added', 'date_modified')
	list_per_page = 15
	list_display = ('name', 'application_date', 'position_applied', 'age', 'us_visa', 'vessel_type', 
				     'years_rank', '_gross_tonnage', '_contact_number', 
				     'present_company', 'availability', 'application_source', 'ces', 'interview_1', 
				     'interview_2', 'interview_3', 'st_at', 'principal', 'remarks', 'IsActive')
	search_fields = ('name', 'contactnumber')

admin.site.register(Position, PositionImport)
admin.site.register(Company, CompanyImport)
admin.site.register(Date, DateImport)
admin.site.register(Age, AgeImport)
admin.site.register(USVisa, USVisaImport)
admin.site.register(VType, VTypeImport)
admin.site.register(Availability, AvailabilityImport)
admin.site.register(AppSource, AppSourceImport)
admin.site.register(CES, CESImport)
admin.site.register(TimeIndicator)
# admin.site.register(TimeNum, TimeNumImport)
admin.site.register(StAt, StAtImport)
admin.site.register(Principal, PrincipalImport)
# admin.site.register(Application, ApplicationImport)
admin.site.register(Application, ApplicationAdmin)
# admin.site.register(Publication)
# admin.site.register(Article)