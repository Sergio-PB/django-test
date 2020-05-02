from django.shortcuts import render
from django.http.response import HttpResponse

def basic_resp(req):
    if req.method == 'GET':
        return HttpResponse('answer to get')
    if req.method == 'POST':
        return HttpResponse('answer to post')