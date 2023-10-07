from django.db import models


class Rating(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    name = models.CharField(verbose_name='Фильм', max_length=20)
    rating = models.CharField(verbose_name='Оценка', max_length=2, choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.name}'
