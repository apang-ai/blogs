from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator

from .models import ArticlePost

import markdown
# Create your views here.


class ArticleListViews(View):

    def get(self, request):

        search = request.GET.get('search')
        order = request.GET.get('order')
        column = request.GET.get('column')
        tag = request.GET.get('tag')

        articleList = ArticlePost.objects.all()

        if search:
            articleList = ArticlePost.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))

        else:
            # 将 search 参数重置为空
            search = ''

        # 栏目查询集
        if column is not None and column.isdigit():
            articleList = articleList.filter(column=column)

        if tag and tag != 'None':

            articleList = articleList.filter(tags__name__in=[tag])
        # 根据GET请求中查询条件
        # 返回不同排序的对象数组
        if order == 'click':
            articleList = ArticlePost.objects.all().order_by('-click')

        # 每页显示 2 篇文章
        paginator = Paginator(articleList, 2)
        # 获取URL中的页码
        page = request.GET.get('page')
        # 将导航对象相应的页码内容返回给 articles
        articles = paginator.get_page(page)

        content = {
            'articles': articles,
            'order': order,
            'search': search,
            'column': column,
            'tag': tag,
        }

        return render(request, 'article/list.html', content)


class ArticleDetailViews(View):

    def get(self, request, id):

        try:
            articleObj = ArticlePost.objects.get(id=id)
            articleObj.click += 1
            articleObj.save(update_fields=['click'])

            # 修改 Markdown 语法渲染
            md = markdown.Markdown(
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
            articleObj.body = md.convert(articleObj.body)
        except Exception:

            return redirect('article:article-list')


        content = {
            'article': articleObj,
            'toc': md.toc,
        }
        return render(request, 'article/detail.html', content)




