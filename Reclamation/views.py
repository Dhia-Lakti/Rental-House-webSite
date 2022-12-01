from .serializer import ReclamationSerializer
from .models import Reclamation
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


@api_view(['get'])
def getAllReclamations(request):
    reclamations = Reclamation.objects.all()
    serializer = ReclamationSerializer(reclamations, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['post'])
def AddReclamation(request):
    data = JSONParser().parse(request)
    serializer = ReclamationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['get'])
def getReclamationById(request, reclamation_id):

    try:
        reclamation = Reclamation.objects.get(pk=reclamation_id)
    except  Reclamation.DoesNotExist:
        return JsonResponse({"error": "Reclamation Not Existe"}, status=404)
    serializer = ReclamationSerializer(reclamation)
    return JsonResponse(serializer.data, status=200)

@api_view(['delete'])
def deleteReclamation(request, reclamation_id):
    try:
        reclamation = Reclamation.objects.get(pk=reclamation_id)
    except  Reclamation.DoesNotExist:
        return JsonResponse({"error": "Reclamation Not Existe"}, status=404)
    reclamation.delete()
    return JsonResponse({"success": "Reclamation Deleted successfully"}, status=200)
