from django.db import models
from datetime import datetime
import os
from django.conf import settings

# Create your models here.

#https://djbook.ru/rel1.9/topics/db/models.html#model-inheritance - наследование моделей

class Tag(models.Model, ):
    tag_name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.tag_name}'

class Article(models.Model):
    article_name = models.CharField(max_length = 100, null = True)
    article_text = models.CharField(max_length = 1000, null = True)
    article_date = models.DateTimeField(default = datetime.now())
    article_tag  = models.ManyToManyField(Tag)
    article_img = models.ImageField(upload_to = 'articles', null = True, blank = True)
    #, default = os.path.join(settings.MEDIA_ROOT,'articles','happy_lion.jpg')

    '''
    DataField - дата
    TimeField - время
    
    Числовые типы:
    IntegerField
    PositeveIntegerField
    FloatField
    
    Логические типы:
    BooleanField
    
    Байтовый тип:
    BinaryField
    
    Email:
    EmailField
    
    URL:
    URLField
    
    Image:
    ImageField
    '''

    def __str__(self):
        return f'{self.article_name}, published: {self.article_date}'

