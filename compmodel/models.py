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
    # in here MESystem.__dict__ goes
    body = models.JSONField(null=False,blank=False) 
    # django 4.2.7 does not have JSONField listed in documentation,
    # however it does mentions HStoreField that exhibits exact same behaviour
    # proposal: substitute body with arrays of charfields
    name = models.CharField(max_length=50,null=False,blank=True)

class Solution(models.Model):
    """
        Класс решения модели. содержит внешний ключ, указывающий на модель, при удалении модели
    удаляется и решение. Поле body представляет собой JSON как и модель, но без null значений.
    """
    model = models.ForeignKey(CompModel,on_delete=models.CASCADE,null=False)
    body = models.JSONField(null=False,blank=False)

#class DataSet(models.Model):
    
