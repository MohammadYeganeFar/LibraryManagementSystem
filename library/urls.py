from django.urls import path
from library import views


urlpatterns = [
    path('members/', views.member_list, name='member_list'),
    # path('members/<int:pk>/', views.member_detail, name='member_dateil')
]