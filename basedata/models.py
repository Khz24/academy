from django.db import models


# Create your models here.


class Level(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'مقاطع تحصیلی'
        verbose_name = 'مقطع تحصیلی'


class Student(models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30, null=True)
    student_id = models.IntegerField(null=False, unique=True)
    student_level = models.ForeignKey(Level, on_delete=models.CASCADE, null=False)
    sex = models.CharField(max_length=3, null=False, default='مرد')
    birth_date = models.DateField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'دانش آموزان'
        verbose_name = 'دانش آموز'


class Course(models.Model):
    name = models.CharField(max_length=30, null=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'دروس'
        verbose_name = 'درس'
        ordering = ['level', 'name']
        unique_together = ('name', 'level')
        index_together = ('name', 'level')


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models)
    course = models.ForeignKey(Course, on_delete=models)

    def __str__(self):
        return self.student


class StudentProfile(models.Model):
    student = models.ForeignKey(Student, on_delete=models)
    course = models.ForeignKey(Course, on_delete=models)

    def __str__(self):
        return self.student

