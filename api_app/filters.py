from .models import FoodPermit
import django_filters

class FoodPermitFilter(django_filters.FilterSet):
    address_contains = django_filters.CharFilter(name='address', lookup_expr='contains')
    applicant_name_contains = django_filters.CharFilter(name='applicant', lookup_expr='contains')
    expired_permits = django_filters.CharFilter(name='expirationdate', lookup_expr='year__lt')
    class Meta:
        model = FoodPermit
        fields = ['applicant', 'address', 'address_contains', 'expired_permits']