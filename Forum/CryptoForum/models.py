from django.db import models


# parent model
class Forum(models.Model):
    name = models.CharField(max_length=200, default="anonymous")
    topic = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, default=topic)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)


# child model because of a foreignkey from Forum class
class Comments(models.Model):
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.forum)
