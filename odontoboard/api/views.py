from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pacient
from .serializers import PacientSerializer
from rest_framework import serializers, status

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_pacients': 'pacients/',
        'Add': 'create/',
        'Update': 'update/pk/',
        'Delete': 'delete/pk/',
    }

    return Response(api_urls)

@api_view(['POST'])
def add_pacient(request):
    pacient = PacientSerializer(data=request.data)

    if Pacient.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if pacient.is_valid():
        pacient.save()
        return Response(pacient.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_pacients(request):
    if request.query_params:
        pacients = Pacient.objects.filter(**request.query_params.dict())
    else:
        pacients = Pacient.objects.all()
    
    if pacients:
        serializer = PacientSerializer(pacients, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update_pacients(request, pk):
    pacient = Pacient.objects.get(pk=pk)
    data = PacientSerializer(instance=pacient, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_pacients(request, pk):
    pacient = get_object_or_404(Pacient, pk=pk)
    pacient.delete()
    return Response(status=status.HTTP_202_ACCEPTED)