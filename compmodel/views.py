from django.shortcuts import render

from rest_framework import permissions, viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from compmodel import serializers, models
# Create your views here.

class CompModelViewSet(viewsets.ModelViewSet):
    queryset = models.CompModel.objects.all()
    serializer_class = serializers.CompModelSerializer
    permission_classes = [] # TODO: research what this actually do

#class CompModelPreviewView(viewsets.ModelViewSet):

#function to use Jango REST framework serializers.
@csrf_exempt
def compmodel_list(request):
    #if method is get, return all compmodels
    if request.method == 'GET':
        all_models = models.CompModel.objects.all()
        serializer = serializers.CompModelSerializer(all_models, many=True)
        return JSONResponse(serializer.data,safe=False)
    #if method is post, request body must be list of compmodels to save to database
    elif request.method == 'POST':
        data = JSONParser().parse(data=request)
        serializer = serializers.CompModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def compmodel_single(request, pk):
    #get compmodel with specified primary key.
    try:
        that_compmodel = models.Compmodels.objects.get(pk=pk)
    except:
        #if unsuccessful return 404
        return HttpResponse(status=404)
    #if method is get then return that compmodel
    if request.method == 'GET':
        serializer = serializers.CompModelSerializer(that_compmodel)
        return JSONResponse(serializer)
    #if method is put, update compmodel
    elif request.method == 'PUT':
        data = JSONParser().parse(data=request)
        serializer = serializers.CompModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)
    #if method is delete, then delete that compmodel
    elif request.method == 'DELETE':
        that_model.delete()
        return HttpResponse(status=204)
    
