from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    
    def ready(self):
        from . import signals