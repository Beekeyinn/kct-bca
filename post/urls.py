from django.urls import path
from post.views import (
    create_post,
    post_edit,
    post_delete,
    PostCreateView,
    PostEditView,
    PostDeleteView,
)

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:id>/edit/", PostEditView.as_view(), name="post-edit"),
    path("delete/", PostDeleteView.as_view(), name="post-delete"),
]
