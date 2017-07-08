# from background_task import background
# from django.contrib.auth.models import User
# from models import FoodPermit
# import datetime

# @background(schedule=60)
# def auto_expire(user_id):
#     # lookup user by id and send them a message
#     expired = FoodPermit.objects.get(expirationdate__lte=datetime.datetime.now().date())
#     for obj in expired:
#     	obj.status = "EXPIRED"
#     	obj.save()