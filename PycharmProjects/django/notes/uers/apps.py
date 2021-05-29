from django.apps import AppConfig


class UersConfig(AppConfig):
    name = 'uers'

    def ready(self):
        import uers.signals
