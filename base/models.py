from django.db import models

class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    tel_number = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date_of_request = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"message from {self.first_name} {self.last_name}"
    


class Project(models.Model):
    title = models.CharField(max_length=200)
    brief = models.CharField(max_length=200)
    thumnail = models.ImageField(upload_to='uploads/')
    video = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.title

class Testimony(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}'s Testimony"
    