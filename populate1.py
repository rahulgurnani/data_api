from api_app.models import FoodPermit
from datetime import date
import csv

f = open('Mobile_Food_Facility_Permit.csv', 'r')
fl = csv.reader(f, delimiter=',')
fp = FoodPermit()
fp.locationid = 1
fp.applicant = 'temp'
fp.facilitytype = 'temp'
fp.cnn = 12
fp.locationdescription = 'temp'
fp.address = 'temp'
fp.blocklot = 'temp'
fp.block = 'temp'
fp.lot = 'temp'
fp.permit = 'temp'
fp.status = 'temp'
fp.fooditems = 'temp'
fp.x = 2.44
fp.y = 2.44
fp.latitude = 2.44
fp.longitude = 2.44
fp.schedule = 'temp'
fp.dayshours = 'temp'
d = date(2012, 2, 2)
fp.noisent = d
fp.approved = d
fp.received = d
fp.priorpermit = False
fp.expirationdate = d

fp.save()
	