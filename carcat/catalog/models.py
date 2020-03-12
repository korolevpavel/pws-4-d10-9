from django.db import models

TRANSMISSION_CHOICE = [
    (1, "механика"),
    (2, "автомат"),
    (3, "робот"),
]

class Producer(models.Model):
    name = models.CharField('Производитель', max_length=150)

class Color(models.Model):
    name = models.CharField('Производитель', max_length=150)

class Car(models.Model):
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True)
    model_of_car = models.CharField('Модель', max_length=150, null=True)
    year = models.IntegerField('Год выпуска', null=True)
    transmission = models.SmallIntegerField('Коробка передач', choices=TRANSMISSION_CHOICE, null=True)
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
