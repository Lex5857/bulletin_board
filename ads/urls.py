from django.urls import path

from .views import AdsList, AdsDetail
from .views import ResponsesList, ResponsesDetail
from .views import AdsUpdate, ResponsesUpdate
from .views import AdsDelete, ResponsesDelete
from .views import AdsCreate, ResponsesCreate
from .views import UserCreate, AuthorCreate


urlpatterns = [
    path('creatuser/', UserCreate.as_view()),
    path('creatauthor/', AuthorCreate.as_view(), name='author_create'),

    path('createads/', AdsCreate.as_view()),
    path('ads/', AdsList.as_view(), name='ads_list'),
    path('ads/<int:pk>', AdsDetail.as_view(), name='ads_detail'),
    path('ads/<int:pk>/update/', AdsUpdate.as_view(), name='ads_update'),
    path('ads/<int:pk>/delete/', AdsDelete.as_view(), name='ads_delete'),

    path('createresponses/', ResponsesCreate.as_view()),
    path('responses/', ResponsesList.as_view(), name='responses_list'),
    path('responses/<int:pk>', ResponsesDetail.as_view(), name='responses_detail'),
    path('responses/<int:pk>/update/', ResponsesUpdate.as_view(), name='responses_update'),
    path('responses/<int:pk>/delete/', ResponsesDelete.as_view(), name='responses_delete'),
]
