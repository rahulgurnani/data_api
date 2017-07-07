from api_app.models import FoodPermit
from datetime import date
import csv
from datetime import datetime


f = open('Mobile_Food_Facility_Permit.csv', 'r')
def populate():
    fl = csv.reader(f, delimiter=',')
    for row in fl:
        if k == 0:
            k+=1
            continue
        fp = FoodPermit()
        fp.locationid = int(row[0])
        fp.applicant = row[1]
        fp.facilitytype = row[2]
        fp.cnn = int(row[3])
        fp.locationdescription = row[4]
        fp.address = row[5]
        fp.blocklot = row[6]
        fp.block = row[7]
        fp.lot = row[8]
        fp.permit = row[9]
        fp.status = row[10]
        fp.fooditems = row[11]
        if row[12] == '':
            fp.x = None
        else:
            fp.x = float(row[12])
        if row[13] == '':
            fp.y = None
        else:
            fp.y = float(row[13])
        fp.latitude = float(row[14])
        fp.longitude = float(row[15])
        fp.schedule = row[16]
        fp.dayshours = row[17]
        if len(row[18]) == 0:
            fp.noisent = None		# mm/dd/yyyy time
        else:
            fp.noisent = datetime.strptime(row[18], '%m/%d/%Y %H:%M:%S %p').date()
        if row[19] == '':
            fp.approved = None
        else:
            fp.approved = datetime.strptime(row[19], '%m/%d/%Y %H:%M:%S %p').date()	# mm/dd/yyyy time
        if len(row[20]) == 0:
            fp.received = None
        else:
            fp.received = datetime.strptime(row[20], '%Y-%m-%d').date() # yyyy-mm-dd
        fp.priorpermit = bool(row[21]) 
        if len(row[22]) == 0:
            fp.expirationdate = None		# mm/dd/yyyy time
        else:
            fp.expirationdate = datetime.strptime(row[22], '%m/%d/%Y %H:%M:%S %p').date()	# mm/dd/yyyy time		
        fp.save()    