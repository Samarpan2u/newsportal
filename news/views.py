from django.shortcuts import render, redirect
from news.models import News
from datetime import datetime
from news.forms import ContactUsForm

# Create your views here.
def home_page(request):
    current_datetime = datetime.now()
    editor_picks = News.objects.filter(is_editorial=True)
    trending_news = News.objects.all().order_by('-views_count')[:4]
    editor_picks_new = News.objects.filter(is_editorial=True)[:4]
    popular_news= News.objects.all().order_by('views_count')[:5]
    recent_news= News.objects.all().order_by('created_date')[:5]
    context = {
        "welcome" : "welcome to my custom page: dhoom tanananananaa",
        "date_time" : current_datetime,
        "editorial" : editor_picks,
        "trending_news" : trending_news, 
        "editor_picks_new" : editor_picks_new,
        "popular_news" : popular_news,
        "recent_news" :recent_news
                        }
    templates= "base.html"
    return render(request, templates, context)  

def category(request, category_id):
    current_datetime = datetime.now()
    news_category = News.objects.filter(category=category_id)
    context = {
            'news_category' : news_category, 
             'date_time' : current_datetime
                      }
    return render(request, 'pages/categories.html',context)

def contact_info(request):
    form = ContactUsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    else:
        print (form.errors)

    return render(request, 'pages/contacts.html')
