from django.apps import AppConfig


class OpaiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'opai'
    def ready(self):
        import opai.signals