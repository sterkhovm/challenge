# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from datetime import datetime
from redactor.fields import RedactorField

# Create your models here.



class Subject(models.Model):
    class Meta():
        ordering = ['sort_field']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    name = models.CharField(max_length=200, verbose_name='Название')
    name_dat = models.CharField(max_length=200, verbose_name='Название в дательном падеже')
    description = models.TextField(verbose_name='Описание на сайт')
    name_eng = models.CharField(max_length=100, verbose_name='Короткое название на английском', null=True)
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    sort_field = models.IntegerField(verbose_name='Поле сортировки')

    def __unicode__(self):
        return self.name


class Address(models.Model):
    class Meta():
        ordering = ['name']
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    name = models.CharField(max_length=400, verbose_name='Название')
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        return self.name


class CourseFormatCategory(models.Model):
    class Meta():
        ordering = ['name']
        verbose_name = 'Формат курса'
        verbose_name_plural = 'Форматы курсов'

    name = models.CharField(max_length=200, verbose_name='Название')
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        return self.name


class CourseFormat(models.Model):
    class Meta():
        ordering = ['name']
        verbose_name = 'Формат курса'
        verbose_name_plural = 'Форматы курсов'

    name = models.CharField(max_length=200, verbose_name='Название')
    discription = models.TextField(verbose_name='Описание формата')
    course_format_category = models.ForeignKey(CourseFormatCategory)
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        return self.name


class Tutor(models.Model):
    class Meta():
        ordering = ['last_name', 'first_name']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=200, verbose_name='Отчество')
    subject = models.ManyToManyField(Subject, verbose_name='Преподаваемые дисциплины')
    course_format_category = models.ManyToManyField(CourseFormatCategory, verbose_name='Форматы занятий')
    education = models.CharField(max_length=400, verbose_name='Образование')
    educ = models.CharField(max_length=20, verbose_name='Короткое название ВУЗа')
    experience_years = models.CharField(max_length=100, verbose_name='Опыт работы (лет)')
    experience = models.TextField(verbose_name='Опыт')
    hobby = models.TextField(verbose_name='Увлечения')
    photo = models.ImageField(verbose_name='Фото')
    video = models.URLField(verbose_name='Ссылка на видео', null=True, blank=True)
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        return self.last_name + " " + self.first_name

    def unicode_sort(self):
        return self.__unicode__()

    unicode_sort.admin_order_field = 'last_name'
    unicode_sort.short_description = 'Преподаватель'


class CourseType(models.Model):
    class Meta():
        ordering = ['name']
        verbose_name = 'Вид курса'
        verbose_name_plural = 'Виды курсов'

    name = models.CharField(max_length=200, verbose_name='Расшифровка курса')
    subject = models.ForeignKey(Subject, verbose_name='Дисциплина')
    category = models.CharField(max_length=200, verbose_name='Категория курса', choices=(('1', 'ОГЭ'),
                                                                                         ('2', 'ЕГЭ'),
                                                                                         ('3', 'Олимпиады'),
                                                                                         ('4', 'Спецкурс')))
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        return self.subject.name + " - " + self.name


class CourseAction(models.Model):
    class Meta():
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    name = models.CharField(max_length=200, verbose_name='Название акции')
    name_eng = models.CharField(max_length=200, verbose_name='Короткое название акции на английском')

    def __unicode__(self):
        return self.name


class CourseDiscount(models.Model):
    class Meta():
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    name = models.CharField(max_length=200, verbose_name='Название акции')
    date_start = models.DateField(verbose_name='Дата начала акции')
    date_finish = models.DateField(verbose_name='Дата окончания акции')
    discount = models.FloatField(verbose_name='Доля скидки', default=0)

    def __unicode__(self):
        return self.name



