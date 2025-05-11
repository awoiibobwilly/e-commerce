from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Fulfilment
from .serializer import FulfilmentSerializer


@api_view(['POST'])
def create(request):
    serializer = FulfilmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_many(request):
    fulfilments = Fulfilment.objects.all()
    serializer = FulfilmentSerializer(fulfilments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def details(request, pk):
    try:
        fulfilment = Fulfilment.objects.get(pk=pk)
        serializer = FulfilmentSerializer(fulfilment)
        return Response(serializer.data)
    except Fulfilment.DoesNotExist:
        return Response({'error': 'Fulfilment not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list_one(request, pk):
    try:
        fulfilment = Fulfilment.objects.get(pk=pk)
    except Fulfilment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FulfilmentSerializer(fulfilment)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, pk):
    try:
        fulfilment = Fulfilment.objects.get(pk=pk)
    except Fulfilment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FulfilmentSerializer(fulfilment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        fulfilment = Fulfilment.objects.get(pk=pk)
    except Fulfilment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    fulfilment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
