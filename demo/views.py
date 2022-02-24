from django.shortcuts import render

from demo.models import Course, Student, HomeworkSolution


def courses_view(request):
    context = {
        'courses': Course.objects.prefetch_related('students').all(),
        'solutions': HomeworkSolution.objects.select_related('task').all(),
    }
    return render(request, 'demo/index.html', context)
