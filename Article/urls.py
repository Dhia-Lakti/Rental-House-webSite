from django.urls import path
from .views import getAllArticles, AddArticle, getArticleById, updateArticleById, deleteArticle, getArticleByType


urlpatterns = [
    path('', getAllArticles, name='getAllArticles'),
    path('add', AddArticle, name='AddArticle'),
    path('<int:article_id>', getArticleById, name='getArticleById'),
    path('update/<int:article_id>', updateArticleById, name='updateArticleById'),
    path('delete/<int:article_id>', deleteArticle, name='deleteArticle'),
    path('<str:article_type>', getArticleByType, name='getArticleByType'),

]
