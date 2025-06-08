from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.IntegerField()


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    age = models.IntegerField()

    
class Book(models.Model):
    AVAILABLE = 'A'
    BORROWED = 'B'
    STATUS_SHOICES = [
        (AVAILABLE, 'Available'),
        (BORROWED, 'Borrowed')
    ]
    title = models.TextField()
    author = models.ManyToManyField(Author)
    publication_date = models.DateField(auto_now_add=True, null=True, blank=True)
    ISBN = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_SHOICES, default=AVAILABLE)


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

