from .models import FoodPermit
import django_filters

class FoodPermitFilter(django_filters.FilterSet):
    class Meta:
        model = FoodPermit
        fields = ['applicant', 'address', ]