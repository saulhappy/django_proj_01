from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage

PROTECTED_MEDIA = getattr(settings, 'PROTECTED_MEDIA', None)

if not PROTECTED_MEDIA: raise ImproperlyConfigured("PROTECTED_MEDIA not set in settings.py")

class ProtectedStorages(FileSystemStorage):
    location = PROTECTED_MEDIA