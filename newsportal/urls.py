"""
URL configuration for newsportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import home_page, category, contact_info, search, subscribe
from newsportal import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='homepage'),
    path('category/<int:category_id>', category, name='category'),
    path('contacts/', contact_info, name='contactme'),
    path('search/', search, name='search'),
    path('subscribe/',subscribe, name='subscribe')



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
