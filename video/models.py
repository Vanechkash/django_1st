from django.db import models




class Video(models.Model):
    name = models.CharField(max_length=150)
    like = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.date)
# Create your models here.
