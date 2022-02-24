from django.db import models
from django.utils.translation import gettext as _


class Student(models.Model):
    # id
    name = models.CharField(max_length=100)
    # tasks
    # solutions
    # courses

    def __str__(self):
        return self.name


class HomeworkTask(models.Model):
    # id
    text = models.TextField()
    students = models.ManyToManyField(Student, related_name='tasks', through='HomeworkSolution')
    # solutions

    def __str__(self):
        return self.text


class HomeworkSolution(models.Model):
    class Meta:
        verbose_name = _('solution')
        verbose_name_plural = _('solutions')

    # id
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='solutions')
    task = models.ForeignKey(HomeworkTask, on_delete=models.CASCADE, related_name='solutions')
    text = models.TextField()

    def __str__(self):
        return self.text


class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses', blank=True)
    homework_tasks = models.ManyToManyField(HomeworkTask, related_name='courses', blank=True)

    def __str__(self):
        return self.title
