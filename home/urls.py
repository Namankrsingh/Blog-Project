from django.urls import path
from home.views import BlogView, PublicBlogView, CommentView, AllCommentsView, CommentDetailView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog-list'),  
    path('blogs/<uuid:blog_id>/', BlogView.as_view(), name='blog-detail'),  
    path('publicblogs/', PublicBlogView.as_view(), name='public-blog-list'), 
    path('blogs/comments/', CommentView.as_view(), name='comment-list'), 
    path('blogs/comments/<uuid:comment_id>/', CommentDetailView.as_view(), name='comment-detail'),  
    path('comments/', AllCommentsView.as_view(), name='all-comments'),  
]
