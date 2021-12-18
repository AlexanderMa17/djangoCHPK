from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')


class Member(models.Model):
    firstname = models.CharField (max_length=200)
    lastname = models.CharField (max_length=200)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    contact = models.CharField(max_length=100, blank=True)


class Meta:
    db_table = "web_member"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

