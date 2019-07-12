from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me' : 'I am from views.py'}
    return render (request,'first_app/index.html',context=my_dict)
def help(request):
    x = {'insert_me' : 'this is from help'}
    return render (request,'first_app/help.html')#,context=x)
def main(request):
    # x = {'insert_me' : 'this is from help'}
    return HttpResponse("this is main page")
