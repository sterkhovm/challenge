# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class CourseFormatInline(admin.TabularInline):
    model = CourseFormat
    extra = 0


@admin.register(CourseFormatCategory)
class CourseFormatCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    inlines = [
        CourseFormatInline,
    ]


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'unicode_sort', 'education', 'experience_view', 'hobby_view',)
    list_display_links = ('id', 'unicode_sort')
    list_filter = ['subject', 'actual']

    def experience_view(self, obj):
        return obj.experience[:30] + "..."

    def hobby_view(self, obj):
        return obj.hobby[:30] + "..."

    hobby_view.short_description = 'Увлечения'
    experience_view.short_description = 'Опыт'


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')
    list_display_links = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__', 'subject', 'tutor', 'date_start', 'course_format', 'weekdays',)
    list_display_links = ('id', '__unicode__')
    list_filter = ['course_format']
    date_hierarchy = 'date_start'

    def subject(self, obj):
        return obj.course_type.subject.name

    subject.short_description = 'Дисциплина'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'tutor', 'course_type')
    list_display_links = ('id', 'client_name')
    list_filter = ['client_type']


@admin.register(CourseDiscount)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_start', 'date_finish', 'discount')
    list_display_links = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'publication_date')
    date_hierarchy = 'publication_date'