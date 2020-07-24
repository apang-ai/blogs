from django.urls import path
from .views import LoginViews, LogOutViews, RegisterViews, EditViews

app_name = 'users'

urlpatterns = [
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogOutViews.as_view(), name='logout'),
    path('register/', RegisterViews.as_view(), name='register'),
    path('edit-<id>/', EditViews.as_view(), name='edit'),
]