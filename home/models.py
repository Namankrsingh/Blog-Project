from django.db import models
from django.contrib.auth.models import User
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        abstract = True 

class Blog(BaseModel):  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Comment(BaseModel):  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    blog_id = models.ForeignKey("home.Blog", on_delete=models.CASCADE, related_name="comments")  
    comment_text = models.TextField(default="")

    def __str__(self):
        return f"{self.user_id.username} - {self.comment_text[:20]}"

