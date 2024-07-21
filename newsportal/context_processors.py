from news.models import Category


def category(request):
    cat = Category.objects.all()
    return {
        "category" : cat
     }