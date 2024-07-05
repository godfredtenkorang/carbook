from django.db import models
from django.urls import reverse

CAR_TRANSMISSION = (
    ("Automatic", "Automatic"),
    ("Manuel", "Manuel")
)

DRIVE_TYPE = (
    ("Self Drive", "Self Drive"),
    ("With a Driver", "With a Driver"),
)

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, default="", null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-date_added']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("list-category", args=[self.slug])
    
class CarForRent(models.Model):
    category = models.ForeignKey(Category, related_name='vehicle', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    seater = models.IntegerField(default=5)
    car_model = models.CharField(max_length=200, default="")
    transmission = models.CharField(max_length=100, default='Automatic', choices=CAR_TRANSMISSION)
    drive_type = models.CharField(max_length=100, default='With a Driver', choices=DRIVE_TYPE)
    color = models.CharField(max_length=100, default='Black')
    image = models.ImageField(upload_to='car_for_rent')
    accra_price = models.DecimalField(max_digits=5, decimal_places=2)
    outside_price = models.DecimalField(max_digits=5, decimal_places=2)
    just_accra = models.BooleanField(default=False)
    outside_accra = models.BooleanField(default=False)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Cars For Rent'
        ordering = ['-date_added']
        
    def __str__(self):
        return self.name
    
class FeaturedCarForRent(models.Model):
    category = models.ForeignKey(Category, related_name='homevehicle', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    seater = models.IntegerField(default=5)
    car_model = models.CharField(max_length=200, default="")
    transmission = models.CharField(max_length=100, default='Automatic', choices=CAR_TRANSMISSION)
    drive_type = models.CharField(max_length=100, default='With a Driver', choices=DRIVE_TYPE)
    color = models.CharField(max_length=100, default='Black')
    image = models.ImageField(upload_to='car_for_rent')
    accra_price = models.DecimalField(max_digits=5, decimal_places=2)
    outside_price = models.DecimalField(max_digits=5, decimal_places=2)
    just_accra = models.BooleanField(default=False)
    outside_accra = models.BooleanField(default=False)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Featured Cars For Rent'
        ordering = ['-date_added']
        
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.fullname