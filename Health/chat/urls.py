from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.chat_room, name='community'),
    path('accounts/', include('django.contrib.auth.urls')),
]