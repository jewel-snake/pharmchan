from django.shortcuts import render

from rest_framework import permissions, viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from compmodel import serializers, models

# Create your views here.
"""
    запрос на запуск процесса оптимизации
    model_pk -  ключ модели
    dataset_pk - ключ датасета
    в теле POST запроса должен находится JSON объект, который указывает, как сопоставить модель и датасет.
    должен преобразовываться в словарь, где ключами и значениями выступают названия полей в датасете и модели.
"""


@csrf_exempt
def request_run(request,model_pk,dataset_pk):
