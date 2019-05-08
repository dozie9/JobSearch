from django import template
from home.scripts import jobhunterparser_mine
from home.models import Bookmark

register = template.Library()

f = open("home/resumeprjct.txt", encoding='utf-8')
you = f.read()
f.close()

@register.simple_tag
def match(resume, job_desc):
    value = jobhunterparser_mine.get_info(job_desc, resume) * 10
    value = round(value, 2)
    if value >= 100:
        value = 99
    return value

@register.filter
def saved(link, user):
    if Bookmark.objects.filter(user=user, link=link):
        return True
    else:
        return False