from django.urls import path, include
from engine import views

urlpatterns = [
    path('request/optimize/<int:model_pk>/<int:dataset_pk>',views.request_optimize)
]
