from django.urls import path
from .views import post_comment_create_and_list_view

app_names = 'posts'

urlpatterns = [
    path('', post_comment_create_and_list_view, name='main-post-view'),
]