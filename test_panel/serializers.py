from rest_framework import serializers
from .models import Test, Science, ExamTest


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def validate(self, data):
        right_answer = data.get('right_answer')
        variants = [data.get('variant1'), data.get('variant2'), data.get('variant3'), data.get('variant4')]

        if right_answer not in variants:
            raise serializers.ValidationError({"right_answer": "To'g'ri javob variantlardan biriga ham to'g'ri kelmaydi."})
        return data


class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'


class ExamTestSerializer(serializers.ModelSerializer):
    is_correct = serializers.SerializerMethodField()

    class Meta:
        model = ExamTest
        fields = '__all__'
        read_only_fields = ('user', 'is_correct')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        test = validated_data['test']
        selected_answer = validated_data['selected_answer']
        validated_data['is_correct'] = (selected_answer == test.right_answer)
        return super().create(validated_data)

    def get_is_correct(self, obj):
        return obj.selected_answer == obj.test.right_answer
