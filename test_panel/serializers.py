from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Science, Test, ExamTest
from django.contrib.auth import get_user_model

User = get_user_model()


class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ['id', 'science_name', 'created_at', 'updated_at']


class TestSerializer(serializers.ModelSerializer):
    science = serializers.SerializerMethodField()
    class Meta:
        model = Test
        fields = ['id', 'question', 'question_image', 'variant1', 'variant2', 'variant3', 'variant4', 'right_answer',
                  'science', 'created_at', 'updated_at']

    def get_science(self, obj):
        return obj.science.science_name


class ExamTestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTest
        fields = ['id', 'user', 'science', 'selected_answer', 'is_correct', 'created_at', 'updated_at']


class ExamTestSerializer(serializers.Serializer):
    science_id = serializers.IntegerField()
    test_ids = serializers.ListField(child=serializers.IntegerField())
    selected_answers = serializers.ListField(child=serializers.CharField())

    def validate(self, data):
        science_id = data.get('science_id')
        test_ids = data.get('test_ids')
        selected_answers = data.get('selected_answers')

        if len(test_ids) != len(selected_answers):
            raise serializers.ValidationError("Test IDs va selected answers soni bir xil bo'lishi kerak.")

        science = Science.objects.filter(id=science_id).first()
        if not science:
            raise serializers.ValidationError("Berilgan fan mavjud emas.")

        tests = Test.objects.filter(id__in=test_ids)
        if tests.count() != len(test_ids):
            raise serializers.ValidationError("Ba'zi testlar mavjud emas yoki noto'g'ri fan tanlangan.")

        for test in tests:
            if test.science.id != science_id:
                raise serializers.ValidationError("Ba'zi testlar noto'g'ri fan bilan bog'langan.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        science_id = validated_data.get('science_id')
        test_ids = validated_data.get('test_ids')
        selected_answers = validated_data.get('selected_answers')

        science = Science.objects.get(id=science_id)
        correct_count = 0
        incorrect_count = 0

        for test_id, selected_answer in zip(test_ids, selected_answers):
            test = Test.objects.get(id=test_id)
            is_correct = test.right_answer == selected_answer
            if is_correct:
                correct_count += 1
            else:
                incorrect_count += 1

            ExamTest.objects.create(
                user=user,
                science=science,
                selected_answer=selected_answer,
                is_correct=is_correct
            )

        if incorrect_count > 1:
            return {"status": "Siz ishka kirolmadingiz chunki hatolaringiz 1 donadan kop."}
        else:
            return {"status": "Siz muvaffaqiyatli tarzda ishka kirdingiz."}
