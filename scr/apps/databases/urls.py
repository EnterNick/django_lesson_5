from django.urls import path

from .views import CreatePostView, PostsView, PostView, CreateCommentView

urlpatterns = [
    path('add/', CreatePostView.as_view(), name='add_post'),
    path('', PostsView.as_view(), name='posts'),
    path('<int:pk>/', PostView.as_view(), name='post-detail'),
    path('<int:pk>/leave_comment/', CreateCommentView.as_view(), name='comment'),
]
