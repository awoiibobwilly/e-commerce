from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Delivery
from .serializer import DeliverySerializer


@api_view(['POST'])
def create_delivery(request):
    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_deliveries(request):
    deliveries = Delivery.objects.all()
    serializer = DeliverySerializer(deliveries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)
    except Delivery.DoesNotExist:
        return Response({'error': 'Delivery not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_delivery(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
    except Delivery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeliverySerializer(delivery)
    return Response(serializer.data)


@api_view(['PUT'])
def update_delivery(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
    except Delivery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeliverySerializer(delivery, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_delivery(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
    except Delivery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    delivery.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

