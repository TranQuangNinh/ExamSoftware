from import_export import resources
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin, ImportMixin, ExportMixin
from .models import *
from tablib import Dataset

# Register your models here.


class UserInfoAdmin(ImportExportModelAdmin):
    list_display = ['user', 'birth_day', 'phone_number', 'address']
    search_fields = ['user__first_name', 'user__last_name']
    fieldsets = (
        (None, {
            'fields': ('user', 'role', 'avatar', 'birth_day', 'phone_number', 'address')
        }),
    )


class SubjectAdmin(ImportExportModelAdmin):
    search_fields = ['subject_name']


class RoleAdmin(ImportExportModelAdmin):
    search_fields = ['role_name']


class ResultAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['user', 'exam', 'question', 'choose_answer']
    search_fields = ['user__first_name', 'user__last_name', 'exam__exam_name']
    fieldsets = (
        (None, {
            'fields': ('user', 'exam')
        }),
    )


class QuestionAdmin(ImportExportModelAdmin):
    list_display = ['question_main', 'question_img',
                    'question_sub', 'subject', 'status']
    search_fields = ['status']


class AnswerAdmin(ImportExportModelAdmin):
    list_display = ['question', 'answer_name']
    search_fields = ['question__question_name', 'answer_name']
    fieldsets = (
        (None, {
            'fields': ('question', 'answer_name', 'answer_img', 'correct_answer')
        }),
    )


class MenuAdmin(ImportExportModelAdmin):
    list_display = ['menu_name', 'menu_icon', 'menu_link']
    search_fields = ['menu_name', 'menu_icon', 'menu_link']


class ExamAdmin(ImportExportModelAdmin):
    list_display = ['exam_name', 'total_time_to_do_exam',
                    'subject', 'batch']
    search_fields = ['exam_name', 'subject__subject_name', 'batch__batch_name']


class ExamResultAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['user', 'exam', 'total_correct_question', 'point', 'rank']
    search_fields = ['user__first_name', 'user__last_name',
                     'exam__exam_name', 'total_correct_question', 'point', 'rank']
    fieldsets = (
        (None, {
            'fields': ('user', 'exam', 'date', 'total_correct_question', 'point', 'rank')
        }),
    )


class BatchResource(resources.ModelResource):
    class Meta:
        model = Batch
        fields = ('id', 'batch_name', 'content',
                  'created_date', 'time_from', 'time_to', 'status', 'show_notifi', 'slug')


class BatchAdmin(ImportExportModelAdmin):
    resource_class = BatchResource
    list_display = ['batch_name', 'content',
                    'created_date', 'time_from', 'time_to', 'status', 'show_notifi']
    search_fields = ['status', 'show_notifi']
    fieldsets = (
        (None, {
            'fields': ('batch_name', 'content', 'created_date', 'time_from', 'time_to')
        }),
    )


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email')


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Exam_Result, ExamResultAdmin)
