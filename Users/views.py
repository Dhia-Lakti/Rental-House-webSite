from distutils.log import error
from .serializer import UserResponseSerializer, UserRequestSerializer
from .models import User
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password


#class UserView(APIView):

permission_classes = (IsAuthenticated,)

@api_view(['get'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserResponseSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['post'])
def AddUser(request):
    data = JSONParser().parse(request)
    #data["password"] = make_password(data["password"])
    serializer = UserRequestSerializer(data=data)
    #serializer.password = make_password(serializer.password)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['get'])
def getUserById(request, user_id):

    try:
        user = User.objects.get(pk=user_id)
    except  User.DoesNotExist:
        return JsonResponse({"error": "User Not Existe"}, status=404)
    serializer = UserResponseSerializer(user)
    return JsonResponse(serializer.data, status=200)

@api_view(['put'])
def updateUserById(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except  User.DoesNotExist:
        return JsonResponse({"error": "User Not Existe"}, status=404)
    data = JSONParser().parse(request)
    serializer = UserRequestSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['delete'])
def deleteUser(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except  User.DoesNotExist:
        return JsonResponse({"error": "User Not Existe"}, status=404)
    user.delete()
    return JsonResponse({"success": "User Deleted successfully"}, status=200)