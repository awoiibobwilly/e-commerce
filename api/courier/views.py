from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Courier, CourierPerformance
from .serializer import CourierSerializer, CourierPerformanceSerializer


@api_view(['POST'])
def create(request):
    serializer = CourierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_many(request):
    couriers = Courier.objects.all()
    serializer = CourierSerializer(couriers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def details(request, pk):
    try:
        courier = Courier.objects.get(pk=pk)
        serializer = CourierSerializer(courier)
        return Response(serializer.data)
    except Courier.DoesNotExist:
        return Response({'error': 'Courier not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list_one(request, pk):
    try:
        courier = Courier.objects.get(pk=pk)
    except Courier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourierSerializer(courier)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, pk):
    try:
        courier = Courier.objects.get(pk=pk)
    except Courier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourierSerializer(courier, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        courier = Courier.objects.get(pk=pk)
    except Courier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    courier.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def create_courier_perf(request):
    serializer = CourierPerformanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_couriers_perf(request):
    couriers_perf = CourierPerformance.objects.all()
    serializer = CourierPerformanceSerializer(couriers_perf, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def perf_detail(request, pk):
    try:
        courier_perf = CourierPerformance.objects.get(pk=pk)
        serializer = CourierPerformanceSerializer(courier_perf)
        return Response(serializer.data)
    except CourierPerformance.DoesNotExist:
        return Response({'error': 'Courier_perf not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_courier_perf(request, pk):
    try:
        courier_perf = CourierPerformance.objects.get(pk=pk)
    except CourierPerformance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourierPerformanceSerializer(courier_perf)
    return Response(serializer.data)


@api_view(['PUT'])
def update_courier_perf(request, pk):
    try:
        courier_perf = CourierPerformance.objects.get(pk=pk)
    except CourierPerformance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourierPerformanceSerializer(courier_perf, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_courier_perf(request, pk):
    try:
        courier_perf = CourierPerformance.objects.get(pk=pk)
    except CourierPerformance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    courier_perf.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)