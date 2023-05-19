from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 200)
    kasutajad = models.ManyToManyField(User)
    image = models.TextField()
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.CharField(max_length=200)
    image = models.TextField()
    def __str__(self):
        return self.title

class LessonCompleted(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    def __str__(self):
        return str(self.lesson)

class Question(models.Model):
    question = models.CharField(max_length=200)
    def __str__(self):
        return self.question
    