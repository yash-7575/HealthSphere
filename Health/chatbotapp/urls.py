from django.urls import path
from chatbotapp.views import chatbot_view, chatbot_api

urlpatterns = [
    path("chatbotapp/", chatbot_view, name="chatbotapp"),
    path("api/chatbot/", chatbot_api, name="chatbot_api"),
]
