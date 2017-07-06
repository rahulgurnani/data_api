from django import forms

from .models import FoodPermit
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import extras

STATUS_CHOICES = ('EXPIRED', 'REQUESTED', 'INACTIVE')

class FoodPermitForm(forms.ModelForm):
	newfield = forms.DateField(widget = extras.SelectDateWidget)
	class Meta:
		model = FoodPermit
		fields = ['locationid', 'applicant', 'facilitytype', 'cnn', 'locationdescription', 'address', 'blocklot', 'block', 'lot', 'permit', 'status', 'fooditems', 'x', 'y', 'latitude', 'longitude', 'schedule', 'dayshours', 'noisent', 'approved', 'received', 'priorpermit', 'expirationdate', ]
		widgets = {
					'noisent' : extras.SelectDateWidget,
					'approved' : extras.SelectDateWidget,
					'received' : extras.SelectDateWidget,
					'expirationdate': extras.SelectDateWidget					
				}