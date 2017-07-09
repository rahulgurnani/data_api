from .models import FoodPermit

def get_truck_name(locationid):
	all_objects = FoodPermit.objects.all()
	closest = float("inf")
	ans = None
	for obj in all_objects:
		distance = abs(obj.locationid - int(locationid))
		if distance < closest:
			closest = distance
			ans = obj.Applicant

	return ans
