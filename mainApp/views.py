from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .models import Lesson,Teacher,DatesOfWeek,Comment




class LessonsView(generic.ListView):
    template_name = 'mainApp/lesson_list.html'
    context_object_name = 'latest_lesson_list'
    model = Lesson

    def get_queryset(self):
        return Lesson.objects.all()


class LessonView(generic.ListView):
    template_name = 'mainApp/lesson.html'
    context_object_name = 'latest_lesson_list'
    model = Lesson





@csrf_exempt
def liked(request):
    this_name = request.POST['lessonName']
    this_lesson = Lesson.objects.filter(lessonName = this_name).get()
    # this_lesson.like = request.POST['liked']
    this_lesson.like += 1
    this_lesson.save()

    return JsonResponse({
        'status': 'ok',
    }, encoder=json.JSONEncoder)