from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SearchTerm(models.Model):
    tracking_id = models.CharField(max_length=200, default='')
    q = models.CharField(max_length=120)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.q


class ImageSearchTools(models.Model):
    tracking_id = models.CharField(max_length=200, default='')
    file_input = models.ImageField(upload_to ='search_images')
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str('{}, {}'.format(self.user, self.search_date))


