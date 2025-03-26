from django.urls import path
from home.views import BlogView, PublicBlogView, CommentView, AllCommentsView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog-list'),  
    path('publicblogs/', PublicBlogView.as_view(), name='public-blog-list'), 
    path('blogs/comments/', CommentView.as_view(), name='comment-list'),  
    path('comments/', AllCommentsView.as_view(), name='all-comments'),  
]
