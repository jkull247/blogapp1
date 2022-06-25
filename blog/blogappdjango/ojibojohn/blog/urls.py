from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", blogCreativeViews.PostListView.as_view(), name="all"),
    path("create/", blogCreativeViews.PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>", blogCreativeViews.PostDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>", blogCreativeViews.PostUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>", blogCreativeViews.PostDetailView.as_view(), name="post_detail"),

]