class Course(models.Model):
    class Meta():
        #ordering = ['id']
        verbose_name = 'Учебный курс'
        verbose_name_plural = 'Учебные курсы'

    course_header = models.CharField(max_length=200, verbose_name='Заголовок курса', null=True)
    course_type = models.ForeignKey(CourseType, verbose_name='Вид курса')
    tutor = models.ForeignKey(Tutor, verbose_name='Преподаватель')
    duration = models.IntegerField(verbose_name='Длительность (нед.)')
    time_start = models.TimeField(verbose_name='Время начала занятий')
    time_finish = models.TimeField(verbose_name='Время окончания занятий')
    weekdays = models.CharField(max_length=200, verbose_name='Дни занятий')
    date_start = models.DateField(verbose_name='Старт группы', null=True, blank=True)
    course_format = models.ForeignKey(CourseFormat, verbose_name='Формат')
    frequency = models.IntegerField(verbose_name='Частота (раз в нед.)')
    class_duration = models.IntegerField(verbose_name='Длина занятия (мин.)')
    class_qtty = models.CharField(max_length=100, verbose_name='Количество занятий')
    discription = models.TextField(verbose_name='Описание курса')
    program = models.TextField(verbose_name='Программа курса')
    program_description = models.TextField(verbose_name='Описание программы курса')
    address = models.ForeignKey(Address, verbose_name='Адрес')
    course_price = models.IntegerField(verbose_name='Стоимость курса', default=6900)
    place_left = models.IntegerField(verbose_name='Мест осталось', default=7)
    course_action = models.ForeignKey(CourseAction, verbose_name='Акция', null=True, blank=True)
    course_discount = models.ForeignKey(CourseDiscount, verbose_name='Скидка', null=True, blank=True)
    course_class = models.CharField(max_length=200, verbose_name='Класс', choices=(('class8 class9', '8-9 классы'),
                                                                                         ('class10 class11', '10-11 классы')))
    program_file = models.FileField(verbose_name='Программа в PDF', upload_to='course_programs/', null=True, blank=True)
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        try:
            return self.course_type.name + " - " + self.date_start.strftime('%d.%m.%Y')
        except:
            return self.course_type.name

    def myorder(self):
        if self.date_start:
            return abs(datetime.now().date() - (self.date_start if self.date_start
                                        else datetime.strptime('1900-01-01', '%Y-%m-%d').date()))
        else:
            return datetime.now().date() - datetime.now().date()


class Comment(models.Model):
    class Meta():
        ordering = ['id']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    name = models.CharField(max_length=200, verbose_name='Название отзыва')
    client_name = models.CharField(max_length=300, verbose_name='Имя клиента')
    client_type = models.CharField(max_length=200, verbose_name='Статус', choices=(('1', 'Ученик'),
                                                                                   ('2', 'Родитель')))
    photo = models.ImageField(verbose_name='Фото клиента')
    client_link = models.URLField(verbose_name='Ссылка на ВК')
    client_achievement = models.TextField(verbose_name='Результаты ЕГЭ')
    client_was_enrolled_at = models.CharField(max_length=300, verbose_name='Поступил')
    client_gender = models.CharField(max_length=1, verbose_name='Пол клиента', choices=(('1', 'М'),
                                                                                   ('2', 'Ж')))
    tutor = models.ForeignKey(Tutor, null=True, blank=True,  verbose_name='Преподаватель')
    course_type = models.ForeignKey(CourseType, null=True, blank=True, verbose_name='Вид курса')
    text = models.TextField(verbose_name='Текст отзыва')
    full_text = models.TextField(verbose_name='Полный текст отзыва')
    actual = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    def __unicode__(self):
        return "Отзыв - " + self.client_name

class Article(models.Model):
    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    name = models.CharField(verbose_name='Название статьи', max_length=200)
    publication_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.CharField(max_length=200, verbose_name='Автор')
    main_image = models.ImageField(verbose_name='Главное изображение статьи')
    short_text = models.TextField(verbose_name='Короткий текст статьи')
    content = RedactorField(verbose_name=u'Текст статьи')

    def __unicode__(self):
        return self.name