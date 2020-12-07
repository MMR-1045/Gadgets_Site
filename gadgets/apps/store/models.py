from django.db import models

# Create your models here.
class Category(models.Model):
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    # ordering = models.IntegerField(default=0)
    # is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'
        # ordering = ('ordering',)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return '/%s/' % (self.slug)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # is_featured = models.BooleanField(default=False)
    # num_available = models.IntegerField(default=1)
    # num_visits = models.IntegerField(default=0)
    # last_visit = models.DateTimeField(blank=True, null=True)

    # image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('-date_added',)

    def __str__(self):
        return self.title