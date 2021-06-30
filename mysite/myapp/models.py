from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Category nomi', max_length=20)

    def __str__(self):
        return self.name

class Question(models.Model):
    fani = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='fani')
    text = models.CharField(max_length=1000,verbose_name='savol')

    def __str__(self):
        return self.text

class Choice(models.Model):
    text = models.CharField(max_length=1000,verbose_name='javob')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

