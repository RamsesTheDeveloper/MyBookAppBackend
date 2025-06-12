from rest_framework import serializers
from Book.models import Book
from django.conf import settings

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('category', 'id', 'title', 'slug', 'author', 'description', 'status', 'quantity', 'publish_date', 'number_of_pages')

"""
from rest_framework import serializers

from book_api.models import Book

from django.forms import ValidationError

# Automatically implementing serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

        # Note 1
    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No Diet Coke please")
        return value

    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("Too heavy for our inventory")
        return data

    def get_description(self, data):
        return "This book is called" + data.title + " and it is " + str(data.number_of_pages) + " pages long."

# 1. This is how we validate the data that is coming in when we use ModelSerializer.
"""