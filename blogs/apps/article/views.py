from django.shortcuts import render, redirect
from django.views import View
from .models import ArticlePost

import markdown
# Create your views here.


class ArticleListViews(View):

    def get(self, request):

        blogsObj = ArticlePost.objects.all()

        content = {
            'blogList': blogsObj
        }

        return render(request, 'article/list.html', content)


class ArticleDetailViews(View):

    def get(self, request, id):

        try:
            articleObj = ArticlePost.objects.get(id=id)

            articleObj.body = markdown.markdown(articleObj.body, extensions=[
                                                                    # 包含 缩写、表格等常用扩展
                                                                    'markdown.extensions.extra',
                                                                    # 语法高亮扩展
                                                                    'markdown.extensions.codehilite',
                                                         ])
        except Exception:

            return redirect('article:article-list')


        content = {
            'article': articleObj
        }
        return render(request, 'article/detail.html', content)

