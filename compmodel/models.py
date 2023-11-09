from django.db import models
from django.contrib.auth.models import User

class CompModel(models.Model):
    """
        Compartment model ehehehe
    содержит неявно объявленное поле id - primary key, это внутрений механизм джанго
    author foreign key user - вторичный ключ, ссылающийся на сущность пользователя 
    django.contrib.auth.models.User.
    body text - безразмерное текстовое поле, хранящее модель в промежуточном
    представлении в сериализованной форме. целостность модели проверяется
    при первичном создании и каждой десериализации.
    """
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    body = models.TextField(null=False,blank=False,default='{"volumes": [], "transfers": [], "outgos": [], "name": "", "comment": "", "__system__": true}')
    name = models.CharField(50,null=False,blank=True)
