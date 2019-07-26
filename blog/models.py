from django.db import models

# Create your models here.

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length =200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    
    def __str__ (self) :
        return self.title
    def summary(self):
        return self.body[:20]
    
class BlogComent(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    def approve(self):
        self.approved_comment =True
        self.save()