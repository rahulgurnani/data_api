from .models import FoodPermit
import django_filters
from django.forms import extras
from django.db import models
from django import forms

class FoodPermitFilter(django_filters.FilterSet):
    address_contains = django_filters.CharFilter(name='address', lookup_expr='contains')
    applicant_name_contains = django_filters.CharFilter(name='applicant', lookup_expr='contains')
    expired_permits = django_filters.DateFilter(name='expirationdate', lookup_expr='lte', widget = extras.SelectDateWidget)
    class Meta:
        model = FoodPermit
        fields = ['applicant', 'address', 'address_contains', 'expired_permits']

        # filter_overrides = {
        #     models.DateField: {
        #         'filter_class': django_filters.DateFilter,
        #         'extra': lambda f: {
        #             'widget': extras.SelectDateWidget
        #         },
        #     },
        # }