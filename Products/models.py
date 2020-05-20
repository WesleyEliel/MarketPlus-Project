from django.db import models
from django import forms
from django.utils import timezone
from Accounts.models import *
from taggit.managers import TaggableManager


# Create your models here.

# Models Managers
class ProductCategoryManager(models.Manager):
    def all(self):
        return super(ProductCategoryManager, self).filter(active=True)


class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(active=True).filter(featured=True)


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(active=True)


class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(active=True)


class ActiveProductReviewManager(models.Manager):
    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(is_approved=True)


# Models
class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    other_notes = models.TextField(max_length=220)
    category = models.OneToOneField('ProductCategory', null=True, blank=True, on_delete=models.CASCADE)
    normal_price = models.DecimalField(decimal_places=2, max_digits=100, default=6500)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, default=6500)
    quantity_in_stock = models.IntegerField()
    images = models.ManyToManyField('ProductImage')
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    objects = models.Manager()
    is_active = ActiveProductManager()
    is_featured = FeaturedProductManager()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    tags = TaggableManager()

    def __str__(self):
        return str(self.title)

    def get_price(self):
        return self.sale_price

    class Meta:
        unique_together = ('title', 'slug')


class ProductImage(models.Model):
    title = models.CharField(max_length=220, null=True, blank=False)
    image = models.ImageField(upload_to='products/images/')
    thumbnails = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)


CATEGORY_NAMES = (
    ('vlisco', 'VLISCO'),
    ('chiganvy', 'CHYGANVY'),
    ('hollandais', 'HOLLANDAIS'),
    ('hitarger', 'HITARGET'),
    ('heritage_by_sunshine', 'HERITAGE BY SUNSHINE'),
    ('metro', 'METRO'),
    ('wax', 'WAX'),
    ('so_special', 'SO SPECIAL'),
    ('sejection', 'SEJECTION'),

)


class ProductCategory(models.Model):
    name = models.CharField(max_length=120, choices=CATEGORY_NAMES, default='vlisco')
    product_title = models.CharField(max_length=128, null=False, blank=False)
    product_color = models.CharField(max_length=128, null=False, blank=False)
    product_theme_color = models.CharField(max_length=128, null=False, blank=False)
    product_theme_writing = models.CharField(max_length=228, null=True, blank=True)
    product_reference = models.TextField()
    product_origin_country = models.CharField(max_length=128, null=True, blank=True)
    production_year = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name + ' ' + self.product_title + 'Couleur ' + self.product_color)


class DealOfTheWeek(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    other_notes = models.TextField(max_length=220)
    category = models.OneToOneField('ProductCategory', null=True, blank=True, on_delete=models.CASCADE)
    normal_price = models.DecimalField(decimal_places=2, max_digits=100, default=6500)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, default=6500)
    quantity_in_stock = models.IntegerField()
    images = models.ManyToManyField('ProductImage')
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    valid_from = models.DateTimeField(default=timezone.now())
    valid_to = models.DateTimeField()
    objects = models.Manager()
    is_active = ActiveProductManager()
    is_featured = FeaturedProductManager()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    tags = TaggableManager()

    
    def __str__(self):
        return str(self.title)



"""class Review(models.Model):
    RATINGS = ((5,5),(4,4),(3,3),(2,2),(1,1),)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField()
    objects = models.Manager()
    approved = ActiveReviewManager()"""

class ProductReview(models.Model):
    RATINGS = ((5,5),(4,4),(3,3),(2,2),(1,1),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(('Title'), max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(('Your Rating'), default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField(('Your Review'))
    objects = models.Manager()
    approved = ActiveProductReviewManager()
    

class ProductAnonymousReview(models.Model):
    RATINGS = ((5,5),(4,4),(3,3),(2,2),(1,1),)
    email = models.EmailField()
    complete_name = models.CharField(('Name'), max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(('Title'),max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(('Your Rating'), default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField(('Your Review'))
    objects = models.Manager()
    approved = ActiveProductReviewManager()

