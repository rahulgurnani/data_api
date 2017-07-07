from .models import FoodPermit
import django_filters

class FoodPermitFilter(django_filters.FilterSet):
    address_contains = django_filters.CharFilter(name='address', lookup_expr='contains')
    class Meta:
        model = FoodPermit
        fields = ['applicant', 'address', 'address_contains']