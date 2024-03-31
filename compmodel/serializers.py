from rest_framework import serializers
from compmodel.models import CompModel

class CompModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompModel
        fields = ['id','name','author','body']
        
    """
    should be something like:
class CompModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.IntegerField()
    body = serializers.JSONField(binary=True)

    def create(self, validated_data):
        return CompModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author',instance.author)
        instance.name = validated_data.get('name',instance.name)
        instance.body = validated_data.get('body',instance.body)
        instance.save()
        return instance
    """

class CompModelPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompModel
        fields = ['id','name','author']
