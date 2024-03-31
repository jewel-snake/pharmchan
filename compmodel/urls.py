from django.urls import path, include
from compmodel import views

urlpatterns = [
    path('compmodel/',views.compmodel_list),
    path('compmodel/<int:pk>/',views.compmodel_single),
]
