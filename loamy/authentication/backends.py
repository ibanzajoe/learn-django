import jwt

from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = "token"

    def authenticate(self, request):
        """
        The 'authenticate' method is called on every request regardless of whether the
        end point requires authentication.

        'authenticate' has two possible return values:
        1. 'None' - authentication will fail
        2. '(user, token)' = we return a user / token combination if auth success!
        3. if Neither, raise AuthenticationFailed
        """

        request.user = None

        # auth header should be ["token", "JWT"]
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None  # Invalid token header, no credentials, auth failed

        elif len(auth_header) > 2:
            return None  # Invalid token header, Token Name should have no spaces. auth failed.

        prefix = auth_header[0].decode("utf-8")
        token = auth_header[1].decode("utf-8")

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Try auth, if Auth Success => return user / token.
        If Auth Fail => throw an error.
        """
        try:
            print(token, settings.SECRET_KEY)
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms="HS256")
            print("Post Payload", payload)
        except:
            msg = "Invalid authentication. Cound not decode token."
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload["id"])
        except User.DoesNotExist:
            msg = "No user by this token"
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "This user has been deactivated."
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
