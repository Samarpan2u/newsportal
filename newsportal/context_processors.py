from news.models import Category,SocialMedia


def category(request):
    cat = Category.objects.all()
    return {
        "category" : cat
     }

def social(request):
    social_media = SocialMedia.objects.all().first()
    return {
        "social" : social_media
     }