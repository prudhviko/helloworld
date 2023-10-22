from django.shortcuts import render,HttpResponse

def homepageview(request):
    return HttpResponse("Hello, World...")