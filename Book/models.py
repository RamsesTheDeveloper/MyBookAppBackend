from unicodedata import name
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    class BookObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(BookCategory, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=250)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    description = models.TextField()

    slug = models.SlugField(max_length=250, unique_for_date='published')

    published = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='book_store')

    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager() # default Manager
    bookobjects = BookObjects() # custom Manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


"""
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

# This Book Class defines our Model within the SQL Database
"""