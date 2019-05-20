

from django.db import models
from django.utils import timezone
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    #description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    description2 = RichTextUploadingField(blank=True, null=True, config_name='special')
    is_public = models.BooleanField(default=False)
#    새로운 필드 추가 makemigrations
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

