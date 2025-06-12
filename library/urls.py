from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views


urlpatterns = [
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member_dateil')
]

urlpatterns = format_suffix_patterns(urlpatterns)