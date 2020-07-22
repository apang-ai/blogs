from django.urls import path
from article.views import ArticleListViews, ArticleDetailViews

app_name = 'article'

urlpatterns = [
    path('article-list/', ArticleListViews.as_view(), name='article-list'),
    path('article-detail-<id>/', ArticleDetailViews.as_view(), name='article-detail')
]