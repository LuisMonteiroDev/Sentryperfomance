from rest_framework import serializers
from .models import Books, Companys, BookGenres


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Books
        fields = '__all__'


class CompanysSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Companys
        fields = '__all__'


class BooksGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenres
        fields = '__all__'
