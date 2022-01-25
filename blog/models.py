from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"post_id": self.id})

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]
