from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


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


class Scope(models.Model):
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
    scopes             = models.ManyToManyField('Scope')
    project_directions = models.CharField(max_length=255, blank=True)
    organization       = models.CharField(max_length=255, blank=True)
    name               = models.CharField(max_length=255, blank=True)
    purpose            = RichTextUploadingField()
    requirements       = RichTextUploadingField()
    description        = RichTextUploadingField()
    cost_min           = models.IntegerField(default=0)
    cost_max           = models.IntegerField(default=0)
    link_to_documents  = models.CharField(max_length=255, blank=True)
    link_to_official   = models.CharField(max_length=255, blank=True)
    contacts           = RichTextUploadingField()
    link_to_npa        = models.CharField(max_length=2055, blank=True)
    status             = models.CharField(max_length=3, choices=STATUSES, default='EDT', blank=True)


    def participants_list(self):
        return list(Participant.objects.all())

    def scopes_list(self):
        return list(Scope.objects.all())

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
        return self.scope

    def project_directions_list(self):
        return self.project_directions.split(';')

    def contacts_list(self):
        return self.contacts.split(';')

    def document_urls_list(self):
        return self.link_to_documents.split(';')

    def official_urls_list(self):
        return self.link_to_official.split(';')

    def npa_urls_list(self):
        return self.link_to_npa.split(';')

    def __str__(self):
        return self.name
