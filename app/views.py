from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.generics import *
from django.contrib.auth.models import User

class LoginUserApi(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            return Response({'message': 'Username atau Password Salah!'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        username = user.username
        password = data['password']

        return Response(
            {
                'data': {
                    'id_user': user.id,
                    'username': username,
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                },
            }, status=status.HTTP_200_OK
        )

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RegisterSerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def checklist_list(request):
    queryset = models.Checklist.objects.all()
    serializer = serializers.ChecklistSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checklist_create(request):
    serializer = serializers.ChecklistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def checklist_delete(request, pk):
    checklist = models.Checklist.objects.get(id=pk)
    checklist.delete()

    return Response('Deleted')

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def checklist_item_list(request, checklistid):
    queryset = models.ChecklistItem.objects.filter(checklist_id=checklistid)
    serializer = serializers.ChecklistSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checklist_item_create(request, checklistid):
    serializer = serializers.ChecklistItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def checklist_item_detail(request, checklistid, checklistitemid):
    queryset = models.ChecklistItem.objects.get(id=checklistitemid, checklist_id=checklistid)
    serializer = serializers.ChecklistSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def checklist_item_update(request, checklistid, checklistitemid):
    checklist_item = models.ChecklistItem.objects.get(id=checklistitemid, checklist_id=checklistid)
    serializer = serializers.ChecklistItemSerializer(instance=checklist_item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def checklist_item_delete(request, checklistid, checklistitemid):
    checklist_item = models.ChecklistItem.objects.get(id=checklistitemid, checklist_id=checklistid)
    checklist_item.delete()

    return Response('Deleted')

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def checklist_update(request, checklistid, checklistitemid):
    checklist = models.ChecklistItem.objects.get(id=checklistid)
    serializer = serializers.ChecklistSerializer(instance=checklist, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)