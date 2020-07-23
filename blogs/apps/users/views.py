from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View

# Create your views here.


class LoginViews(View):

    def get(self, request):

        return render(request, 'users/login.html')

    def post(self, request):

        getUser = request.POST.get('username')
        getPass = request.POST.get('password')

        userObj = auth.authenticate(username=getUser, password=getPass)

        if userObj:

            auth.login(request, userObj)
            return redirect('article:article-list')
        else:
            content = {
                'err': '用户名或密码错误！'
            }
            return render(request, 'users/login.html', content)


class LogOutViews(View):

    def get(self, request):

        auth.logout(request)

        return redirect('users:login')

