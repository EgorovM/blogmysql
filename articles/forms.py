from ckeditor.widgets import CKEditorWidget
from django import forms


class PostEditForm(forms.Form):
    description = forms.CharField(widget=CKEditorWidget, label='Описание')
    requirements = forms.CharField(widget=CKEditorWidget, label='Требования к участнику')
    contacts = forms.CharField(widget=CKEditorWidget, label='Контакты организации')
