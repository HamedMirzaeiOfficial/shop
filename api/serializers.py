from rest_framework import serializers
from shop.models import Product, Category, Image


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category', 'name', 'slug',
                  'description', 'price', 'available')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('product', 'image')
