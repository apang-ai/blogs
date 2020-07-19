from django.urls import path

from users.views import LoginViews, ResViews


urlpatterns = [
    path('login/', LoginViews.as_view(), name='login'),
    path('res/', ResViews.as_view(), name='res'),
]