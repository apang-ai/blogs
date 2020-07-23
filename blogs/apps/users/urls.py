from django.urls import path
from .views import LoginViews, LogOutViews

app_name = 'users'

urlpatterns = [
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogOutViews.as_view(), name='logout'),
]