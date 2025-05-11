from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Settlement
from .serializer import SettlementSerializer


@api_view(['POST'])
def create(request):
    serializer = SettlementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_many(request):
    settlements = Settlement.objects.all()
    serializer = SettlementSerializer(settlements, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def details(request, pk):
    try:
        settlement = Settlement.objects.get(pk=pk)
        serializer = SettlementSerializer(settlement)
        return Response(serializer.data)
    except Settlement.DoesNotExist:
        return Response({'error': 'Settlement not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_one(request, pk):
    try:
        settlement = Settlement.objects.get(pk=pk)
    except Settlement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SettlementSerializer(settlement)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, pk):
    try:
        settlement = Settlement.objects.get(pk=pk)
    except Settlement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SettlementSerializer(settlement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        settlement = Settlement.objects.get(pk=pk)
    except Settlement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    settlement.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
