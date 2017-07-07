# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class FoodPermit(models.Model):
	locationid = models.BigIntegerField(default=0)
	applicant = models.CharField(max_length=100, blank=True, default='')
	facilitytype = models.CharField(max_length=100, blank=True, default='')
	cnn = models.BigIntegerField(default=0)
	locationdescription = models.CharField(max_length=100, blank=True, default='')
	address = models.CharField(max_length=100, blank=True, default='')
	blocklot = models.CharField(max_length=100, blank=True, default='')
	block = models.CharField(max_length=100, blank=True, default='')
	lot = models.CharField(max_length=100, blank=True, default='')
	permit = models.CharField(max_length=100, blank=True, default='')
	status = models.CharField(max_length=100, blank=True, default='')
	fooditems = models.CharField(max_length=100, blank=True, default='')
	x = models.DecimalField(max_digits=12, decimal_places=3, null=True)
	y = models.DecimalField(max_digits=12, decimal_places=3, null=True)
	latitude = models.DecimalField(max_digits=20, decimal_places=16)
	longitude = models.DecimalField(max_digits=20, decimal_places=16)
	schedule = models.CharField(max_length=100, blank=True, default='')
	dayshours = models.CharField(max_length=100, blank=True, default='')
	noisent = models.DateField(default=datetime.date.today, null=True)
	approved = models.DateField(default=datetime.date.today, null=True)
	received = models.DateField(default=datetime.date.today, null=True)
	priorpermit = models.BooleanField()
	expirationdate = models.DateField(default=datetime.date.today, null=True)
	# location = models.
	class Meta:
		ordering = ('locationid',) 



