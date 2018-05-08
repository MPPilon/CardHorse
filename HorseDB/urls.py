"""CardHorse DB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from CardHorse import settings
from HorseDB import views

urlpatterns = [
    # Example: "<domain>/db/"
    path(r'', views.database_homepage, name='database_homepage'),

    # Example: "<domain>/db/ajax_fetch_all_cards/"
    path(r'ajax_fetch_all_cards', views.ajax_fetch_all_cards, name='ajax_fetch_all_cards'),

    # Example: "<domain>/db/admin/acquire_cards/"
    path(r'admin/acquire_cards', views.database_admin_acquire_card_list, name='admin_acquire_cards'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
