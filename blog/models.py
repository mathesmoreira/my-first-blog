from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #models.CharField – this is how you define text with a limited number of characters.
    title = models.CharField(max_length=200)

    #models.TextField – this is for long text without a limit. Sounds ideal for blog post content
    text = models.TextField()

    #models.DateTimeField – this is a date and time.
    created_date = models.DateTimeField(default=timezone.now)

    #models.ForeignKey – this is a link to another model.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title