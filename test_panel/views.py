from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import Test, Science, ExamTest
from .serializers import TestSerializer, ScienceSerializer, ExamTestSerializer
from rest_framework.decorators import action


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdminUser, ]

    def create(self, request, *args, **kwargs):
        science_id = request.data.get('science')
        if science_id:
            science = Science.objects.get(id=science_id)
            test_count = Test.objects.filter(science=science).count()
            if test_count >= 15:
                return Response({"status": "Ushbu fan uchun 15 tadan ortiq test yaratilishi mumkin emas."},
                                status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class ScienceViewSet(viewsets.ModelViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    permission_classes = [IsAdminUser, ]


class ExamTestViewSet(viewsets.ModelViewSet):
    queryset = ExamTest.objects.all()
    serializer_class = ExamTestSerializer
    permission_classes = [IsAuthenticated, ]

    # def get(self, request):
        # user =

    def get_queryset(self):
        user = self.request.user
        return ExamTest.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.test_count >= 2:
            return Response({"error": "Siz 2 marta test yechgansiz, sizga boshqa mumkin emas."},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def submit_answers(self, request):
        user = request.user
        exam_tests = ExamTest.objects.filter(user=user)
        if exam_tests.count() < Test.objects.count():
            return Response({"error": "Barcha testlarni yeching."}, status=status.HTTP_400_BAD_REQUEST)

        incorrect_answers = exam_tests.filter(is_correct=False).count()
        if incorrect_answers > 1:
            user.test_count += 1
            user.save()
            return Response({"result": ("Siz testda 1 ta dan kop hato qildingiz va siz ishka kirolmadingiz. "
                                       "Lekin hali kayfiyati tushurmang agar yana 1 ta imkoniyatiz"
                                        " bo'lsa boshqatan topshirolisiz")})

        user.test_count += 1
        user.save()
        return Response({"result": "Tabriklaymiz, siz testdan muvaffaqiyatli o'tdingiz!"})
