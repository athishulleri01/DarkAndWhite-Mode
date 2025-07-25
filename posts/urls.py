from django.urls import path
from .views import PostListView, PostDetailView, PostViewListing

app_name = 'Posts'

urlpatterns = [
    path("", PostListView.as_view() , name="main"),
    # path("", PostViewListing , name="main"),
    path("<pk>/", PostDetailView.as_view() , name="detail"),
]
