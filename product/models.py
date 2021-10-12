from django.db import models
from django.db.models.base import Model
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from tools.slug_generator import slugify
from datetime import datetime
from main.models import *


User = get_user_model()



class Category(models.Model):

    parent_category = models.ForeignKey('self', verbose_name='Parent Category', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_categories', blank=True, null=True)

    title = models.CharField(_('Title'), max_length=120)
    image = models.ImageField(_("Image") , upload_to='product_image', null=True, blank=True)
    category_order = models.IntegerField(_("Category Order"))
    slug = models.SlugField(('slug'), max_length=255, editable=False, unique=True)



     #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title}" 

    def save(self,*args, **kwargs):
        
        title = self.title
        self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()

# Create your models here.
class Product(models.Model):
    
    # relation's
    user_id = models.ForeignKey(User, verbose_name="User", 
                                on_delete=models.CASCADE, db_index=True,related_name="user_product")
    modell_id = models.ForeignKey(Modell, verbose_name="Model",
                                on_delete=models.CASCADE, db_index=True, related_name="model_product")
    category_id = models.ForeignKey(Category, verbose_name=_("Category"), 
                                on_delete=models.CASCADE, db_index=True, related_name="category_product")    


    title = models.CharField(_('Title'), max_length=120)
    description = models.TextField(_("Description"), null=True,blank=True)
    vin_code = models.CharField(_("Vin code"), max_length=120, null=True, blank=True)
    price = models.DecimalField(_('Qiymet'),max_digits=6, decimal_places=2)
    discount = models.DecimalField(_('Discount Percentage'),max_digits=6, decimal_places=2)
    main_image = models.ImageField(_("Main Image") , upload_to='product_image', null=True, blank=True)
    image = models.ImageField(_('Image'), upload_to='product_image', blank=True, null=True)
    slug = models.SlugField(('slug'), max_length=255, editable=False, unique=True)
    is_discount = models.BooleanField(_("Is Discount") , default=False)


    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title}" 

    def save(self,*args, **kwargs):
        
        title = self.title
        self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()
    
    # def get_absolute_url(self):
    #     return reverse_lazy('tours:tour-detail', kwargs={'slug': self.slug})
