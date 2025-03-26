from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.id") 
    blog_id = serializers.ReadOnlyField(source="blog_id.uid")
    created_by = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Comment
        fields = ['uid', 'user_id', 'blog_id', 'created_at', 'comment_text', 'created_by']

class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='user_id.username') 
    user_id = serializers.ReadOnlyField(source="user_id.id")

    class Meta:
        model = Blog
        fields = ['uid', 'user_id', 'created_at', 'title', 'blog_text', 'main_image', 'created_by']
