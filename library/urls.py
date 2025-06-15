from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from library.views import (
    MemberViewSet, 
    AuthorViewSet, 
    BookViewSet
    )


router = DefaultRouter()
router.register(r'members', MemberViewSet, basename='member')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
# prefix is for URL mapping and
# base name is for naming the urls.(name=member-list)

urlpatterns = [
    path('', include(router.urls))
]
