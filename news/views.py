from django.shortcuts import render
from news.models import News

# Create your views here.
def home_page(request):
    editor_picks = News.objects.filter(is_editorial=True)
    trending_news = News.objects.all().order_by('-views_count')[:4]
    editor_picks_new = News.objects.filter(is_editorial=True)[:4]
    popular_news= News.objects.all().order_by('views_count')[:5]
    recent_news= News.objects.all().order_by('created_date')[:5]
    context = {
        "welcome" : "welcome to my custom page: dhoom tanananananaa",
        "editorial" : editor_picks,
        "trending_news" : trending_news, 
        "editor_picks_new" : editor_picks_new,
        "popular_news" : popular_news,
        "recent_news" :recent_news
                        }
    templates= "base.html"
    return render(request, templates, context)  

def category(request, category_id):
    news_category = News.objects.filter(category=category_id)
    context = {
            'news_category' : news_category   
                      }
    return render(request, 'pages/categories.html',context)

