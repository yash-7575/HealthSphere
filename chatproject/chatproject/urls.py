from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chat_room, name='chat_room'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'), # Add this line
]