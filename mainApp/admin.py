from django.contrib import admin

from .models import Lesson,Teacher,DatesOfWeek,Comment




class DatesOfWeekInline(admin.TabularInline):
    model = DatesOfWeek
    extra = 0
    min_num = 1
    max_num = 7

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class LessonAdmin(admin.ModelAdmin):
    inlines = [DatesOfWeekInline, CommentInline]


    
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Teacher)