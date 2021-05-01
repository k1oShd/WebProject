from rest_framework import serializers
from .models import Prodcut, Manufacturer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodcut
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_blank=True)
    description = serializers.CharField(max_length=500, allow_blank=True, required=False)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('code', instance.description)
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200, allow_blank=True)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
