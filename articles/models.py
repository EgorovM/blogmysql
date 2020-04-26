from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

"""
• Сфера (если несколько то они должны идти отдельно, так как по том по ним будет отдельный поиск)
• Направления проектов (если несколько то они должны идти отдельно, так как по том по ним будет отдельный поиск)
• Организация
• Наименование
• Цель финансирования (если несколько то они должны идти отдельно, так как по том по ним будет отдельный поиск)
• Требования к участнику
• Описание
• Сумма
• Ссылка на Документы
• Ссылка на официальный источник
• Контакты организатора
• Ссылка НПА
"""


class City(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUSES = [
        ('PUB', 'Опубликовано'),
        ('EDT', 'Редактируется'),
        ('DEL', 'Удалено')
    ]

    city               = models.ForeignKey('City', on_delete=models.CASCADE, null=True, blank=True)
    category           = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    source             = models.ForeignKey('Source', on_delete=models.CASCADE, null=True, blank=True)
    participants       = models.ManyToManyField('Participant')
    grade              = models.ForeignKey('Grade', on_delete=models.CASCADE, null=True, blank=True)
    scope              = models.CharField(max_length=255, blank=True)
    project_directions = models.CharField(max_length=255, blank=True)
    organization       = models.CharField(max_length=255, blank=True)
    name               = models.CharField(max_length=255, blank=True)
    purpose            = models.CharField(max_length=255, blank=True)
    requirements       = models.CharField(max_length=255, blank=True)
    description        = RichTextUploadingField()
    cost               = models.CharField(max_length=255, blank=True)
    link_to_documents  = models.CharField(max_length=255, blank=True)
    link_to_official   = models.CharField(max_length=255, blank=True)
    contacts           = models.CharField(max_length=255, blank=True)
    link_to_npa        = models.CharField(max_length=255, blank=True)
    status             = models.CharField(max_length=3, choices=STATUSES, default='EDT', blank=True)


    def participants_list(self):
        return list(Participant.objects.all())

    def cities_list(self):
        return City.objects.all()

    def grades_list(self):
        return Grade.objects.all()

    def categories_list(self):
        return Category.objects.all()

    def sources_list(self):
        return Source.objects.all()

    def get_participants(self):
        return self.participants

    def scope_list(self):
        return self.scope.split(';')

    def project_directions_list(self):
        return self.project_directions.split(';')

    def contacts_list(self):
        return self.contacts.split(';')

    def __str__(self):
        return self.name
