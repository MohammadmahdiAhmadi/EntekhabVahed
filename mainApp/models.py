from django.db import models

import datetime



class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=0)

    genderList = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = models.CharField(max_length=50, choices=genderList, default='male',)

    lessonTeaching = models.TextField(default='empty')
    days = models.TextField(default='empty')
    educations = models.TextField(default='empty')
    moreDetail = models.TextField(default='empty')


    def __str__(self):
        return self.name



class Lesson(models.Model):
    lessonName = models.CharField(max_length=50)
    vahed = models.PositiveSmallIntegerField()
    collegeName = models.CharField(max_length=50)
    
    genderList = [
        ('mix', 'mix'),
        ('male', 'male'),
        ('female', 'female'),
    ]
    classGender = models.CharField(max_length=10, choices=genderList, default='mix',)
    like = models.PositiveIntegerField(default=0)
    unlike = models.PositiveIntegerField(default=0)
    mianTermDate = models.DateTimeField()
    termDate = models.DateTimeField()

    teacherName = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        primary_key=True,
    )


    def __str__(self):
        return self.lessonName


    # def liking(self):
    #     self.like += 1
    #     self.save()




class DatesOfWeek(models.Model):
    lesson = models.ForeignKey(Lesson,
    on_delete=models.CASCADE)

    weekDaysList = [
        ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه شنبه', 'سه شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنجشنبه', 'پنجشنبه'),
        ('جمعه', 'جمعه'),
    ]
    weekDays = models.CharField(max_length=50, choices=weekDaysList,default='شنبه',)

    beginTime = models.TimeField()
    endTime = models.TimeField()



class Comment(models.Model):
    lesson = models.ForeignKey(Lesson,
    on_delete=models.CASCADE)

    publisherName = models.CharField(max_length=50)
    publishDate = models.DateTimeField()
    text = models.TextField(default='empty')
    like = models.PositiveIntegerField(default=0)
    unlike = models.PositiveIntegerField(default=0)
    