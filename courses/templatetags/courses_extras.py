from django import template
from courses.models import Tutor, Course
from datetime import datetime

register = template.Library()

@register.assignment_tag
def get_modal_height(tutor_id):
    height = 1328
    tutor = Tutor.objects.get(id=tutor_id)
    if tutor.comment_set.count() == 0:
        height -= 326
    if not tutor.video:
        height -= 506
    return height


@register.assignment_tag
def get_new_course_price(course_id):
    course = Course.objects.get(id=course_id)
    if course.course_discount and course.course_discount.date_start <= datetime.now().date() <= course.course_discount.date_finish:
        return int(course.course_price * (1-course.course_discount.discount))
    else:
        return None


@register.filter
def percentage(value):
    return '{0:.0%}'.format(value)