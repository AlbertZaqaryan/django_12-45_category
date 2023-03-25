from django.urls import path
from . import views

urlpatterns=[
    path('' ,views.index, name='index'),
    path('prod/<int:id>/' ,views.prod, name='prod'),
]