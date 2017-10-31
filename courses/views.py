# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response, redirect, render
from django.core.context_processors import csrf
from django.core.mail import EmailMessage

# Create your views here.

def p_index(request):
    args = {}
    args.update(csrf(request))
    tutors = Tutor.objects.filter(actual=True).order_by('?')
    args['tutors'] = tutors
    args['comments'] = Comment.objects.filter(actual=True).order_by('?')
    return render_to_response('index.html', args)


def p_contacts(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('contacts.html', args)


def p_about(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('ocenter.html', args)


def get_comments(request):
    args = {}
    args.update(csrf(request))
    args['comments'] = Comment.objects.filter(actual=True).order_by('?')
    return render_to_response('ucheniki.html', args)


def p_courses(request):
    args = {}
    args.update(csrf(request))
    courses = Course.objects.filter(actual=True)
    subjects = Subject.objects.all()
    if request.POST:
        args['course_type_cat'] = course_type_cat = request.POST.get('d1', None)
        if course_type_cat is not None:
            course_types = CourseType.objects.filter(category=course_type_cat).filter(actual=True)
            courses = courses.filter(course_type__in=course_types)
        args['selected_subjects'] = selected_subjects = [int(x) for x in request.POST.getlist('c1')]
        if len(selected_subjects) != 0:
            print selected_subjects
            courses = courses.filter(course_type__subject__in=selected_subjects)
    args['courses'] = sorted(courses, key=lambda c: c.myorder())
    args['subjects'] = subjects
    return render_to_response('kurskonf.html', args)


def get_tutors(request):
    args = {}
    args.update(csrf(request))
    tutors = Tutor.objects.filter(actual=True)
    args['subjects'] = Subject.objects.filter(actual=True)
    if request.POST:
        subj = request.POST.get('cc', None)
        subject = Subject.objects.get(id=subj)
        tutors = tutors.filter(subject__in=[subject])
        args['selected_subj'] = subject
    args['tutors'] = tutors
    #args[]
    return render_to_response('prepodi.html', args)


def get_course(request, course_id):
    args = {}
    args.update(csrf(request))
    program = []
    course = Course.objects.get(id=course_id)
    i = 0
    while i < len(course.program.splitlines())-1:
        program.append([course.program.splitlines()[i], course.program.splitlines()[i+1]])
        i += 2
    args['course'] = course
    args['program'] = program
    args['comments'] = Comment.objects.all()
    #args['discount'] = int(round(((float(course.course_price-course.course_price_new)/course.course_price_new) * 100)))
    return render_to_response('kurs.html', args)


def get_subject(request, subject_id):
    args = {}
    args.update(csrf(request))
    args['subject'] = subject = Subject.objects.get(id=subject_id)
    courses = Course.objects.filter(course_type__subject=subject).filter(actual=True)
    print courses
    args['courses'] = sorted(courses, key=lambda c: c.myorder())
    args['tutors'] = Tutor.objects.filter(actual=True).filter(subject=subject)
    args['description_top'] = subject.description.splitlines()[0]
    args['description'] = subject.description.splitlines()[1:]
    return render_to_response('predmet.html', args)


def p_stoimost(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('stoimosti.html', args)


def p_system(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('system.html', args)


def p_thanks(request):
    args = {}
    args.update(csrf(request))
    name = request.POST.get('name', None)
    phone = request.POST.get('tel', None)
    email = request.POST.get('email', None)
    if name is not None and phone is not None:
        message = u"Имя: " + name + u"\nТелефон: " + phone
        if email is not None:
            message += u"\nEmail: " + email
        msg = EmailMessage(u'[egechallenge.ru] Новый лид с сайта',
                           message, to=['lead@egechallenge.ru'])
        msg.send()
    return render_to_response('thanks.html', args)


def get_article(request, article_id):
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    args['other_articles'] = Article.objects.exclude(id=article_id).order_by('-publication_date')[:2]

    return render_to_response('blog_page.html', args)


def p_blog(request):
    args = {}
    args['articles'] = Article.objects.all().order_by('-publication_date')[:10]
    return render_to_response('blog.html', args)