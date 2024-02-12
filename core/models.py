from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings
from django.utils.text import slugify




class Series(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Message(models.Model):

    class MessageObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published', 'Published'),
    )

    series = models.ForeignKey(Series, related_name='message', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True)
    file = models.FileField(upload_to='uploads/message/', blank=True)
    flyer = models.ImageField(upload_to='uploads/message_flyer/', blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='date', blank=True)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=options, default='draft')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    objects = models.Manager()
    message_objects = MessageObjects()
        

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

