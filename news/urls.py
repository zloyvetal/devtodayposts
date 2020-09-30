from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, CommentsCreateView, CommentsDetalView, \
    CommentsListView, UpvoteUpdateView, UpvoteResetAllView

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('post/view_all/', PostListView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    path('comment/create/', CommentsCreateView.as_view()),
    path('comment/view_all/', CommentsListView.as_view()),
    path('comment/detail/<int:pk>', CommentsDetalView.as_view()),
    path('post/upvote/<int:pk>', UpvoteUpdateView.as_view()),
    path('post/reset_all/', UpvoteResetAllView.as_view())
]
