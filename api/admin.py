from django.contrib import admin
from .models import Quiz, Question, Option, Student, Topic, Result, ResultDetail
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Student)
admin.site.register(Topic)
admin.site.register(Result)
admin.site.register(ResultDetail)