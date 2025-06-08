from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    AVAILABLE = 'A'
    BORROWED = 'B'
    STATUS_SHOICES = [
        (AVAILABLE, 'Available'),
        (BORROWED, 'Borrowed')
    ]
    title = models.TextField()
    authors = models.ManyToManyField(Author, related_name='books')
    publication_date = models.DateField(auto_now_add=True, null=True, blank=True)
    ISBN = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_SHOICES, default=AVAILABLE)
    
    def __str__(self) -> str:
        return self.title

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    
    def __str__(self) -> str:
        return self.book.title 

