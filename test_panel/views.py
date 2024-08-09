from rest_framework import viewsets, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ScienceCreateAPIView(generics.CreateAPIView):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    permission_classes = [IsAdminUser, ]


class ScienceListView(APIView):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if ExamTest.objects.filter(user=user).exists():
            return Response({'detail': 'Siz boshqa test topshira olmaysiz'}, status=status.HTTP_403_FORBIDDEN)

        sciences = Science.objects.all()
        serializer = ScienceSerializer(sciences, many=True)
        return Response(serializer.data)


class ScienceDetailView(generics.RetrieveAPIView):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    permission_classes = [IsAdminUser]


class ScienceTestsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, science_id):
        science = get_object_or_404(Science, id=science_id)
        user = request.user

        if ExamTest.objects.filter(user=user, science=science).exists():
            return Response({'detail': 'Siz boshqa test topshira olmaysiz'}, status=status.HTTP_403_FORBIDDEN)

        tests = science.tests.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)


class ExamTestPostApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        science = Science.objects.get(id=request.data.get('science_id'))

        if ExamTest.objects.filter(user=user, science=science).exists():
            return Response({'detail': 'Siz boshqa test topshira olmaysiz'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ExamTestSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_201_CREATED)