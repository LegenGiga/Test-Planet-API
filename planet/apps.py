from django.apps import AppConfig


class PlanetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'planet'

    def ready(self):
        import planet_api.signals
