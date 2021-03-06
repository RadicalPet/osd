"""osd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexView, email, success
from .business.views import IndexView as BusinessIndexView
from .community.views import IndexView as CommunityIndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^community/', CommunityIndexView.as_view(), name='community_home'),
    url(r'^business/', BusinessIndexView.as_view(), name='business_home'),
    url(r'^email/$', email, name='email'),
    url(r'^success/$', success, name='success'),
]
