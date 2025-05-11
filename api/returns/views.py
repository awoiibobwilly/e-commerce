from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Returns
from .serializer import ReturnsSerializer


@api_view(['POST'])
def create(request):
    serializer = ReturnsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_many(request):
    returns = Returns.objects.all()
    serializer = ReturnsSerializer(returns, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def details(request, pk):
    try:
        returns = Returns.objects.get(pk=pk)
        serializer = ReturnsSerializer(returns)
        return Response(serializer.data)
    except Returns.objects.DoesNotExist:
        return Response({'error': 'returns not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_one(request, pk):
    try:
        returns = Returns.objects.get(pk=pk)
    except Returns.objects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReturnsSerializer(returns)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, pk):
    try:
        returns = Returns.objects.get(pk=pk)
    except Returns.objects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReturnsSerializer(returns, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        returns = Returns.objects.get(pk=pk)
    except Returns.objects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    returns.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
