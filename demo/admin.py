from django.contrib import admin

from demo.models import Student, HomeworkTask, HomeworkSolution, Course


class HomeworkSolutionInline(admin.TabularInline):
    model = HomeworkSolution
    extra = 0


class CourseInline(admin.TabularInline):
    model = Course.students.through
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    inlines = [CourseInline, HomeworkSolutionInline]


@admin.register(HomeworkTask)
class HomeworkTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    search_fields = ['text']
    inlines = [HomeworkSolutionInline]


@admin.register(HomeworkSolution)
class HomeworkSolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'task']
    search_fields = ['text']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
