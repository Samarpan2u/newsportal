from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {
        "welcome" : "welcome to my custom page: dhoom tanananananaa" 
    }
    templates= "base.html"
    return render(request, templates, context)  

