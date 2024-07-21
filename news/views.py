from django.shortcuts import render
from news.models import News

# Create your views here.
def home_page(request):
    editor_picks = News.objects.filter(is_editorial=True)
    context = {
        "welcome" : "welcome to my custom page: dhoom tanananananaa",
        "editorial" : editor_picks
                }
    templates= "base.html"
    return render(request, templates, context)  

