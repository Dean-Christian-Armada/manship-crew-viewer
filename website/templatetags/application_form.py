from django import template
from website.models import Application
from website.forms import *

register = template.Library()

@register.inclusion_tag('website/applications/form.html', takes_context=True)
def app_form(context):
	request = context['request']
	primary_details = PrimaryDetails()
	secondary_details = SecondaryDetails()
	tertiary_details = TertiaryDetails()
	if request.method == 'POST':
		primary_details = PrimaryDetails(request.POST)
		secondary_details = SecondaryDetails(request.POST)
		tertiary_details = TertiaryDetails(request.POST)
		if primary_details.is_valid() and secondary_details.is_valid() and tertiary_details.is_valid():
			pass
		else:
			print primary_details.errors, secondary_details.errors, tertiary_details.errors
	context_dict = { 'primary_details': primary_details, 'secondary_details': secondary_details,
					'tertiary_details': tertiary_details }
	return context_dict