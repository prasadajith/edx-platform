"""
Programs Configuration
"""


from django.apps import AppConfig


class ProgramsConfig(AppConfig):
    """
    Default configuration for the "openedx.core.djangoapps.programs" Django application.
    """
    name = u'openedx.core.djangoapps.programs'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals  # pylint: disable=unused-variable
