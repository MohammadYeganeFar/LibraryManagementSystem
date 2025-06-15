from rest_framework import serializers
from library.models import Member, Author, Book

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
   

class AuthorSerializer(serializers.ModelSerializer):
    # I defined a `related_name=books in Book model, 
    # so maybe not needed to implement this:`
    # books = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Member.objects.all()
    #     )

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField()
    class Meta:
        model = Book
        fields = "__all__"

    def perform_create(self, serializer):
        serializer.save(authors=self.request.user)