from django.contrib import admin
from .models import Author, Category, Ads, Responses, AdsCategory


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Ads)
admin.site.register(Responses)
admin.site.register(AdsCategory)
