import django_filters
from django_filters import FilterSet
from .models import Post
from django.forms import DateTimeInput


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    date = django_filters.DateTimeFilter(
        field_name="dateCreation",
        lookup_expr="gt",
        label="Posting date",
        widget=DateTimeInput(
            attrs={"type": "date"},
            format='%Y-%m-%dT'
        )
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['icontains'],

        }
