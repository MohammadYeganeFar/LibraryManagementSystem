from django.urls import path
from library import views


urlpatterns = [
    path('members/', views.member_list, name='member_list')
]