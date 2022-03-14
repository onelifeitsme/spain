#!coding:utf-8
from django.apps import AppConfig


class PublicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.publications'
    verbose_name = 'Публикации'
