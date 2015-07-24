from django import forms
from .models import Application

class PrimaryDetails(forms.ModelForm):
	first_name = forms.CharField(max_length=50, label='First Name')
	last_name = forms.CharField(max_length=50, label='Last Name')
	class Meta:
		model = Application
		fields = ('first_name', 'last_name', 'contact_number')

class SecondaryDetails(forms.ModelForm):
	SAMPLE_CHOICES = (
		('Person 1', 'Person 1'),
		('Person 2', 'Person 2'),
		('Person 3', 'Person 3'),
	)
	referred_by = forms.ChoiceField(choices=SAMPLE_CHOICES)
	class Meta:
		model = Application
		fields = ('num_years_rank', 'time_indicator', 'age', 'referred_by', 'gross_tonnage')

class TertiaryDetails(forms.ModelForm):
	class Meta:
		model = Application
		fields = ('position_applied', 'application_source', 'availability', 'us_visa', 'present_company',
				'vessel_type', 'principal')

class CombineForm(forms.ModelForm):
	# include = PrimaryDetails, SecondaryDetails, TertiaryDetails
	class Meta:
		model = Application
		exclude = ('name', 'st_at', 'application_date', 'ces', 'interview_1', 'interview_2', 'interview_3')




# class ApplicationForm(forms.ModelForm):
# 	first_name = forms.CharField(max_length=50, label='First Name')
# 	last_name = forms.CharField(max_length=50, label='Last Name')
# 	class Meta:
# 		model = Application
# 		fields = ('first_name', 'last_name', 'contact_number', 'gross_tonnage', 'present_company', 'age', 'us_visa', 
# 			'vessel_type', 'num_years_rank', 'time_indicator', 'availability', 'application_source',
# 			'position_applied', 'principal')

		# def __init__(self, *args, **kwargs):
		# 	super(ApplicationForm, self).__init__(*args, **kwargs)
		# 	self.fields['']