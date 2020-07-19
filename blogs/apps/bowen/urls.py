from django.urls import path, include

from bowen.views import indexViews


urlpatterns = [
    path('', indexViews.as_view(), name='index')
]