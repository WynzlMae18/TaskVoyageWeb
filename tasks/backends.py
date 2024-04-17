

from django.contrib.auth.backends import BaseBackend
from .models import CustomUser  # Import your custom user model

class CustomUserAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None):
        if username is not None:
            # Check authentication by username
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                user = None
        elif email is not None:
            # Check authentication by email
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None
        else:
            # Neither username nor email provided
            return None

        if user is not None and user.check_password(password):
            return user
        else:
            return None