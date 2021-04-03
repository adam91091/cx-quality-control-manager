import django_filters
from django.db.models import Q

from apps.constants import ORDER_STATUS_OPEN_STARTED
from apps.orders.models import Order


class StatusChoiceFilter(django_filters.ChoiceFilter):
    """Custom choice filter for order status"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            (ORDER_STATUS_OPEN_STARTED, ORDER_STATUS_OPEN_STARTED),
        ]

    def filter(self, qs, value: str):
        """
        Extend base filter method for retrieving opened or started orders.
        Make filtering using Q query with alternative.
        :param qs:    QuerySet instance
        :param value: Value from extra['choices']
        """
        if value == ORDER_STATUS_OPEN_STARTED:
            _qs = qs.filter(Q(status__iexact='Started') | Q(status__iexact='Open'))
            return _qs
        return super().filter(qs, value)


class OrderFilter(django_filters.FilterSet):

    client_name = django_filters.CharFilter(field_name='client__client_name', lookup_expr='icontains')
    order_sap_id = django_filters.CharFilter(lookup_expr='icontains')
    product_sap_id = django_filters.CharFilter(field_name='product__product_sap_id', lookup_expr='icontains')
    date_of_production = django_filters.DateTimeFromToRangeFilter(lookup_expr='range')
    description = django_filters.CharFilter(field_name='product__description', lookup_expr='icontains')
    status = StatusChoiceFilter(choices=Order.STATUS_CHOICES, lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ('client_name', 'order_sap_id', 'product_sap_id',
                  'date_of_production', 'description', 'status', )
