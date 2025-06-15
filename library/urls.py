from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library.views import MemberViewSet, AuthorViewSet


member_list = MemberViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)
member_detail = MemberViewSet.as_view(
    {
        'get':'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)
member_name = MemberViewSet.as_view(
    {
        'get': 'fullname'
    }
)
author_list = AuthorViewSet.as_view(
    {
        'get': 'list'
    }
)
author_detail = AuthorViewSet.as_view(
    {
        'get': 'retrieve'
    }
)

urlpatterns = [
    path('members/', member_list, name='member-list'),
    path('members/<int:pk>/', member_detail, name='member-detail'),
    path('members/<int:pk>/name/', member_name, name='member-name'),
    path('authors/', author_list, name='author-list'),
    path('authors/<int:pk>/', member_detail, name='author-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)