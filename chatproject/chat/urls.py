from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chat_room, name='chat_room'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]