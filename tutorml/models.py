from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    category = models.CharField("Категория", max_length=20)
    pub_date = models.DateTimeField('Дата публикации')
    img_path = models.CharField("Путь к изображению", default="tutorml/img/blank.png", max_length=100)
    views = models.IntegerField("Просмотры", default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Dataset(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    category = models.CharField("Категория", max_length=20)
    file = models.CharField("Сссылка на датасет", default="tutorml/datasets/", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Датасет"
        verbose_name_plural = "Датасеты"


class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=100)
    answer = models.TextField("Ответ")

    def __str__(self):
        return self.question


class Subscription(models.Model):
    email = models.EmailField("Почта", unique=True)
    notify_tutorials = models.BooleanField("Оповещать о туториалах", default=False)
    notify_datasets = models.BooleanField("Оповещать о датасетах", default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Question(models.Model):
    text = models.CharField("Текст вопроса", max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField("Текст выбора", max_length=200)
    votes = models.IntegerField("Голоса", default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Выбор"
        verbose_name_plural = "Выборы"
