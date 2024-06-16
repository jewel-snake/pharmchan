from django.shortcuts import render

from rest_framework import permissions, viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import compmodel
import json
import PyPharm
import numpy
import threading
# Create your views here.

def optimize_and_save_thread(requested_model,data,)
    ir = json.loads(requested_model.body,object_hook=compmodel.irmodel.MEEncoder.as_system)
    model = PyPharm.BaseCompartmentModel(ir['matrix'],ir['output'],volumes=ir['volumes'])
    model.load_optimization_data(theoretical_x,theoretical_y,known_compartments,c0=data['init'])
    x0 = numpy.random.uniform(data['x_min'],data['x_max'])
    model.optimize(bounds=data['bounds'],x0=x0,options={'disp':True})
    serialized = json.dumps(model.configuration_matrix)
    solution = compmodel.models.Solution(model=requested_model.id,body=serialized)
    solution.save()

"""
    запрос на запуск процесса оптимизации
    model_pk -  ключ модели
    dataset_pk - ключ датасета
    в теле POST запроса должен находится JSON объект, который указывает, как сопоставить модель и датасет.
    должен преобразовываться в словарь, где ключами и значениями выступают названия полей в датасете и модели.
"""


@csrf_exempt
def request_optimize(request,model_pk,dataset_pk):
    if request.method == 'POST':
        try:
            requested_model = compmodel.models.Compmodel(pk=model_pk)
        except:
            return HttpResponse(status=404)

        try:
            requested_dataset = compmodel.models.DataSet(pk=dataset_pk)
        except:
            return HttpResponse(status=404)

        data = json.loads(request.data) #,object_hook=compmodel.irmorel.DataSetEncoder.as_dataset)
        try:
            (known_compartments,theoretical_x,theoretical_y) = requested_dataset.bind(requested_model,data['binding'])
        except:
            return HttpResponse(status=500)
#wrap
        threading.Thread(target=optimize_and_save_thread,args=(requested_model,data))
# wrap 

        return HttpResponse(status=201)
