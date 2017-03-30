from django.conf.urls import include, url


urlpatterns = [
    # url(r'^1/', 'EventApp.views.get_data'),
    url(r'^contacts/$', 'courses.views.p_contacts'),
    url(r'^about/$', 'courses.views.p_about'),
    url(r'^course/(?P<course_id>\d+)/$', 'courses.views.get_course'),
    url(r'^courses/$', 'courses.views.p_courses'),
    url(r'^tutors/$', 'courses.views.get_tutors'),
    url(r'^students/$', 'courses.views.get_comments'),
    url(r'^subject/(?P<subject_id>\d+)/$', 'courses.views.get_subject'),
    url(r'^stoimost/$', 'courses.views.p_stoimost'),
    url(r'^system/$', 'courses.views.p_system'),
    url(r'^thanks/$', 'courses.views.p_thanks'),
    url(r'^article/(?P<article_id>\d+)/$', 'courses.views.get_article'),
    url(r'^blog/$', 'courses.views.p_blog'),
    url(r'^$', 'courses.views.p_index'),
]
