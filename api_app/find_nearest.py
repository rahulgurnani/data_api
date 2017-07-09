from .models import FoodPermit

def get_truck_name(locationid):
	all_objects = FoodPermit.objects.all()
	closest = float("inf")
	ans = None
	for obj in all_objects:
		if abs(obj.locationid - int(locationid)) < closest:
			closest = abs(obj.locationid - locationid)
			ans = obj.Applicant

	return ans
