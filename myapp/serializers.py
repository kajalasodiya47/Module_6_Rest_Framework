from rest_framework import serializers
from .models import Book

# bookserializer code
class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=('id','title','author','isbn','publisher')
