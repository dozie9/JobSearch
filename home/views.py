from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.forms import HomeForm
import json, ast, subprocess, sys, os
from home.models import Bookmark

#from home import JobSearch
from django.urls import reverse


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        # form = HomeForm()
        # posts = Post.objects.all()
        # print(posts)
        # args = {'form':form, 'posts':posts}
        return render(request, self.template_name)

    def post(self,request):
        school_major = request.POST['school_major']
        job_type = request.POST['job_type']
        resume = request.POST['resume']
        location = request.POST['location']
        q = school_major + ' ' + job_type + ' ' + location
        details = subprocess.check_output(["python", "home/scripts/JobSearch.py", q])
        if request.session.get('result'):
            del request.session['result']
        if request.session.get('resume'):
            del request.session['resume']
        if request.session.get('search'):
            del request.session['search']
        if request.session.get('fname'):
            del request.session['fname']
        fname = str(details, "utf-8").split("\n")[0]
        with open("home/temp/" + fname) as f:
            data = f.read()
        request.session['result'] = ast.literal_eval(data)
        request.session['resume'] = resume
        request.session['search'] = q
        request.session['fname'] = fname
        return redirect(reverse('home:result'))


def result_view(request):
    result = request.session.get('result')
    resume = request.session.get('resume')
    fname = request.session.get('fname')
    q = request.session.get('search')
    data = False
    start = 0
    end = 10
    page_num = 1
    if request.GET.get("page"):
        page_num = int(request.GET['page'])
        if page_num > 1:
            page_num = page_num
            start = 10 * (page_num)
            end = (10 * (page_num + 1))
        else:
            page_num = 1
    search_result_full = result
    length = len(search_result_full)
    page_data = {}
    page = False
    if length > 10:
        search_result = search_result_full[start:end]
        page = True
        n = int(length / 10)
        page_data['number'] = [1] * n
        page_data['state'] = page_num
    else:
        search_result = search_result_full
    try:
        os.remove("home/temp/" + fname)
    except:pass
    return render(request, 'home/search_result.html', locals())


def bookmark(request):
    header = request.POST['header']
    company = request.POST['company']
    link = request.POST['link']
    if Bookmark.objects.filter(user=request.user, link=link):
        return JsonResponse({"status":2})
    else:
        book = Bookmark.objects.create(title=header, company=company, link=link, user=request.user, timestamp=datetime.today())
        book.save()
        return JsonResponse({'status': 1})

@login_required
def saved_jobs(request):
    jobs = Bookmark.objects.filter(user=request.user)
    return render(request, 'home/saved_jobs.html', locals())