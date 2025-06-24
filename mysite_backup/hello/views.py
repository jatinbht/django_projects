from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    resp = HttpResponse("view count=" + str(num_visits))

    resp.set_cookie('dj4e_cookie', 'dfcb89d6', max_age=1000)

    return resp