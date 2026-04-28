from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    text = models.CharField(max_length=200)

class Choice(models.Model):
    text = models.CharField(max_length=100)

class Submission(models.Model):
    student = models.CharField(max_length=100)
