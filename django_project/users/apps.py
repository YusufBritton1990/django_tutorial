from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """
        signals: User ability to create and save. makes a profile and user at
        the same time
        """
        import users.signals
