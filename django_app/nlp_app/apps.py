from django.apps import AppConfig


class NlpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nlp_app'


    def ready(self):
        # Importa el módulo signals para que se conecten las señales
        import nlp_app.signals