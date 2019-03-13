from django.db import models

class Specialist (models.Model):
    name = models.CharField(verbose_name='ФИО', max_length = 300 )

    info = models.CharField(verbose_name='Инфо о специалисте',max_length=10000)

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Специалисты"
        verbose_name = "Специалист"


class Recording (models.Model):
    name = models.CharField(verbose_name='ФИО ', max_length=300)
    brand = models.CharField(verbose_name='Марка автомобиля', max_length=10000)
    specialist = models.ForeignKey( Specialist, verbose_name='Специалист ',on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата записи ')
    time = models.CharField(verbose_name='Время  ', max_length=5)

    def __str__(self):
        return ' %s' % self.id

    class Meta:
        verbose_name_plural = "Записи"
        verbose_name = "Запись"

