from django.shortcuts import render
from django.views import View


# Create your views here.

class ResViews(View):

    def get(self, request):

        # return render(request, '')
        pass

    def post(self, request):

        pass


class LoginViews(View):

    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):

        pass