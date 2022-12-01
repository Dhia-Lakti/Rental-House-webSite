from .serializer import ArticleSerializer
from .models import Article
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


@api_view(['get'])
def getAllArticles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['post'])
def AddArticle(request):
    data = JSONParser().parse(request)
    serializer = ArticleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['get'])
def getArticleById(request, article_id):

    try:
        article = Article.objects.get(pk=article_id)
    except  Article.DoesNotExist:
        return JsonResponse({"error": "Article Not Existe"}, status=404)
    serializer = ArticleSerializer(article)
    return JsonResponse(serializer.data, status=200)

@api_view(['put'])
def updateArticleById(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except  Article.DoesNotExist:
        return JsonResponse({"error": "Article Not Existe"}, status=404)
    data = JSONParser().parse(request)
    serializer = ArticleSerializer(article, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['delete'])
def deleteArticle(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except  Article.DoesNotExist:
        return JsonResponse({"error": "Article Not Existe"}, status=404)
    article.delete()
    return JsonResponse({"success": "Article Deleted successfully"}, status=200)

@api_view(['get'])
def getArticleByType(request, article_type):

    try:
        articles = Article.objects.filter(type__iexact=article_type)
    except  Article.DoesNotExist:
        return JsonResponse({"error": "Article Not Existe"}, status=404)
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)
