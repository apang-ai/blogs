from django.shortcuts import render
from django.views import View

from bowen.models import BowenKind

# Create your views here.


class indexViews(View):

    def get(self, request):

        BowenKindObj = BowenKind.objects.all()

        content = {
            'kindList': BowenKindObj
        }

        return render(request, 'index.html', content)

    def post(self, request):
        
        pass