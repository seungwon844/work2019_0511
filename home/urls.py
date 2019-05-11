from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('', views.post_list_latest, name='post_list_latest'),
    # path('', views.expensive_item, name='expensive_item'),
    path('', views.result_list, name='result_list'),
]
