from django.contrib import admin
from .models import Student, Level, Course, StudentCourse, StudentProfile


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'family', 'status', 'sex',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(StudentProfile)
