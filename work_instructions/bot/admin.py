from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']

class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(User)
admin.site.register(Task, TaskAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Bug, BugAdmin)
