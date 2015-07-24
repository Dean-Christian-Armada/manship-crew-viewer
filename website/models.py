from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
import re, datetime
# Create your models here.

class Date(models.Model):
	date = models.DateField(unique=True)

	def __str__(self):
		return str(self.date)

class Age(models.Model):
	age = models.IntegerField(unique=True)

	def __str__(self):
		return str(self.age)

class USVisa(models.Model):
	visa = models.CharField(max_length=6, null=True, default='NONE', unique=True)

	def __str__(self):
		return self.visa

class VType(models.Model):
	vessel_type = models.CharField(max_length=50, null=True, unique=True)

	def __str__(self):
		return self.vessel_type

class Availability(models.Model):
	availability = models.CharField(max_length=10, default='Anytime', unique=True)

	def __str__(self):
		return self.availability

class AppSource(models.Model):
	source = models.CharField(max_length=30, null=True, unique=True)

	def __str__(self):
		return self.source

class CES(models.Model):
	ces = models.CharField(max_length=3, null=True, unique=True)

	def __str__(self):
		return self.ces

class TimeIndicator(models.Model):
	indicator = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.indicator

class StAt(models.Model):
	st_at = models.CharField(max_length=3, null=True, unique=True)

	def __str__(self):
		return self.st_at

class Principal(models.Model):
	principal = models.CharField(max_length=10, null=True, unique=True)

	def __str__(self):
		return self.principal

class Company(models.Model):
	company = models.CharField(max_length=50, null=True, unique=True)

	def __str__(self):
		return self.company

class Position(models.Model):
	position = models.CharField(max_length=10, null=True, unique=True)

	def __str__(self):
		return self.position

class Application(models.Model):
	INTERVIEW_CHOICES = (
		('-', '-'),
		('N/A', 'N/A'),
		('A', 'A'),
		('P', 'P'),
		('X', 'X'),
	)
	name = models.CharField(max_length=100, unique=True)
	# to be formatted by thousand seperators - https://www.python.org/dev/peps/pep-0378/
	gross_tonnage = models.IntegerField(default=None, verbose_name="Gross Tonnage")
	# to be seperated by hyphen(mobile format) - http://stackoverflow.com/questions/5254445/add-string-in-a-certain-position-in-python
	contact_regex = RegexValidator(regex=r'^([0-9]{7}|[0-9]{11})$', message="Telephone and Mobile Numbers are only allowed")
	contact_number = models.CharField(max_length=15, validators=[contact_regex], default=None, null=True, blank=True, verbose_name="Contact Number")
	remarks = models.TextField(null=True, blank=True)
	date_added = models.DateField(auto_now_add=True, editable=False, null=True)
	date_modified = models.DateTimeField(editable=False, null=True)
	IsActive = models.BooleanField(default=True)
	present_company = models.ForeignKey('Company', default=None, verbose_name='Present Company')
	application_date = models.ForeignKey('Date', verbose_name='Application Date')
	age = models.ForeignKey('Age')
	us_visa = models.ForeignKey('USVisa', verbose_name='US Visa')
	vessel_type = models.ForeignKey('Vtype', verbose_name='Vessel Type')
	num_years_rank = models.FloatField(default=None, validators=[ MinValueValidator(0) ])
	time_indicator = models.ForeignKey('TimeIndicator', default=1, verbose_name='Time Indicator')
	availability = models.ForeignKey('Availability')
	application_source = models.ForeignKey('AppSource', verbose_name='Application Source')
	position_applied = models.ForeignKey('Position', default=None, verbose_name='Position Applied')
	ces = models.ForeignKey('CES', default=1, verbose_name='CES')
	st_at = models.ForeignKey('StAt', default=4)
	principal = models.ForeignKey('Principal')
	interview_1 = models.CharField(max_length=5, choices=INTERVIEW_CHOICES, default='-')
	interview_2 = models.CharField(max_length=5, choices=INTERVIEW_CHOICES, default='-')
	interview_3 = models.CharField(max_length=5, choices=INTERVIEW_CHOICES, default='-')

	def save(self, *args, **kwargs):
		if self.date_added != None:
			self.date_modified = datetime.datetime.today()
		super(Application, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	def years_rank(self):
		years = self.num_years_rank
		indicator = self.time_indicator
		decimal_num = re.search('([.])([0-9]*)', str(years))
		if not int(decimal_num.group(2)):
			years = int(years)
		if not years:
			years = ''
		elif years == 1:
			indicator = str(indicator).replace('s', '')
		# return years
		return "%s %s" % (years, indicator)
	years_rank.short_description = "Years in Rank"

	def _gross_tonnage(self):
		gross_tonnage = self.gross_tonnage
		if not gross_tonnage:
			gross_tonnage = 'N/A'
		else:
			gross_tonnage = format(gross_tonnage, "6,d").replace(",", ",")
		return gross_tonnage
	_gross_tonnage.short_description = "Gross Tonnage"

	def _contact_number(self):
		contact_number = self.contact_number
		if contact_number == '0':
			contact_number = 'N/A'
		elif len(contact_number) == 7:
			contact_number = contact_number[:3] + '-' + contact_number[3:5] + '-' + contact_number[5:]
		else:
			contact_number = contact_number[:4] + '-' + contact_number[4:8] + '-' + contact_number[8:]
		return contact_number
	_contact_number.short_description = "Contact Number"