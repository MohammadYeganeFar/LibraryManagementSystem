from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from library.models import Member, Author, Book
from library.serializers import (
    MemberSerializer,
    AuthorSerializer,
    BookSerializer
    )


class MemberViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provide these oprations:
        * list
        * create
        * retrieve
        * update
        * destroy
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True, methods=['GET'])
    def fullname(self, request, pk, *args, **kwargs):
        member = self.get_object() # instead of Member.objects.get(pk=pk)
        return Response(member.name)

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provide these operations:
        * list
        * retrive
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer