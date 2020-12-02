from django.urls import path

from . import views

app_name = 'mainApp'

urlpatterns = [
    path('liked/', views.liked, name='liked'),
    path('', views.LessonsView.as_view(), name='lesson_list'),
    path('<slug:lessonName>/', views.LessonView.as_view(), name='lesson'),
]