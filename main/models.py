from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from tools.slug_generator import slugify
from datetime import datetime


User = get_user_model()

class Marka(models.Model):

    
    title = models.CharField('Basligi', max_length=120)
    image = models.ImageField(_('Image'), upload_to='marka_image', blank=True, null=True)
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)


    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Marka'
        verbose_name_plural = 'Markalar'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title}" 

    def save(self,*args, **kwargs):
        
        title = self.title
        self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()
    
    # def get_absolute_url(self):
    #     return reverse_lazy('tours:tour-detail', kwargs={'slug': self.slug})


class Modell(models.Model):
    
    # relation's
    marka_id = models.ForeignKey(Marka, verbose_name="Marka", 
                                on_delete=models.CASCADE, db_index=True,related_name="marka_model")



    title = models.CharField('Basligi', max_length=120)
    image = models.ImageField(_('Image'), upload_to='model_image', blank=True, null=True)
    min_year = models.IntegerField("Minimal Buraxilis ili", null=True, blank=True)
    max_year = models.IntegerField("Maksimal buraxilis ili", null=True, blank=True)
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)



    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Model'
        verbose_name_plural = 'Modeller'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title}" 

    def save(self,*args, **kwargs):
        
        title = self.title
        self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()
    
    # def get_absolute_url(self):
    #     return reverse_lazy('tours:tour-detail', kwargs={'slug': self.slug})


class WishList(models.Model):

    
    # relation's
    marka_id = models.ForeignKey(User, verbose_name="User", 
                                on_delete=models.CASCADE, db_index=True,related_name="user_marka")


    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Arzu Listi'
        verbose_name_plural = 'Arzu Listleri'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.id}" 

    def save(self,*args, **kwargs):
        
        title = self.title
        self.slug = f"{slugify(self.created_at)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save()
    
    # def get_absolute_url(self):
    #     return reverse_lazy('tours:tour-detail', kwargs={'slug': self.slug})