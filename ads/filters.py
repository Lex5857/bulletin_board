from django_filters import FilterSet
from .models import Ads


# Создаем свой набор фильтров для модели Ads.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class AdsFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Ads
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'author': ['exact'],
            'category': ['exact'],
            'heading': ['icontains'],
        }
