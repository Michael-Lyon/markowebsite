from .models import Item
import django_filters 


class ItemFilter(django_filters.FilterSet):
    category = Item.objects.all()
    class Meta:
        model = Item
        fields = ['category']
