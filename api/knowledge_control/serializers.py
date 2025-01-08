from knowledge_control import models
from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = [
            'id',
            'text',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = models.Question
        fields = [
            'id',
            'text',
            'options',
        ]


class TestDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Test
        fields = '__all__'
