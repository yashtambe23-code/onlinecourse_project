from django.contrib import admin
from .models import Instructor, Learner, Course, Lesson, Enrollment, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
