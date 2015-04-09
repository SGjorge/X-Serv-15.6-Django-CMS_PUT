from django.shortcuts import render
from models import Pages
from django.conf.urls import patterns, include, url
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def contentapp(request,resourceName):
    response = '<h1>Welcome to Contentapp</h1>'
    if request.method == "GET":
        try:
            content = Pages.objects.get(name=resourceName)
            return HttpResponse(response + content.page)
        except Pages.DoesNotExist:
            response += '<body> GET </body>'
            form = "<form action='' method='POST'>\n"
            form += "Page: <input type='text' name='name' value=''><br>\n"
            form += "Content page: <input type='text' name='page'><br>\n"
            form += "<input type='submit' value='enviar'>\n"
            form += "</form>\n"
            response += form
            return HttpResponse(response)
    elif request.method == "POST":
        response += '<body> POST </body>' 
        newPage = Pages(name=request.POST['name'], page=request.POST['page'])
        newPage.save()
        response += "--Page: " + request.POST['name'] 
        response += ", Content Page: " + request.POST['page']
        return HttpResponse(response)
    elif request.method == "PUT":
        response += '<body> PUT </body>'
        (namePage, Page) = request.body.split(';')
        newPage = Page(name=namePage, page=Page)
        newPage.save()
        response += "--Page: " + request.POST['name'] 
        response += ", Content Page: " + request.POST['page']
        return HttpResponse(response)
    else:
        response += '<body> Fucking else </body>'
        return HttpResponse(response)
