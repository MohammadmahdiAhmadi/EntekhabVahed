from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Lesson,Teacher,DatesOfWeek,Comment


class LessonsView(generic.ListView):
    template_name = 'mainApp/lesson.html'
    context_object_name = 'latest_lesson_list'

    def get_queryset(self):
        return Lesson.objects.all()


def vote(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    selected_like = lesson.get(pk=request.POST['lesson'])
    lesson.like = 222
    selected_like.like = 111
    selected_like.save()



