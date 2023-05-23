from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("""<h1>A little bit about us! 
                        We are the best restaurant in the whole
                        Manchester!</h1>""")
