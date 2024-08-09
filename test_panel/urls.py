from django.urls import path, include

from .views import ScienceListView, ScienceDetailView, ScienceTestsView, ExamTestPostApiView


urlpatterns = [
    path('science/list/', ScienceListView.as_view(), name='science-list'),
    path('sciences/<int:pk>/', ScienceDetailView.as_view(), name='science-detail'),
    path('sciences/<int:science_id>/tests/', ScienceTestsView.as_view(), name='science-tests'),
    path('pass_exam/', ExamTestPostApiView.as_view()),
]
