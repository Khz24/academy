from django.contrib import admin
from .models import Student, Level, Course, StudentLevel


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'family', 'status', 'sex',)
    search_fields = ('student_id',)
    list_filter = ('sex', 'status',)
    ordering = ('student_id',)
    list_per_page = 10


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level_id', )
    search_fields = ('level_id', )
    list_filter = ('level_id',)
    ordering = ('level_id', 'name')


admin.site.register(Level,)
admin.site.register(Course, CourseAdmin,)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentLevel)

