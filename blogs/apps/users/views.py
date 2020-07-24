from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View

from .models import Profile

# Create your views here.


class LoginViews(View):
    '''登录'''
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
    '''登出'''
    def get(self, request):

        auth.logout(request)

        return redirect('users:login')


class RegisterViews(View):
    '''注册'''
    def get(self, request):

        return render(request, 'users/register.html')

    def post(self, request):

        getUser = request.POST.get('username')
        getEmail = request.POST.get('email')
        getPass = request.POST.get('password')
        getPass2 = request.POST.get('password2')

        if getUser and getPass and getEmail and getPass2:

            userObj = User.objects.filter(username=getUser)

            if userObj:
                content = {'err': '用户已存在！'}
                return render(request, 'users/register.html', content)

            else:

                if getPass == getPass2:

                    createUserObj = User.objects.create_user(username=getUser, password=getPass, email=getEmail)

                    User.save(createUserObj)

                    return redirect('users:login')
        else:
            content = {'err': '输入不能为空!'}
            return render(request, 'users/register.html', content)


class EditViews(View):

    def get(self, request, id):

        userObj = User.objects.get(id=id)
        if userObj:

            try:
                userProfile = Profile.objects.get(userId_id=id)
                content = {'profile': userProfile}
                return render(request, 'users/edit.html', content)

            except Exception:

                return render(request, 'users/edit.html')
        else:
            return redirect('article:article-list')

    def post(self, request, id):

        getPhone = request.POST.get('phone')
        getBio = request.POST.get('bio')
        getAvater = request.FILES.get('avatar')
        print(getAvater)

        if getBio or getPhone or getAvater:

            try:
                userProfileObj = Profile.objects.get(userId_id=id)

                userProfileObj.mobile = getPhone
                userProfileObj.bio = getBio
                userProfileObj.avatar = getAvater
                userProfileObj.save()

                content = {'profile': userProfileObj}
                return render(request, 'users/edit.html', content)

            except Exception:

                userProfile = Profile.objects.create(mobile=getPhone, bio=getBio, avatar=getAvater, userId_id=id)

                content = {'profile': userProfile}
                return render(request, 'users/edit.html', content)
